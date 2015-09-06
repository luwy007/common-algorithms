class Solution:
	#dp[i][j] represents the cost that changing from str1[:i-1] to str2[:j-1] needs
	
	def findLCSseq(self,str1,str2):
		dp = []
