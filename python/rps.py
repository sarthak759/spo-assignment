from random import randint

t= ["Rock", "Paper", "Scissors"]

comp= t[randint(0,2)]

player= False

while player== False:
	player= input("Rock, Paper, Scissors\n")
	if player== comp :
		print("Tie")
	elif player== "Rock" :
		if comp== "Paper":
			print("You lose!", comp, "covers", player)
		else:
			print("You win!",player,"smashes", comp)
	elif player== "Paper":
		if comp=="Scissors":
			print("You lose!",comp,"cuts", player)
		else:
			print("You win!",player,"covers",comp)
	elif player== "Scissors":
		if comp== "rock":
			print("You lose!",comp,"smashes",player)
		else:
			print("You win!",player,"cuts",comp)
	else:
		print("invalid input, please check your spelling")

	player= False
	comp= t[randint(0,2)]