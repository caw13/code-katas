import re

# Part 1
f = open('../weather.dat','r')
lowestFound = 9999
foundDay = -1
for line in f:
	searchObj = re.search(r' +([0-9]+) +([0-9]+) +([0-9]+) .*',line)
	if searchObj:
		max = float(searchObj.group(2))
		min = float(searchObj.group(3))
		spread = max - min
		if lowestFound > spread:
			lowestFound = spread
			foundDay = searchObj.group(1)
print("Part 1: Lowest day: "+foundDay)

# Part 2
f = open('../football.dat','r')
lowestFound = 9999
foundTeam = "Error none found"
line = f.readline
for line in f:
	searchObj = re.search(r'.+ ([A-Za-z_]+) .+ ([0-9]+) +- +([0-9]+) .*',line)
	if searchObj:
		pointsFor = int(searchObj.group(2))
		pointsAgainst = int(searchObj.group(3))
		if lowestFound > abs(pointsFor - pointsAgainst):
			lowestFound = abs(pointsFor - pointsAgainst)
			foundTeam = searchObj.group(1)
print("Part 2 lowest difference is team: "+foundTeam)

# Part 3
def findLowest(filename,expression,invalidNum=9999):
	f = open(filename,'r')
	lowestFound = invalidNum
	foundItem = "Error none found"
	line = f.readline
	for line in f:
		searchObj = re.search(expression,line)
		if searchObj:
			firstNum = float(searchObj.group(2))
			secondNum = float(searchObj.group(3))
			if lowestFound > abs(firstNum - secondNum):
				lowestFound = abs(firstNum - secondNum)
				foundItem = searchObj.group(1)
	return foundItem

# Redo part1	
filename1 = '../weather.dat'
pattern1 = ' +([0-9]+) +([0-9]+) +([0-9]+) .*'
print("Part 1 redo: "+findLowest(filename1,pattern1))	
	
# Redo part2	
filename2 = '../football.dat'
pattern2 = '.+ ([A-Za-z_]+) .+ ([0-9]+) +- +([0-9]+) .*'
print("Part 2 redo: "+findLowest(filename2,pattern2))

			