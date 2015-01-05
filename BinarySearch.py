def BinarySearch(a,b):
  if not b:
    return -1
  maxIndex = len(b)
  while(maxIndex > 0 ):
    middleIndex = maxIndex/2
    if(a == b[middleIndex]):
      return middleIndex
    middleIndex =((maxIndex -middleIndex) /2)+middleIndex 
    if(a == b[middleIndex]):
      return middleIndex
    maxIndex = middleIndex
  return -1
