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
	
test_chop(chopLoop)
print("passed")