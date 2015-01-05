def BinarySearch(a,b):
  middleIndex = len(b)/2
  if not b:
    return -1
  if(a == b[middleIndex]):
    return middleIndex
  return -1
