import sort

class Rack:
	def __init__(self):
		self.elements = []
	
	def add(self,newElem):
		self.elements.append(newElem)
		self.elements = sort.mergeSort(self.elements)

	def print(self):
		result = ""
		for letter in self.elements:
			result += str(letter)
		print(result)

rack = Rack()
while True:
	input_line = input("Enter input:\n")
	input_line = input_line.lower()
	input_line = list(input_line)
	for letter in input_line:
		rack.add(letter)
	rack.print()
	
