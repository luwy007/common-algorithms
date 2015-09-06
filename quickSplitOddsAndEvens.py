class Solution:
	#仅用O(1)的空间，将整数数组按奇偶数分成2部
	#数组左边是奇数、右边是偶数。（要求：给出完整代码，尽量高效，简洁）
	def split(self, nums):
		if(len(nums)<=1):
			return 
		head = 0
		tail = len(nums)-1
		while(head<=tail):
			while(nums[head]%2==1 and head<tail):
				head += 1
			while(nums[tail]%2==0 and head<tail):
				tail -= 1
			if(head==tail):
				return
			else:
				temp = nums[head]
				nums[head] = nums[tail]
				nums[tail] = temp

if __name__=="__main__":
	tests = [[1,2,3,4,5,6,7],[2,4,6,1,3,5]]
	for test in tests:
		Solution().split(test)
		print(test)