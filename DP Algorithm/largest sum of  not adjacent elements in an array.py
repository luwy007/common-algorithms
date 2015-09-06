class Soultion:
	
	def largestSumOfArray(self,arr): 
		if(len(arr)==0):
			return None
		elif(len(arr)== 1):
			if(arr[0]>0):
				return arr[0]
			else:
				return 0
		elif(len(arr)==2):
			if(arr[0]>0 or arr[1]>0):
				if(arr[0]>arr[1]):
					return arr[0]
				else:
					return arr[1]
			else:
				return 0
		else:
			sum1 = 0
			sum2 = 0
			if(arr[0]>0):
				sum2 = arr[0]
			index = 0
			for num in arr[1:]:
				if(arr[index]>0):
					if(sum1+num>sum1):
						sum1 += num
						temp = sum1
						sum1 = sum2
						sum2 = temp
				else:
					if(num<0):
						continue
					if(sum1>sum2):
						sum2 = sum1
					else:
						sum1 = sum2
					sum1 += num
			if(sum1>sum2):
				return sum1
			else:
				return sum2


