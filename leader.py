# the four lists we are supposed to check for the leader elements
arr1 = [12,9,7,14,8,6,3]
arr2 = [8,23,19,21,15,6,11]
arr3 = [55,67,71,57,51,63,38]
arr4 = [21,58,44,14,51,36,23]

def findLeader(arr):											# finding leader func
	leader = arr[-1]												# set leader to last el of array
	print(leader, "is a leader element")		# print it - it's a leader
	arr.pop()																# remove it from list
	
	while arr:															# long as we have elements to check
		sprawdzanko = arr[-1]									# get the next one (rightmost one)
		arr.pop()															# remove it from list
		if sprawdzanko > leader:							# if its a leader
			print(sprawdzanko, "is a leader")		# then its a leader
			leader = sprawdzanko								# smiles all around :)

# what we call the "driver code"
if __name__ == "__main__":			# only runs the content if this file is
	print("OF THE FIRST ARRAY:")	# being run as opposed to being imported
	findLeader(arr1)
	print("OF THE SECOND ARRAY:")
	findLeader(arr2)
	print("OF THE THIRD ARRAY:")
	findLeader(arr3)
	print("OF THE FOURTH ARRAY:")
	findLeader(arr4)