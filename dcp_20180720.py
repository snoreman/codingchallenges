"""
Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers in the original
array except the one at i.

For example, if our input was [1, 2, 3, 4, 5],
the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def readInFromFile(fileName): #string file name
    with open(fileName) as dataFile:
        dataLine = dataFile.readline()
        arr = list(map(int, dataLine.strip().split(',')))
        return arr

dataArr = readInFromFile('dcp_20180720_data')
print(dataArr)
"""
#resultArr = [for x in dataArr: for y in dataArr: if dataArr.index(x) != dataArr.index(y)]
resultArr = []
i = 0
while i < len(dataArr):
    prod = 1
    j = 0
    while j < len(dataArr):
        if(i != j):
            prod *= dataArr[j]
            print(prod)
        j += 1
    resultArr.append(prod)
    i += 1

print (resultArr)
"""


def productExceptSelf(nums):
    p = 1
    n = len(nums)
    output = []
    for i in range(0,n):
        output.append(p)
        p = p * nums[i]
    p = 1
    for i in range(n-1,-1,-1):
        output[i] = output[i] * p
        p = p * nums[i]
    return output

print(productExceptSelf(dataArr))
