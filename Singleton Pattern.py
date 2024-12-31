from abc import ABC, abstractmethod
import os
import random
import time

class Singleton:
    instance = None
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
class Shape(ABC, Singleton):
    @abstractmethod
    def sides(self):
        pass
class Circle(Shape):
    def sides(self):
        return "0"
class Square(Shape):
    def sides(self):
        return "4"
class Triangle(Shape):
    def sides(self):
        return "3"
class Game:
    def __init__(self):
        self.sides = None
        self.circle_count = 0
        self.triangle_count = 0
        self.square_count = 0
        self.correct_guesses = 0
        self.incorrect_guesses = 0
    def leaderboard(self):
        print("\nLeaderboard: \n")
        print(f"Circle Count: {self.circle_count} ")
        print(f"Square Count: {self.square_count} ")
        print(f"Triangle Count: {self.triangle_count} ")
        print(f"Correct Guesses Count: {self.correct_guesses} ")
        print(f"Inforrect Guesses Count: {self.incorrect_guesses} \n")
    def random_sides(self):
        self.sides = random.choice(["0", "3", "4"])
        return self.sides
    def question(self):
        return f"\nWhat shape has {self.random_sides()} sides?"
    def game(self):
        while True:
            print(self.question())
            print("\nSelect an Option: \n")
            print("1. Circle")
            print("2. Square")
            print("3. Triangle")
            print("4. Reset Question and Terminal")
            print("5. Return to Main Menu")
            option = input("Select a menu option: ")
            if option == "1" and "0" == self.sides:
                choice = Circle()
                self.circle_count += 1
                self.correct_guesses += 1
                print(f"A circle has {choice.sides()} sides: {id(choice)}")
            elif option == "2" and "4" == self.sides:
                choice = Square()
                self.square_count += 1
                self.correct_guesses += 1
                print(f"A square has {choice.sides()} sides: {id(choice)}")
            elif option == "3" and "3" == self.sides:
                choice = Triangle()
                self.triangle_count += 1
                self.correct_guesses += 1
                print(f"A triangle has {choice.sides()} sides: {id(choice)}")
            elif option == "4":
                self.cls()
            elif option == "5":
                print("Returning to main menu...")
                break
            else:
                self.incorrect_guesses +=1
                print("Wrong guess you lose!")
                break    
    def cls(self):
        os.system('cls')
        time.sleep(0.1)
    def main_menu(self):
        while True:
            print("\nSelect a choice: ")
            print("1. Play Game")
            print("2. Scoreboard")
            print("3. Clear Terminal")
            print("4. End Game")
            option = input("Select a menu option: ")
            if option == "1":
                self.game()
            elif option == "2":
                self.leaderboard()
            elif option == "3":
                self.cls()
            elif option == "4":
                break
            else:
                print("Invalid input")
def main():
    run = Game()
    run.main_menu()
main()
