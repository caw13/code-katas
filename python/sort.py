def merge(leftPart, rightPart):
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
	
def mergeSort(passedArray):
	if len(passedArray) <= 1:
		return passedArray
	elif len(passedArray) == 2:
		if passedArray[0] <= passedArray[1]:
			return passedArray
		else:
			return [passedArray[1],passedArray[0]]
	else:
		midpoint = len(passedArray) // 2
		left = mergeSort(passedArray[0:midpoint])
		right = mergeSort(passedArray[midpoint:])
		return merge(left,right)