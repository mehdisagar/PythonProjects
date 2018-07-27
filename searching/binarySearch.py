#time complexity O(log(n))
def binarySearch(input_list, value):
	low = 0
	high = len(input_list) - 1
	
	while low < high:
		mid = (low + high)/2
		if(input_list[mid] == value):
			return mid
		elif(input_list[mid] < value):
			low = mid + 1
		else:
			high = mid - 1
	return None

def recursive_binarySearch(input_list, value):

	if len(input_list) == 0:
		return False

	else:
		mid = len(input_list)/2
		if input_list[mid] == value:
			return True

		else:
			if input_list[mid] < value:
				return recursive_binarySearch(input_list[mid + 1:], value)
			else:
				return recursive_binarySearch(input_list[:mid],value)
	
if __name__  == "__main__":
	inList = [1,3,9,11,15,19,29]
	val1 = 11
	val2 = 0
	print (binarySearch(inList, val1))
	print (recursive_binarySearch(inList, val2))
