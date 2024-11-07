"""
CSV Handling done the hard way...

Without using either the csv module or pandas, we have to do a fair amount of work to parse 
and process a CSV file.
"""

import re

from datetime import datetime


def parse_file(filepath: str) -> tuple:
    """
    Parses a CSV file and returns the headers and data as a tuple

    There are a lot of things we have to handle when parsing a CSV file:
    - Quoted fields - like the "Name" column, where a comma separates the first and last names
    - Empty fields - like the "Middle Name" column, where some rows have no value
    - Empty lines - the file might have empty lines at the end
    - Leading/trailing whitespace - we have to strip it from each line and each field
    - Newlines - we have to strip them from each line
    - Encoding - we have to specify the encoding when opening
    - Headers - we have to read the first line separately to get the column names

    We're not handling:
    - File not found - if the file doesn't exist, we'll get an error raised by open()
    - File permissions - if the file is read-only, we'll get an error raised by open()
    - File too large - if the file is too large to fit in memory, we'll run out of memory
    - Invalid CSV - if the file isn't a valid CSV file, we'll get errors parsing it
    - Memory usage - we're reading the entire file into memory, which might be a problem for large files
    - Performance - we're reading the file line by line, which might be slow for large files
    - Error handling - we're not handling any errors that might occur during parsing
    - CSV dialects - we're assuming the CSV file is comma-separated with double quotes for quoting
    - CSV options - we're not handling any options like delimiter, quotechar, or escapechar

    It's a lot of work to handle all these cases, which is why the csv module exists. It's always a
    good idea to stand on the shoulders of giants!

    Args:
        filepath: str: The path to the CSV file to parse
        
    Returns:
        tuple: A tuple containing:
         - a list of headers, and 
         - data as a list of lists
    """

    data = []

    # reading the file is simple enough
    with open(filepath, "r", encoding="utf-8") as file:
        # Read the header line separately to get the column names
        headers = file.readline().strip().split(",")

        # then we need to process each line in the file
        for line in file:

            # skip completely empty lines - in particular the last line of the file
            # might be empty
            if not line.strip():
                continue

            values = []
            value = ""
            in_quotes = False

            # we have to iterate over each character in the line to make sure
            # we parse the data correctly
            for char in line.strip():
                if char == '"':
                    # Toggle in_quotes for quote handling
                    in_quotes = not in_quotes
                elif char == "," and not in_quotes:
                    values.append(value)
                    value = ""
                else:
                    value += char

            # Add the last field
            values.append(value)

            # Add the parsed row to the data list
            data.append(values)

    return headers, data


def calculate_column_widths(headers: list, records: list) -> list:
    """
    Calculates the maximum width of each column in the data.
    
    Not so efficient, but it works for small datasets. The efficiency of the
    algorithm is O(n*m) where n is the number of records and m is the number 
    of columns.

    Args:
        headers: list: The list of headers
        records: list: The list of records

    Returns:
        list: A list of integers representing the maximum width of each column
    """
    column_widths = [len(header) for header in headers]

    for record in records:        
        for i, value in enumerate(record):
            try:
                column_widths[i] = max(column_widths[i], len(str(value)))
            except IndexError:
                x = 1
    return column_widths


def print_formatted_table(column_widths: list, headers: list, records: list) -> None:
    """
    Prints the records to screen as a formatted table with equal column widths
    """
    header_row = " | ".join(f"{headers[i].ljust(column_widths[i])}" for i in range(len(headers)))
    divider = "-+-".join("-" * column_widths[i] for i in range(len(headers)))
    print(header_row)
    print(divider)

    for record in records:
        # note that we have to handle the case where the record has fewer fields than the headers
        # by using the ternary operator to check if i is less than the length of the record...
        formatted_row = " | ".join(
            f"{str(record[i]).ljust(column_widths[i])}" if i < len(record) else " " * column_widths[i]
            for i in range(len(headers))
        )
        print(formatted_row)


def reorder_columns(headers: list, records: list, column_name: str) -> tuple:
    """
    Reorders the specified column to be the first column in the data.
    
    Again, the efficiency of the algorithm is O(n*m) where n is the number of records and m is the number
    of columns.

    Args:
        headers: list: The list of headers
        records: list: The list of records
        column_name: str: The column to move to the first position

    Returns:
        tuple: Updated headers and records with the column moved to the first position
    """
    # find the index of the column to move
    col_index = headers.index(column_name)

    # move the specified column to the beginning of headers
    headers = [headers[col_index]] + headers[:col_index] + headers[col_index+1:]

    # reorder each record to have the specified column first
    reordered_records = []
    for record in records:
        # ensure the record has enough columns by padding with empty strings if needed.
        # otherwise, we'll get an index out of range error when we try to access the column
        # but the record has fewer columns than the header
        record = record + [""] * (len(headers) - len(record))
        reordered_record = [record[col_index]] + record[:col_index] + record[col_index+1:]
        reordered_records.append(reordered_record)

    return headers, reordered_records


