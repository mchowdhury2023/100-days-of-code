def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        print("fizzBuzz")
    elif input % 3 == 0:
        print("fizz")

    elif input % 5 == 0:
        print("buzz")

    else:
        print(input)

fizz_buzz(7)