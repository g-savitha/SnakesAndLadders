import random

def die():
    while "d":
        key = input("Press 'd' to throw  the dice:  ")  
        if key == "d":
             die_val = random.randint(1,6)
             print("die value is",die_val)
             return die_val
        else:
            print("Enter the valid key")
            continue

def ladder(curposition,dieval):
    curposition += dieval
    ladder = [[5,46],[11,29],[22,61],[60,87],[72,96],[75,87]]
    for li in ladder:
        if curposition == li[0]:
            print("Yippee!! You have climbed the ladder")
            return li[1]
    return 0
    
def snake(curposition,dieval):
    curposition += dieval
    snake = [[12,6],[38,18],[80,44],[65,54],[92,48]]
    for li in snake:
        if curposition == li[0]:
            print("Ouchh!! You are bitten by a snake")
            return li[1]
    return 0

def dieConditions(count,dieval,currentpos,orgpos):
	while currentpos < 100:
		if dieval == 6 : # die value is six
			if count < 3 :
				if count == 1:
					currentpos += dieval
				dieval = die()
				count += 1
				currentpos += dieval
				if dieval == 6 and count == 3:
					return 1
				if dieval == 6 and count < 3 and currentpos <= 100:
					return dieConditions(count,dieval,currentpos,orgpos)
				elif dieval < 6 and currentpos <= 100:
					return currentpos
				elif currentpos > 100:
					return orgpos
			else:
				return 1
		else: #dieval is not six
			lad_val = ladder(currentpos,dieval)
			snak_val = snake(currentpos,dieval)
			if lad_val:#if you get a ladder
				return lad_val
			if snak_val:#if you get a snake
				return snak_val
			else:#if you dont get a snake or ladder
				return currentpos + dieval
	return orgpos#if your current position is greater than 100	

def players(players_names,numberOfPlayers):
    curpositions = []
    for i in players_names:
        curpositions.append(0)
    while max(curpositions) < 100:
        j = 0
        while j < numberOfPlayers:
            if max(curpositions) < 100:
                print(players_names[j].upper(),"Now it's your turn")
                curposition = curpositions[j]
                s = [95,96,97,98,99]
                a = [[5,4,3,2,1],[4,3,2,1],[3,2,1],[2,1],[1]]
                if curposition in s:
                    position = s.index(curposition)
                    die_val = die()
                    if die_val in a[position]:
                        curposition += die_val
                else:
                    dieval = die()
                    curposition = dieConditions(1,dieval,curposition,curposition)
                    lad_val = ladder(curposition,0)
                    snak_val = snake(curposition,0)
                    if lad_val:
                        curposition = lad_val
                    if snak_val:
                        curposition = snak_val                    
                curpositions[j] = curposition
                if curposition == 100:
                    print(players_names[j].upper(),"Congrats! You have won the game")
                    exit(0)
                print("your current position is",curposition)
                j += 1

players_names = []
print("SNAKES AND LADDERS is played between two or more players")
numberOfPlayers = int(input("Enter number of players: "))
for i in range(0,numberOfPlayers):
    print("enter name of player",i + 1)
    players_names.append(input())
print("press 'i' for instructions otherwise any other letter to start the game")
choice = input()
if choice == "i":
    message = """a. Each player takes a turn to roll a single die to move his/her position by the number of squares indicated by die roll.
    b. If on completion of a move, a player lands on lower-numbered end of a LADDER, the player moves upto the ladder's higher-numbered square.
    c. If the player lands on the higher-numbered square of a SNAKE, the player must move down to the snake's lowered-numbered square.
    d. If the player rolls a 6, the player may, after moving, immediately take another turn; otherwise play passes to the next player in
    turn.
    e. If a player roll three consecutive SIXES, the player must return to the starting square and continues.
    f. The player who is first to reach 100 is the winner."""
    print(message)
print("Now You can start the game")
print("ladders are from \n5 to 46\n11 to 29\n22 to 61\n60 to 68\n72 to 96\n75 to 87\n\nsnakes are from \n12 to 6\n38 to 18\n65 to 54\n80 to 44\n92 to 48")
players(players_names,numberOfPlayers)
