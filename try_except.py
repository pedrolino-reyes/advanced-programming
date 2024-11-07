numbers = [
  (30, 3),
  (5, 45),
  (0, 0),
  (0, 1),
  (7, 6),
]

for num1, num2 in numbers:
    try:
        if num1 > num2:
            if num1%num2 == 0:
                print(num1, " is a multiple of ", num2)
        else:
                # this is invalid syntax: if num2%num1 == 0:Missing E
                if num2%num1 == 0:
                    print(num2, " is a multiple of ", num1)
    except ZeroDivisionError:
        print("You cannot divide by zero")
    