import random

options = ["rock", "fire", "scissors", "snake", "human", "tree", "wolf", "sponge", "paper", "air", "water", "dragon",
           "devil", "lightning", "gun"]
commands = ["!exit", "!rating"]


def new_list(name, lst):
    temp = lst.copy()
    for j in range(temp.index(name)):
        temp.append(temp[0])
        temp.pop(0)
    temp.remove(name)
    return temp


def convert_to_dict(lst):
    temp = []
    for line in lst:
        temp.append(line.replace("\n", "").split())
    return dict(temp)


my_file = open("rating.txt", "r")
list_names = my_file.readlines()
dict_names = convert_to_dict(list_names)
my_file.close()

user_name = input("Enter your name:")
print(f"Hello, {user_name}")
chosen_options = input().split(",")[::-1]
print("Okay, let's start")
if chosen_options == [""]:
    chosen_options = ["rock", "paper", "scissors"]
user_score = 0
if user_name in dict_names:
    user_score = int(dict_names[user_name])

while True:
    user_option = input()
    com_option = random.choice(chosen_options)
    if (user_option not in chosen_options) and (user_option not in commands):
        print("Invalid input")
    elif user_option == "!exit":
        print("Bye!")
        break
    elif user_option == "!rating":
        print(f"Your rating: {user_score}")
    elif user_option == com_option:
        user_score += 50
        print(f"There is a draw ({user_option})")
    else:
        sorted_options = new_list(user_option, options)
        winning = sorted_options[:7]
        print(winning)
        if com_option in winning:
            user_score += 100
            print(f"Well done. The computer chose {com_option} and failed")
        else:
            print(f"Sorry, but the computer chose {com_option}")