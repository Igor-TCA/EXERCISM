def steps(number):
    step = 0
    if not number > 0:
        raise ValueError("Only positive integers are allowed")
    while number != 1:
        if number % 2 == 0:
            number = number / 2
            step = step + 1
        else:
            number = (number * 3) + 1
            step = step + 1
    return step 