# fizz buzz algorithm
# replace numbers that are only divisible by 3 with 'Fizz'
# replace numbers that are only divisible by 5 with 'Buzz'
# replace numbers that are both divisible by 3 and 5 with 'FizzBuzz'
# return every other number as is

target = 100

for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