def sort_by_date(records: list, date_col_index: int) -> list:
    """
    Sorts the records by the date column specified by date_col_index.
    
    Args:
        records: list: The list of records
        date_col_index: int: The index of the date column to sort by

    Returns:
        list: Sorted records by the specified date column
    """
    return sorted(records, key=lambda x: datetime.strptime(x[date_col_index], "%d/%m/%Y"))


def smart_parse_file(headers: list, filepath: str) -> tuple:
    """
    Parses a badly formatted CSV file and returns the headers and data as a tuple.
    
    Given that some of the field values aren't separated by commas, we're going to
    try to identify the fields based on their content. We're going to assume that:
    - A date is in the format DD/MM/YYYY
    - An email address contains an @ symbol
    - An ID is in the format 12345678-1234
    - A title is one of Mr., Ms., Mrs., or Dr.
    - A name contains a comma
    - A company is anything else

    Args:
        headers: list: The list of headers
        filepath: str: The path to the CSV file to parse
        
    Returns:
        tuple: A tuple containing:
         - a list of headers, and 
         - data as a list of lists
    """
    data = []
    
    # Regular expressions to match specific patterns
    date_pattern = re.compile(r"\d{2}/\d{2}/\d{4}")
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    id_pattern = re.compile(r"\d{8}-\d{4}")
    
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            # Skip completely empty lines
            if not line.strip():
                continue

            # Split the line by commas, handling quoted fields
            values = []
            value = ""
            in_quotes = False

            for char in line.strip():
                if char == '"':
                    in_quotes = not in_quotes
                elif char == "," and not in_quotes:
                    values.append(value.strip())
                    value = ""
                else:
                    value += char

            values.append(value.strip())  # Add the last field value

            # Initialize an empty record aligned with headers
            record = [""] * len(headers)
            
            # Determine which column each value corresponds to
            for value in values:
                if date_pattern.match(value):
                    record[headers.index("Updated")] = value
                elif email_pattern.search(value) and id_pattern.search(value):
                    # both email and ID are in the same field value
                    record[headers.index("Email")] = email_pattern.search(value).group()
                    record[headers.index("ID")] = id_pattern.search(value).group()
                elif email_pattern.search(value):
                    record[headers.index("Email")] = email_pattern.search(value).group()
                elif id_pattern.search(value):
                    record[headers.index("ID")] = id_pattern.search(value).group()
                elif value in {"Mr.", "Ms.", "Mrs.", "Dr.", ""}:
                    record[headers.index("Title")] = value
                elif "," in value:
                    record[headers.index("Name")] = value
                else:
                    record[headers.index("Company")] = value

            # Append the correctly ordered record to data
            data.append(record)

    # Return headers and data as a tuple to match the expected format
    return headers, data


def write_to_file(headers: list, records: list, filepath: str) -> None:
    """
    Writes the headers and records to a CSV file.
    
    Args:
        headers: list: The list of headers
        records: list: The list of records
        filepath: str: The path to the CSV file to write
    """
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(",".join(headers) + "\n")
        for record in records:
            file.write(",".join(record) + "\n")


def append_to_file(records: list, filepath: str) -> None:
    """
    Appends records to an existing CSV file with headers.
    
    Args:
        records: list: The list of records
        filepath: str: The path to the CSV file to append
    """
    with open(filepath, "a", encoding="utf-8") as file:
        for record in records:
            file.write(",".join(record) + "\n")


if __name__ == "__main__":
    print("Exercise 1\n")
    header_fields, row_data_1 = parse_file("PeopleTrainingData.csv")
    widths = calculate_column_widths(header_fields, row_data_1)
    print_formatted_table(widths, header_fields, row_data_1)

    print("\nExercise 2: reordering columns and ordering by Updated date\n")
    header_fields, row_data_1 = reorder_columns(header_fields, row_data_1, "Updated")
    row_data = sort_by_date(row_data_1, 0)
    widths = calculate_column_widths(header_fields, row_data_1)
    print_formatted_table(widths, header_fields, row_data_1)
    write_to_file(header_fields, row_data_1, "PeopleTrainingDataUpdateCLEANED.csv")

    print("\nExercise 3: parsing a badly formatted CSV file\n")
    headers, row_data_2 = smart_parse_file(header_fields, "PeopleTrainingDataUpdate.csv")
    header_fields, row_data_2 = reorder_columns(header_fields, row_data_1, "Updated")
    row_data = sort_by_date(row_data_2, 0)
    widths = calculate_column_widths(header_fields, row_data_2)
    print_formatted_table(widths, header_fields, row_data)
    append_to_file(row_data, "PeopleTrainingDataUpdateCLEANED.csv")