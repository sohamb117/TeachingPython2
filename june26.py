import random
winCount = 0
tieCount = 0
loseCount = 0

computerChoice = ["Rock", "Paper", "Scissors"]

def play():
	global winCount, tieCount, loseCount
	win = False
	lose = False
	tie = False
	gameEnd = False
	computer = random.choice(computerChoice)
	player = input("Pick a choice of rock, paper, or scissors. Use lowercase.")
	print(computer)
	if computer == "Rock" and player == "rock":
		tie = True
		tieCount += 1
		gameEnd = True
		print("Computer chose", computer, "and player chose", player, "Tie!")
	elif computer == "Rock" and player == "paper":
		win = True
		winCount += 1
		gameEnd = True
		print("Computer chose", computer, "and player chose", player, "Player wins!")
	elif computer == "Rock" and player == "scissors":
		lose = True
		loseCount += 1
		gameEnd = True
		print("Computer chose", computer, "and player chose", player, "Computer wins!")
	elif computer == "Paper" and player == "paper":
		tie = True
		tieCount += 1
		gameEnd = True
		print("Computer chose", computer, "and player chose", player, "Tie!")
	elif computer == "Paper" and player == "Scissors":
		win = True
		winCount += 1
		gameEnd = True
		print("Computer chose", computer, "and player chose", player, "Player wins!")
	elif computer == "Paper" and player == "rock":
		lose = True
		loseCount += 1
		gameEnd = True
		print("Computer chose", computer, "and player chose", player, "Computer wins!")		
	elif computer == "Scissors" and player == "scissors":
		tie = True
		tieCount += 1
		gameEnd = True
		print("Computer chose", computer, "and player chose", player, "Tie!")
	elif computer == "Scissors" and player == "rock":
		win = True
		winCount += 1
		gameEnd = True
		print("Computer chose", computer, "and player chose", player, "Player wins!")
	elif computer == "Scissors" and player == "paper":
		lose = True
		loseCount += 1
		gameEnd = True
		print("Computer chose", computer, "and player chose", player, "Computer wins!")
	

while True:
	play()