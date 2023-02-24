'''
Poker hands

In the card game poker, a hand consists of five cards and are ranked,
from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then
the rank made up of the highest value wins;
for example,
a pair of eights beats a pair of fives (see example 1 below).
But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below);
if the highest cards tie then the next highest cards are compared,
and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
 	2C 3S 8S 8D TD
Pair of Eights
 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
 	2C 5C 7D 8S QH
Highest card Queen
 	Player 1
3	 	2D 9C AS AH AC
Three Aces
 	3D 6D 7D TD QD
Flush with Diamonds
 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
 	3C 3D 3S 9S 9D
Full House
with Three Threes
 	Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space):
the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid
(no invalid characters or repeated cards),
each player's hand is in no specific order,
and in each hand there is a clear winner.

How many hands does Player 1 win?
'''
from time import perf_counter as time
from urllib.request import urlopen
import re

cardic = {
'2':1,
'3':10,
'4':100,
'5':1000,
'6':10000,
'7':10**5,
'8':10**6,
'9':10**7,
'T':10**8,
'J':10**9,
'Q':10**10,
'K':10**11,
'A':10**12
}

st = re.compile(r'[^0]{5}')

def score(hand):
    score = 0
    hand = hand.split()
    H = str(sum(cardic[h[0]] for h in hand))
    lH = len(H)
    C = ''.join([h[1] for h in hand])
    straight = st.search(H)
    top = 10000000000
    if straight:
        if len(set(C))==1:
            if lH==13: return 10*top
            # 10 - Royal flush

            else: return 9*top+lH
            # 9  - Straight Flush

    invH = H[::-1]
    if '4' in H: return 8*top+invH.index('4')*100+invH.index('1')
    # 8 - Four of a kind

    three = '3' in H
    if three and '2' in H: return 7*top+invH.index('3')*100+invH.index('2')
    # 7 - Full House

    if len(set(C))==1: return 6*top+sum([n*100**j for j,n in enumerate(sorted([i for i in range(lH)for _ in range(int(invH[i]))if invH[i]!='0']))])
    # 6 - Flush

    if straight: return 5*top+lH
    # 5  - Straight

    if three: return 4*top+invH.index('3')*10000+sum([n*100**j for j,n in enumerate(sorted([i for i in range(lH)if invH[i]=='1']))])
    # 4 - three of a kind

    if '2' in H:
        if len(H.replace('2',''))==len(H)-2: return 3*top+sum([n*100**j for j,n in enumerate(sorted([i for i in range(lH)if invH[i]=='2']))],1)+invH.index('1')
        # 3 - two pairs

        else: return 2*top+invH.index('2')*1000000+sum([n*100**j for j,n in enumerate(sorted([i for i in range(lH)if invH[i]=='1']))])
        # 2 - one pair

    else:
        return sum([n*100**j for j,n in enumerate(sorted([i for i in range(lH)if invH[i]=='1']))])
    # 1 - High card

url = "https://projecteuler.net/project/resources/p054_poker.txt"
file = str(urlopen(url).read())[2:-1].split(r'\n')[:-1]

t = time()
player1wins = 0
for game in file:
    hand1,hand2 = game[:14],game[15:]
    s1,s2 = score(hand1),score(hand2)
    if s1>s2:
        player1wins += 1
print(player1wins) # 376
print(time()-t)
