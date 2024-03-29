import math
import string

class StoneGame:
    def getScore(self, treasure, stones):
        scores = [0,0]
        turn = 1
        while sum(treasure) != 0:
            print(treasure)
            if 1 in stones:
                index = stones.index(1)
                scores[turn-1] += treasure[index]
                treasure[index] = 0
            else:
                index = self.get_index(stones)
            stones[index] -= 1
            turn = 3 - turn
        return scores[0]

    def get_index(self,stones):
        for i in range(len(stones)):
            if stones[i] != 2 and stones[i] != 0:
                return i
        else:
            return stones.index(2)

# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pfx 2.1.9
import sys
import time
def KawigiEdit_RunTest(testNum, p0, p1, hasAnswer, p2):
	sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("{"))
	for i in range(len(p0)):
		if (i > 0):
			sys.stdout.write(str(","))
		
		sys.stdout.write(str(p0[i]))
	
	sys.stdout.write(str("}") + str(",") + str("{"))
	for i in range(len(p1)):
		if (i > 0):
			sys.stdout.write(str(","))
		
		sys.stdout.write(str(p1[i]))
	
	sys.stdout.write(str("}"))
	print(str("]"))
	obj = StoneGame()
	startTime = time.clock()
	answer = obj.getScore(p0, p1)
	endTime = time.clock()
	res = True
	print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
	if (hasAnswer):
		print(str("Desired answer:"))
		print(str("\t") + str(p2))
	
	print(str("Your answer:"))
	print(str("\t") + str(answer))
	if (hasAnswer):
		res = answer == p2
	
	if (not res):
		print(str("DOESN'T MATCH!!!!"))
	elif ((endTime - startTime) >= 2):
		print(str("FAIL the timeout"))
		res = False
	elif (hasAnswer):
		print(str("Match :-)"))
	else:
		print(str("OK, but is it right?"))
	
	print(str(""))
	return res

all_right = True


# ----- test 0 -----
p0 = [3,2]
p1 = [1,2]
p2 = 5
all_right = KawigiEdit_RunTest(0, p0, p1, True, p2) and all_right
# ------------------

# ----- test 1 -----
p0 = [5,4,3,2,1]
p1 = [1,1,1,1,1]
p2 = 9
all_right = KawigiEdit_RunTest(1, p0, p1, True, p2) and all_right
# ------------------

# ----- test 2 -----
p0 = [5,5]
p1 = [2,2]
p2 = 0
all_right = KawigiEdit_RunTest(2, p0, p1, True, p2) and all_right
# ------------------

# ----- test 3 -----
p0 = [1]
p1 = [10]
p2 = 0
all_right = KawigiEdit_RunTest(3, p0, p1, True, p2) and all_right
# ------------------

if (all_right):
	print(str("You're a stud (at least on the example cases)!"))
else:
	print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
# You and your friend are playing a game.  There is a number of treasure chests hidden under piles of stones.  That is, the i-th chest has stones[i] stones piled on top of it.  You take turns taking exactly one stone from the top of one of the chests.  Whoever takes the last stone from the top of a chest takes the chest and the treasure inside.  The inside of the i-th chest is worth treasure[i].  The game objective is to gather as much treasure as possible.
# 
# Unfortunately, your friend is a cyborg and always makes the best possible move (maximizing his final win).  Given stones and treasure, return the maximum total amount you can get from the chests given that you move first.
# 
# DEFINITION
# Class:StoneGame
# Method:getScore
# Parameters:tuple (integer), tuple (integer)
# Returns:integer
# Method signature:def getScore(self, treasure, stones):
# 
# 
# CONSTRAINTS
# -stones will contain between 1 and 50 elements, inclusive.
# -stones and treasure will contain the same number of elements.
# -Each element of stones will be between 1 and 10^6, inclusive.
# -Each element of treasure will be between 1 and 10^6, inclusive.
# 
# 
# EXAMPLES
# 
# 0)
# {3,2}
# {1,2}
# 
# Returns: 5
# 
# In your first move you take the stone from the 0-th chest and take its treasure.  Then your friend must take a stone from the 1-st chest leaving you with one stone on the 1-st chest.  You take the last stone in your second move and take the contents of the 1-st chest.
# 
# 1)
# {5,4,3,2,1}
# {1,1,1,1,1}
# 
# Returns: 9
# 
# 
# 
# 2)
# {5,5}
# {2,2}
# 
# Returns: 0
# 
# 
# 
# 3)
# {1}
# {10}
# 
# Returns: 0
# 
# 
# 
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pfx 2.1.9!
