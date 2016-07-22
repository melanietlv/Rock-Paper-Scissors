print "Hi, I'm Melanie the computer. Let's play a games of Rock-Paper-Scissors!\nMake your move (r, p, s)" 
from random import choice
m = 0
y = 0 

def choice2(move, m, y):
	x = choice("rps")
	if move == "r" and x == "r":
		print "I play rock."
		print "We tied!"
		return m, y
	elif move == "r" and x == "s":
		print "I play scissors."
		print "You win!"
		return m, y+1
	elif move == "r" and x == "p":
		print "I play paper."
		print "I win!"
		return m+1, y
	if move == "p" and x == "p":
		print "I play paper."
		print "We tied!"
		return m+1, y
	elif move == "p" and x == "s":
		print "I play scissors."
		print "I win!"
		return m + 1, y
	elif move == "p" and x == "r":
		print "I play rock."
		print "You win!"
		return m, y+1
	if move == "s" and x == "s":
		print "I play scissors."
		print "We tied!"
		return m, y
	elif move == "s" and x == "p":
		print "I play paper."
		print "You win!"
		return m, y+1
	elif move == "s" and x == "r":
		print "I play rock."
		print "I win!"
		return m+1, y

m = 0
y = 0


move = raw_input("Make your move: or q to quit: ")
while move != "q":
	m, y = choice2(move, m, y)
	print m, y
	
	move = raw_input("Make your move: or q to quit: ")
	
print "Final score is Melanie: %d, You: %d" % (m, y)























