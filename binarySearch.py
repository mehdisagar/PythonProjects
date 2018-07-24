#time complexity O(log(n))
def binarySearch(input_list, value):
	low = 0
	high = len(input_list) - 1
	
	while low < high:
		mid = (low + high)/2
		if(input_list[mid] == value):
			return mid
		elif(input_list[mid] < value):
			low = mid - 1
		else:
			high = mid - 1
	return None
	
inList = [1,3,9,11,15,19,29]
val1 = 3
val2 = 0
print (binarySearch(inList, val1))
print (binarySearch(inList, val2))
