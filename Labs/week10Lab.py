# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: Wedaad Haruna
# date: 09-12-2020
# purpose: Week 10 Lab exercise

from abc import ABC, abstractmethod


class MathsGame(ABC):
    print("WELCOME TO THE GAME")

    @abstractmethod
    def game_play(self):
        pass


class Fibonacci(MathsGame):
    def __init__(self):
        self.counter = 0
        self.game_option = int(input("Please enter in 1 to play and 2 to exit: "))

    # overriding abstract method
    def game_play(self):
        if type(self.game_option) != int:
            raise TypeError

        self.counter += 1

        while self.counter == 1:
            if self.game_option == 1:
                print("**Inside while loop and the game option is 1**")
                print("**Inside if statement and counter is: ", self.counter)
                int(input("Please enter in the amount of terms you want in this sequence: "))
                print("**User has just entered the number of terms")
                break

            elif self.game_option == 2:
                print("Option 2 was chosen, GAME OVER")
                break

        else:
            print("Incorrect value entered please enter 1 to play and 2 to exit")


fib_game = Fibonacci()
fib_game.game_play()
