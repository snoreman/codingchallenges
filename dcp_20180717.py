"""
Daily Coding Problem #1 2018-07-17

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example: given [10, 15, 3, 7] and k of 17, return true since 10 + 7 = 17
Bonus: Can you do this in one pass?
"""

with open('dcp_20180717_data') as f:
	lis = list(map(int, f.readline().rstrip().split()))
	n = int(f.readline().rstrip())


print (lis, n)

def findSum(listOfValues, sumToFind):
		valuesToLookFor = []
		for value in listOfValues:
			difference = sumToFind - value
			valuesToLookFor.append(difference)
			print ("added %d" % (difference))
			if value in valuesToLookFor:
				print("does %d + %d = %d" % (value, difference, sumToFind))
				return True
		return False

print(findSum(lis, n))
