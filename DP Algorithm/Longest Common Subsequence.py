class Solution:
	#dp[i][j] represents the length of the longest subsequence of str1[:i] anb str2[:j]
	#dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]+1(if(str1[i],str2[j])))
	def findLCSseq(self,str1,str2):
		dp = []
