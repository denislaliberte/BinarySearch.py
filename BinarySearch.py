def BinarySearch(a,b):
  if not b:
    return -1
  maxIndex = len(b)
  minIndex = 0
  middleIndex = maxIndex/2
  while(maxIndex > minIndex ):
    if(a == b[middleIndex]):
      return middleIndex
    if(a > b[middleIndex]):
      middleIndex =((maxIndex -middleIndex) /2)+middleIndex
    if(a == b[middleIndex]):
      return middleIndex
    maxIndex = middleIndex
    middleIndex = maxIndex/2
  return -1
