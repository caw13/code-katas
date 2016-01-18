import sort

class Rack:
	def __init__(self):
		self.elements = []
	
	def add(self,newBall):
		self.elements.append(newBall)
		self.elements = sort.mergeSort(self.elements)

rack = Rack()
while True:
	input_line = input("Enter input:\n")
	rack.add(input_line)
	print(rack.elements)
	
