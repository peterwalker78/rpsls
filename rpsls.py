#!/usr/bin/python

import random
import time

rock = 1
paper = 2
scissors = 3
lizard = 4
spock = 5

names = { rock: "Rock", paper: "Paper", scissors: "Scissors", lizard: "Lizard", spock: "Spock"}
rules = { rock: [scissors, lizard], paper: [rock, spock], scissors: [paper, lizard], lizard: [paper, spock], spock: [rock, scissors]}

player_score = 0
computer_score = 0

def start():
	print "Let's play a game of Rock, Paper, Scissors, Lizard, Spock"
	while game():
		pass
	scores()

def game():
	player = move()
	computer = random.randint(1, 5)
	result (player, computer)
	return play_again()

def move():
	while True:
		print
		player = raw_input("Rock     = 1\nPaper    = 2\nScissors = 3\nLizard   = 4\nSpock    = 5\nMake a move: ")
		try:
			player = int(player)
			if player in (1,2,3,4,5):
				return player
		except ValueError:
			pass
		print "Oops! I didn't understand that. Please enter 1, 2, 3, 4, or 5."

def result(player, computer):
	print "1..."
	time.sleep(0.5)
	print "2..."
	time.sleep(0.5)
	print "3!"
	time.sleep(0.25)
	print "Computer threw {0}!".format(names[computer])
	global player_score, computer_score
	if player == computer:
		print "Tie game."
	elif computer in rules[player]:
		print "Your victory has been assured."
		player_score += 1
	else:
		print "The computer laughs as you realise you have been defeated."
		computer_score += 1

def play_again():
	answer = raw_input("Would you like to play again? y/n: ")
	if answer in ("y", "Y", "yes", "Yes", "Of course!"):
		return answer
	else:
		print "Thank you very much for playing. See you next time!"

def scores():
	global player_score, computer_score
	print "HIGH SCORES"
	print "Player: ", player_score
	print "Computer: ", computer_score

if __name__ == '__main__':
	start()