def test_chop():
  assert -1 == chop(3, [])
  assert -1 == chop(3, [1])
  assert 0 == chop(1, [1])
  #
  assert 0 == chop(1, [1, 3, 5])
  assert 1 == chop(3, [1, 3, 5])
  assert 2 == chop(5, [1, 3, 5])
  assert -1 == chop(0, [1, 3, 5])
  assert -1 == chop(2, [1, 3, 5])
  assert -1 == chop(4, [1, 3, 5])
  assert -1 == chop(6, [1, 3, 5])
  #
  assert 0 == chop(1, [1, 3, 5, 7])
  assert 1 == chop(3, [1, 3, 5, 7])
  assert 2 == chop(5, [1, 3, 5, 7])
  assert 3 == chop(7, [1, 3, 5, 7])
  assert -1 == chop(0, [1, 3, 5, 7])
  assert -1 == chop(2, [1, 3, 5, 7])
  assert -1 == chop(4, [1, 3, 5, 7])
  assert -1 == chop(6, [1, 3, 5, 7])
  assert -1 == chop(8, [1, 3, 5, 7])

def chop(searchVal,passedArray):
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
	
test_chop()
print("passed")