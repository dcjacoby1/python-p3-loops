#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    return [i ** 2 for i in int_list]
    

def fizzbuzz():
    for i in range(100):
        if (i + 1) % 5 == 0 and (i + 1) % 3 == 0:
            print("FizzBuzz")
        elif (i + 1) % 3 == 0:
            print("Fizz")
        elif (i + 1) % 5 == 0:
            print("Buzz")
        else:
            print(f"{i + 1}")
        
