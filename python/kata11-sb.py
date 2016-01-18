class Rack:
	def __init__(self):
		self.elements = []

	def merge(self, leftPart, rightPart):
		lIndex = rIndex = 0
		mergedArray = []
		while (lIndex < len(leftPart)) and (rIndex < len(rightPart)):
			if leftPart[lIndex] < rightPart[rIndex]:
				mergedArray.append(leftPart[lIndex])
				lIndex+=1
			else:
				mergedArray.append(rightPart[rIndex])
				rIndex+=1
		if lIndex < len(leftPart):	
			for item in leftPart[lIndex:]:
				mergedArray.append(item)
		if rIndex < len(rightPart):
			for item in rightPart[rIndex:]:
				mergedArray.append(item)
		return mergedArray
	
	def mergeSort(self,passedArray):
		if len(passedArray) <= 1:
			return passedArray
		elif len(passedArray) == 2:
			if passedArray[0] <= passedArray[1]:
				return passedArray
			else:
				return [passedArray[1],passedArray[0]]
		else:
			midpoint = len(passedArray) // 2
			left = self.mergeSort(passedArray[0:midpoint])
			right = self.mergeSort(passedArray[midpoint:])
			return self.merge(left,right)
	
	def add(self,newBall):
		self.elements.append(newBall)
		self.elements = self.mergeSort(self.elements)

rack = Rack()
while True:
	input_line = input("Enter input:\n")
	rack.add(input_line)
	print(rack.elements)
	
