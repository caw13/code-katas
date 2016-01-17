def test_chop(chopMethod):
  assert -1 == chopMethod(3, [])
  assert -1 == chopMethod(3, [1])
  assert 0 == chopMethod(1, [1])
  #
  assert 0 == chopMethod(1, [1, 3, 5])
  assert 1 == chopMethod(3, [1, 3, 5])
  assert 2 == chopMethod(5, [1, 3, 5])
  assert -1 == chopMethod(0, [1, 3, 5])
  assert -1 == chopMethod(2, [1, 3, 5])
  assert -1 == chopMethod(4, [1, 3, 5])
  assert -1 == chopMethod(6, [1, 3, 5])
  #
  assert 0 == chopMethod(1, [1, 3, 5, 7])
  assert 1 == chopMethod(3, [1, 3, 5, 7])
  assert 2 == chopMethod(5, [1, 3, 5, 7])
  assert 3 == chopMethod(7, [1, 3, 5, 7])
  assert -1 == chopMethod(0, [1, 3, 5, 7])
  assert -1 == chopMethod(2, [1, 3, 5, 7])
  assert -1 == chopMethod(4, [1, 3, 5, 7])
  assert -1 == chopMethod(6, [1, 3, 5, 7])
  assert -1 == chopMethod(8, [1, 3, 5, 7])

def chopLoop(searchVal,passedArray):
  start = 0
  end = len(passedArray)
  while (end-start) > 0:
    midpoint = ((end - start) // 2)+start
    if searchVal == passedArray[midpoint]:
      return midpoint
    elif searchVal < passedArray[midpoint]:
      end = midpoint
    else:
      start = midpoint + 1
  return -1
  
def chopRecursion(searchVal,passedArray, start=0,end=-2):
  if end == -2:   # optional argument not provided
    end = len(passedArray)
  if (end-start) == 0:
    return -1
  midpoint = ((end - start) // 2)+start
  if searchVal == passedArray[midpoint]:
    return midpoint
  elif searchVal < passedArray[midpoint]:
    return chopRecursion(searchVal,passedArray,start,midpoint)
  else:
    return chopRecursion(searchVal,passedArray,midpoint + 1,end)
  return -1
  
def chopSlice(searchVal,passedArray):
  if len(passedArray) == 0:
    return -1
  midpoint = len(passedArray) // 2
  if searchVal == passedArray[midpoint]:
    return midpoint
  elif searchVal < passedArray[midpoint]:
    return chopSlice(searchVal,passedArray[0:midpoint])
  else:
    result = chopSlice(searchVal,passedArray[midpoint+1:])
    if result > -1:
      return (result + midpoint + 1)
    else:
      return -1
	
	
test_chop(chopLoop)
print("chopLoop passed")
test_chop(chopRecursion)
print("chopRecursion passed")
test_chop(chopSlice)
print("chopSlice passed")

#   print("start: "+str(start)+" end: "+str(end)+" midpoint: "+str(midpoint))