# 2.4 Activity 1: Constructing data formats

## 1. An XML DTD lacks type constraints which were resolved by the introduction of an XML Schema. JSON has basic typing built in:

**Why is the concept of 'types' important?**

First, I'm not sure that the basic typing offered by JSON is very widely used. It's very common these days for developers to rely on JSON Schema or the very similar OpenAPI Specification to provide validation rules for JSON documents. The basic typing in JSON is cumbersome and not overly useful, while JSON Schemas and OAS files can provide fairly detailed validation requirements for data. XML Schemas (XSD) are also 

Typing is just one part of the validation puzzle, the other part being that the data actually makes sense as well as being the right data type. Simply checking that a piece of data is a string or an integer is not as useful as validating that the string represents a valid date, or that an integer lies within a certain accepted range, for example. 

Type checking is really just a first level of validation. It's important in the sense that it may at least save time further down the line since you have predictability over the data type that you will receive so there might not be the need for so much error handling by systems that are consuming the data. Nevertheless, defensive coding practices are generally a good idea anyway, and a lot of developers will write routines to handle cases where the data isn't as expected.



**What would be the advantages and/or disadvantages if there were no types?**

A big advantage of not defining types is that you can save time when creating documents - often, defining accurate and useful validation schemas can take time. This is an advantage for producers of data. A lot of data providers still just issue data in CSV files, leaving data validation to the consumer.

So, an obvious disadvantage of not declaring types is that consumers have to write their own validation routines to check the data type before proceeding to process the data. Again, this isn't so dreadful in a lot of cases, since consumers are likely to include such routines as a matter of course anyway to defend against errors. But it does mean that there's no guarantee of predictability of the data.

Predictability is very useful when you start designing systems to work together, in particular when you might want to create a "fake" data provider for development purposes. A common pattern in software development, particularly now that microservices are becoming more popular, is for teams to develop systems in tandem. The consumer system may be built before the producer system has been finalised. In this case, defining the data schema upfront has the benefit that the consumer system can be built and tested according to a pre-defined "contract" of how the producer system is going to behave. Without such a contract, the consumer system cannot be finalised until the producer system has been completed, which can hold up the development cycle.



**Considering some programming languages adhere to the principle of "Duck typing", would this be a better approach to structuring documents for use with programs?**

Duck typing will only go so far, I believe. For example, in Python an integer and a string do have some common methods and operations available to them, but in a lot of common cases you'll find that the operations you want to perform on a string will throw an error if you perform them on an integer.

- You can call str() on either an integer or a string, converting them to a string. But if you're expecting a string, why would you call this method?
- You can use the `+` operator for both integers and strings. But 1 + 1 = 2 while "A" + "B" = "AB"
- You can used the `*` operator for both. But 1 * 2 = 2 while "A" * 2 = "AA", and "A" * "A" will throw an exception
- You can format a string using either, e.g. with f-strings: `f"Hello {1}"` = "Hello 1" and `f"Hello {world}`= "Hello world"

In reality, although there's a degree of duck typing here, it's not so useful. Also, it can lead to unexpected issues. For example, in JavaScript, you can do the following

```
1 + 1 // results in 2
"1" + 1 // results in 11
```

When all is said and done, though, CSV data is read in as text in most cases, and programs just have to spend a bit of time at the beginning cleaning the data and setting the appropriate data type for each value. CSV is still very widely used, so it's quite possible to do things this way. A lot of tooling exists to try to infer the data type based on the data - just try importing a CSV file into Excel. Databricks is a very popular platform for data engineering, and Databricks will also attempt to automatically infer data. Nevertheless, it must be said that this process can slow down the file loading process (especially for large files - which are often going to be used in modern data engineering projects), and defining the schema upfront will improve processing times.

## 2. Both JSON and XML are considered semi-structured data representations, whereas CSV is classified more towards unstructured, or minimally structured. There are considerable overheads with writing both JSON and XML, whereas CSV has been and is still used effectively.

**What do we gain from semi-structured data, and given the current advances in application development, is this gain essential to moving technology forward?**

Semi-structured data can offer us more flexibility and easier adaptability when it comes to consuming data. If you consider a relational SQL database, then each column and its data type needs to be defined upfront. Database model classes are defined strictly according to this schema too. And then if the data changes one day, the system needs to be re-engineered to accommodate the changes. In a lot of environments these days, data producers can and will change the format of the data they're providing more frequently than a development team will want to re-engineer their system. Additional columns might be sent that consumers don't need to worry about, but they might have to update their systems just to handle these columns. I saw this a lot when working with a system that consumed the Facebook Ads API many years ago - there was constant rework required to handle changes to the data that was being received, so we could write that data to an SQL database.

Big data frameworks - Spark, Hadoop, Databricks, are designed to handle diverse data for this reason. Data scientists and analysts are freed up to analyse and explore the data without first needing to worry about defining schemas. Semi-structured data has enough structure to allow the data to be used by a machine, but not so much that a large amount of time needs to be invested in modelling the data perfectly. Given the time-saving benefit, it's maybe not *essential*, but it is definitely *preferable*.