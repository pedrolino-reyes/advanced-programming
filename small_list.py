names = "John, Paul, George, Ringo"
nameList = names.split()
try:
    print(nameList[1000])
except IndexError:
    print(f"Your list only has {len(nameList)} elements, I can't give you element 1000")