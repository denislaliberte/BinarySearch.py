def BinarySearch(a,b):
  if not b:
    return -1
  maxIndex = len(b)
  minIndex = 0
  while(maxIndex > minIndex):
    middleIndex = (minIndex + maxIndex) /2
    if(a == b[middleIndex]):
      return middleIndex
    if(a > b[middleIndex]):
      minIndex = middleIndex
    else:
      maxIndex = middleIndex
  return -1
