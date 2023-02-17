"""
Monopoly odds

In the game, Monopoly, the standard board is set up in the following way:

p084_monopoly_board.png
A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
Advance to GO
Go to JAIL
Chance (10/16 cards):
Advance to GO
Go to JAIL
Go to C1
Go to E3
Go to H2
Go to R1
Go to next R (railway company)
Go to next R
Go to next U (utility company)
Go back 3 squares.
The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final square that the player finishes at on each roll that we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
"""

from random import choice, shuffle

Monopoly = ["GO","A1","CC1","A2","T1","R1","B1","CH1","B2","B3","JAIL","C1","U1","C2","C3","R2","D1","CC2","D2","D3", # 19
			"FP","E1","CH2","E2","E3","R3","F1","F2","U2","F3","G2J","G1","G2","CC3","G3","R4","CH3","H1","T2","H2"]

community_Chest = [None]*14 + [0,10]
chance = [None]*6 + [0,10,11,24,39,5,"next_R","next_R","next_U","back_3"]

def play(dice,n):

	shuffle (community_Chest)
	shuffle(chance)
	count = {i:0 for i in range(40)}
	position = 0
	double = 0
	dice = range(1,dice+1)

	for i in range(n):
		count[position] += 1
		d1,d2 = choice(dice), choice(dice)
		if d1==d2: double += 1
		else: double = 0

		position = (position + d1+d2) % 40

		label = Monopoly[position]
		if double==3:
			position = 10
			double = 0
		elif label[:2] == 'CC':
			card = community_Chest.pop()
			if card!=None: position = card
			community_Chest.insert(0,card)
		elif label[:2] == 'CH':
			card = chance.pop()
			if card==None: pass
			elif isinstance(card,int):
				position = card
			elif card=='next_R':
				position = {7:15,22:25,36:5}[position]
			elif card=='nextU':
				potision = {7:12,22:28,36:12}[position]
			elif card=='back_3':
				position -= 3
			chance.insert(0,card)
		elif label=='G2J':
			position = 10

	print(count)
	stats = [(count[i]*100/n,f"{i:02d}") for i in range(40)]
	print(stats)
	r = '.'.join(e[1] for e in sorted(stats,reverse=True))

	return r

p = play(4,1000000)
print(p)

