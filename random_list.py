randomList = ['67', 53, '3O',72, '10']

for i in randomList:
    try:
        print(int(i) * 10)
    except ValueError as msg:
        msg = str(msg)
        if msg.startswith("invalid literal for int() with base 10"):
            print(f"For the value '{i}', it looks like you have mixed letters and numbers.")
        else:
            print("I don't know what went wrong")