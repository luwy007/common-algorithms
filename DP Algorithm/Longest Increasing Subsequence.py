class Solution():
	def findLongestIncreasingSubsequence(self,arr):
		dp = []
		dp.append(1)
		for index in range(1,len(arr)): 
			largest = 1
			for index2,aheadNum in enumerate(arr[:index]):
				if(aheadNum<arr[index] and largest<dp[index2]+1):
					largest = dp[index2]+1
			dp.append(largest)

		largest = 1
		largest_index = 0 
		for index,item in enumerate(dp):
			if(largest<item):
				largest = item
				largest_index = index

		result = [arr[largest_index]]
		largest_index -= 1
		while(largest_index>=0):
			if(dp[largest_index]==largest-1):
				result = [arr[largest_index]]+result
				largest -= 1
			largest_index -= 1
		return result

	def ProFindLIS(self,arr):
		#this func can solve the problem with O(NlogN)
		pass

if __name__=="__main__":
	tests = [[1,2,3,4,5,6,5,4,3,2,1],[1,3,4,2,3,5,2,1,6,3,8]]
	for test in tests:
		res = Solution().findLongestIncreasingSubsequence(test)
		print(res)












