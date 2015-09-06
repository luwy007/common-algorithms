class Solution:
	# arr is a sorted array, eg:[1,2,3]
	# if arr contains x, return the last place of x, or return -1
	def BinarySearch(self,arr,x):
		head = 0
		tail = len(arr) 
		found = False
		while(head<tail):
			mid = head+(tail-head)//2
			if(arr[mid]==x):
				head = mid
				while(head<tail):
					mid = head+(tail-head)//2
					if(arr[mid]==x):
						head = mid
					else:
						tail = mid-1
						if(arr[tail]==x):
							return tail-1 

			elif(arr[mid]>x):
				tail = mid-1
			else:
				head = mid+1
			pass
		return -1
