import math # get math for flooring in the sort method
# the two lists we are supposed to check for the majority elements
arr1 = [1,2,3,4,5,5,5,5,5,5,6]
arr2 = [1,2,3,4,3,3,2,4,5,6,1,2,3,4,6,1,2,3,4,6,6]

def findMajorityByDict(arr): 											# finding majority func
	newArr = arr[:]																	# create a copy of arr
	arrDict = {}																		# create the dict
	arrLen = len(newArr)														# get len of array for later use
	while newArr:																		# while we've stuff to do
		currEl = newArr.pop()													# get first el of list
		if str(currEl) in arrDict:										# if element has been counted before
			arrDict[str(currEl)] += 1										# increase element count
		else:																					# and if not
			arrDict[str(currEl)] = 1										# then set it to one
	for i in arrDict:																# find the one with highest value
		if arrDict[i] > arrLen/2:											# find it
			return print(i, "is the majority element")	# ayy we got it
	print("there is no majority element")						# if we dont have it, say so!!

def findMajorityBySort(arr):
	# this is a method shown in the presentation files, which is why ive chosen to
	# write code for it here; it works well with little code footprint if a list does
	# have a majority element - but if it doesn't, it still picks one! a wrong one!
	# the dict assigning method above does not do that and is therefore superior :)
	# we should only use it if we are certain there IS a majority element
	arr.sort()																			# sort the array
	print(arr[math.floor(len(arr)/2)])							# get the entry from the middle


# what we call the "driver code"
if __name__ == "__main__":							# only runs the content if this file is
	print("OF THE FIRST ARRAY BY DICT:")	# being run as opposed to being imported
	findMajorityByDict(arr1)
	print("OF THE SECOND ARRAY BY DICT:")
	findMajorityByDict(arr2)
	print("OF THE FIRST ARRAY BY SORT:")
	findMajorityBySort(arr1)
	print("OF THE SECOND ARRAY BY SORT:")
	findMajorityBySort(arr2) # will be false, since arr2 doesnt have a majority element