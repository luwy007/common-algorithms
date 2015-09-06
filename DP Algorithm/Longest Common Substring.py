class Solution:
	#dp[i][j] represents the length of the longest substring of str1[:i] anb str2[:j]
	#dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]+1(if(str1[i],str2[j])))
	# the function can be realized with common DP algorithm, 
	# it can be also solved within time complexity O(M*N),
	# and space complexity O(1) 
	def findLCSstr(self,str1,str2):
		pass