#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

play_options = ["Rock", "Paper", "Scissors"]
player = False

def determine_winner(player, computer):
    if player == computer:
        print("Tie!")
    elif (player == "Rock" and computer == "Scissors") or (player == "Paper" and computer == "Rock") or (player == "Scissors" and computer == "Paper"):
        print("You win!", player, "beats", computer)
    else:
        print("You lose!", computer, "beats", player)

def re_start(option):
    re_start = input(option).lower()
    if re_start in ("y", "yes"):
        print("Let's play again!")
        return False
    else:
        print("Thanks for playing!")
        return exit()

while player == False:
    print("Choose your weapon!")
    player = input("Rock, Paper, Scissors? ").capitalize()
    computer = random.choice(play_options)

    if player in play_options:
        print("Player chose:", player)
        print("Computer chose:", computer)
        determine_winner(player, computer)
        player = re_start("Would you like to play again? (y/n) ")
    else:
        print("Not a valid option.")
        player = re_start("Would you really like to play? (y/n) ")