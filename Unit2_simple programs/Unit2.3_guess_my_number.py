# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 15:32:35 2021

@author: Dhanny Indrakusuma
Exercise: guess my number

In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer 
between 0 (inclusive) and 100 (not inclusive).
The computer makes guesses, and you give it input - is its guess too high or too low?
Using bisection search, the computer will guess the user's secret number!

**Hint: Endpoints
** Your program should use bisection search. So think carefully what that means.
What will the first guess always be?
How should you calculate subsequent guesses?

** Your initial endpoints should be 0 and 100. Do not optimize your subsequent 
endpoints by making them be the halfwaypoint plus or minus 1. Rather, 
just make them be the halfway point.

Note: your program should use input to obtain the user's input! 
Be sure to handle the case when the user's input is not one of h, l, or c.
When the user enters something invalid, you should print out a message 
to the user explaining you did not understand their input.
Then, you should re-ask the question, and prompt again for input. 
"""

print("Please think of a number between 0 and 100!")
# assigning high and low values 0 to 100
epsilon = 1
low = 0
high = 100

# loop until it guess correctly
while (high - low) > epsilon:
    # Bisection search: guess the midpoint between our current high and low guesses
    ans = (high + low)//2
    print("Is your secret number " + str(ans) + "?")
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if guess == 'h': # guessed number too high
        high = ans
    elif guess == 'l': # guessed number too low
        low = ans
    elif guess == 'c': # correct guess!
        break
    else: # unwanted input
        print("Sorry, I did not understand your input.")
    
print("Game over. Your secret number was:", ans)


"""
Here is a transcript of an example session:

Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 87?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 81?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 84?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 82?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 83?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 83
"""