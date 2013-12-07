import math
import string

class RectangularGrid:
    def countRectangles(self, width, height):
        counter = 0
        for i in range(1,width+1):
            for j in range(1,height+1):
                if i != j:
                    counter += ( (1+ (width-i)) * (( 1 + (height- j))) )
        return counter

# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pfx 2.1.9
import sys
import time
def KawigiEdit_RunTest(testNum, p0, p1, hasAnswer, p2):
	sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str(p0) + str(",") + str(p1))
	print(str("]"))
	obj = RectangularGrid()
	startTime = time.clock()
	answer = obj.countRectangles(p0, p1)
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
p0 = 3
p1 = 3
p2 = 22
all_right = KawigiEdit_RunTest(0, p0, p1, True, p2) and all_right
# ------------------

# ----- test 1 -----
p0 = 5
p1 = 2
p2 = 31
all_right = KawigiEdit_RunTest(1, p0, p1, True, p2) and all_right
# ------------------

# ----- test 2 -----
p0 = 10
p1 = 10
p2 = 2640
all_right = KawigiEdit_RunTest(2, p0, p1, True, p2) and all_right
# ------------------

# ----- test 3 -----
p0 = 1
p1 = 1
p2 = 0
all_right = KawigiEdit_RunTest(3, p0, p1, True, p2) and all_right
# ------------------

# ----- test 4 -----
p0 = 592
p1 = 964
p2 = 81508708664
all_right = KawigiEdit_RunTest(4, p0, p1, True, p2) and all_right
# ------------------

if (all_right):
	print(str("You're a stud (at least on the example cases)!"))
else:
	print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
# Given the width and height of a rectangular grid, return the total number of rectangles (NOT counting squares) that can be found on this grid.
# For example, width = 3, height = 3 (see diagram below):
# 
#  __ __ __
# |__|__|__|
# |__|__|__|
# |__|__|__|
# 
# In this grid, there are 4 2x3 rectangles, 6 1x3 rectangles and 12 1x2 rectangles. Thus there is a total of 4 + 6 + 12 = 22 rectangles. Note we don't count 1x1, 2x2 and 3x3 rectangles because they are squares.
# 
# 
# DEFINITION
# Class:RectangularGrid
# Method:countRectangles
# Parameters:integer, integer
# Returns:long integer
# Method signature:def countRectangles(self, width, height):
# 
# 
# NOTES
# -rectangles with equals sides (squares) should not be counted.
# 
# 
# CONSTRAINTS
# -width and height will be between 1 and 1000 inclusive.
# 
# 
# EXAMPLES
# 
# 0)
# 3
# 3
# 
# Returns: 22
# 
# See above
# 
# 1)
# 5
# 2
# 
# Returns: 31
# 
# 
#  __ __ __ __ __
# |__|__|__|__|__|
# |__|__|__|__|__|
# 
# In this grid, there is one 2x5 rectangle, 2 2x4 rectangles, 2 1x5 rectangles, 3 2x3 rectangles, 4 1x4 rectangles, 6 1x3 rectangles and 13 1x2 rectangles. Thus there is a total of 1 + 2 + 2 + 3 + 4 + 6 + 13 = 31 rectangles.
# 
# 2)
# 10
# 10
# 
# Returns: 2640
# 
# 3)
# 1
# 1
# 
# Returns: 0
# 
# 4)
# 592
# 964
# 
# Returns: 81508708664
# 
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pfx 2.1.9!
