def BinarySearch(a,b):
  maxIndex = len(b)
  middleIndex = maxIndex/2
  if not b:
    return -1
  if(a == b[middleIndex]):
    return middleIndex
  middleIndex = middleIndex/2
  if(a == b[middleIndex]):
    return middleIndex
  middleIndex =((maxIndex -middleIndex) /2)+middleIndex 
  print middleIndex
  if(a == b[middleIndex]):
    return middleIndex
  return -1
