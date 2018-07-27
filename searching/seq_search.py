# searching for an element in unordered array, T.C. O(n)<-- W.C.
def  seq_search(array, element):
	pose = 0
	hit = False
	while pose < len(array) and not hit:
		if array[pose] == element:
			hit = True

		else:
			pose += 1

	return hit


if __name__ == '__main__':
	arr = [1, 3, 5, -8, 40]
	print seq_search(arr, 41)
	print seq_search(arr, 5)