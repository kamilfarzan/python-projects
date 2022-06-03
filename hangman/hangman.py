import random
import time
import os

print("\n"*3)

def BeginGame():
    print("Welcome to Hangman!!\nThe Game will begin shortly...\n")
    time.sleep(2)
    print("Enter a letter each turn to narrow down the question. Five errors are allowed here.\nIf you want to go all in, enter the complete word. Here, only one error is allowed.\n")
    time.sleep(3)
    print("The question is getting chosen...\n")
    time.sleep(2)
    print("Here's the QUESTION: ")


def removeConsonants(string):
    out = ""
    for x in string:
        if x not in "AEIOU ":
            out += "_"
        else:
            out += x
    return out


def gameCheck(string, answer, entry):
    out = ""
    if entry == None:
        return None
    entry = entry.upper()
    if len(entry) == 1:
        if entry in answer and entry not in string:
            print("\nCorrect Letter!\n")
            for i in range(len(answer)):
                if answer[i] == entry:
                    out += entry
                else:
                    out += string[i]
            return 1, out
        else:
            print("\nWrong Letter!\n")
            return 0, string
    elif len(entry) > 1:
        if entry == answer:
            return win()
        else:
            return lose()


def lose():
    print("\nloser.")
    return "L"


def win():
    print("\nYOU WON!!")
    return "W"


def printStatus(question, wrongL):
    print(f"{question}       Errors: {wrongL}", end="\n\n")
    printStake(wrongL)


def printStake(wrongL):
    errs = len(wrongL)
    if errs == 0:
        print("   ______   ",
              "  /     |   ",
              "  |     |   ",
              "  |         ",
              "  |         ",
              "  |         ",
              "  |         ",
              "  |         ", sep="\n"
              )
    elif errs == 1:
        print("   ______   ",
              "  /     |   ",
              "  |     |   ",
              "  |     O   ",
              "  |         ",
              "  |         ",
              "  |         ",
              "  |         ", sep="\n"
              )
    elif errs == 2:
        print("   ______   ",
              "  /     |   ",
              "  |     |   ",
              "  |     O   ",
              "  |     |   ",
              "  |     |   ",
              "  |         ",
              "  |         ", sep="\n"
              )
    elif errs == 3:
        print("   ______   ",
              "  /     |   ",
              "  |     |   ",
              "  |     O   ",
              "  |     |   ",
              "  |     |   ",
              "  |    / \  ",
              "  |         ", sep="\n"
              )
    elif errs == 4:
        print("   ______   ",
              "  /     |   ",
              "  |     |   ",
              "  |     O   ",
              "  |    /|\  ",
              "  |     |   ",
              "  |    / \  ",
              "  |         ", sep="\n"
              )
    elif errs == 5:
        print("   ______   ",
              "  /     |   ",
              "  |     |   ",
              "  |     0   ",
              "  |    /|\  ",
              "  |     |   ",
              "  |    / \  ",
              "  |         ", sep="\n"
              )
    print("\n", "~"*20, "\n", sep="")


list_of_items = ["ARMSTRONG", "JETSTREAM SAM",
                 "SUNDOWNER", "MISTRAL", "MONSOON"]
wrong_letters = []

answer = list_of_items[random.randrange(0, len(list_of_items))]
question = removeConsonants(answer)

BeginGame()
print(f"{question}\n")
while True:
    if question == answer:
        win()
        break
    elif len(wrong_letters) == 5:
        lose()
        break
    letter = input("Enter Letter: ")
    check = gameCheck(question, answer, letter)
    if check == None:
        print("\nEnter a letter, man!\n")
        continue
    elif check == "W" or check == "L":
        break
    elif check[0]:
        question = check[1]
        printStatus(question, wrong_letters)
    else:
        wrong_letters += [letter.upper()]
        printStatus(question, wrong_letters)
