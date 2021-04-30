#!/usr/bin/python3
words = ["FizzBuzz" if c % 3 == 0 and c % 5 == 0 else "Buzz" if c % 5 == 0
         else "Fizz" if c % 3 == 0 else str(c) for c in range(1, 101)]
print(words)

"""
    This exercise, is the same as the 12-fizzbuzz.py
    task using list comprehension

    Syntax:
            list_name = [expression1 if condition1 else expression2
                         if condition2 else expression3 if expression3
                         else expression4 for item in iterable]

    Output:
            ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz',
             'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17',
             'Fizz', '19', 'Buzz', 'Fizz', '22', '23', 'Fizz', 'Buzz',
             '26', 'Fizz', '28', '29', 'FizzBuzz', '31', '32', 'Fizz',
             '34', 'Buzz', 'Fizz', '37', '38', 'Fizz', 'Buzz', '41',
             'Fizz', '43', '44', 'FizzBuzz', '46', '47', 'Fizz', '49',
             'Buzz', 'Fizz', '52', '53', 'Fizz', 'Buzz', '56', 'Fizz',
             '58', '59', 'FizzBuzz', '61', '62', 'Fizz', '64', 'Buzz',
             'Fizz', '67', '68', 'Fizz', 'Buzz', '71', 'Fizz', '73',
             '74', 'FizzBuzz', '76', '77', 'Fizz', '79', 'Buzz', 'Fizz',
             '82', '83', 'Fizz', 'Buzz', '86', 'Fizz', '88', '89',
             'FizzBuzz', '91', '92', 'Fizz', '94', 'Buzz', 'Fizz',
             '97', '98', 'Fizz', 'Buzz']
"""
