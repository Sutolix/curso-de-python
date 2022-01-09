def fizzbuzz(number):
    if number % 5 == 0 & number % 3 == 0:
        return 'FizzBuzz'

    if number % 3 == 0:
        return 'fizz'

    if number % 5 == 0:
        return 'buzz'

    return number


print(fizzbuzz(15))
