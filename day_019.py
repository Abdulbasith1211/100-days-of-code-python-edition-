# DAY 19  (STACK - PROBLEM SOLVING 2)



#PROBLEM : https://leetcode.com/problems/min-stack/


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []


    def push(self, x):
     
        self.stack.append(x)
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
            return
        if x <= self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            # Push top of min stack again
            self.min_stack.append(self.min_stack[-1])


    def pop(self):
        
        if len(self.stack) > 0:
        
            self.min_stack.pop()
            self.stack.pop()


    def top(self):
        
        if len(self.stack) > 0:
            return self.stack[-1]
        return None


    def getMin(self):
        
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        return None




#PROBLEM :  https://leetcode.com/problems/next-greater-element-i/



class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num=[-1]*len(nums1)
        for i in range(len(nums1)):
            for n in range(nums2.index(nums1[i]),len(nums2)):
                if nums2[n]>nums1[i]:
                    num[i]=nums2[n]
                    break
        return(num)



#RANDOM PROBLEM : https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret (self, s: str) -> str:
        d = {"(al)":"al","()":"o","G":"G"}
        tmp = ""
        res = ""
        for i in range (len(s)):
            tmp+=s[i]
            if(tmp in d):
                res+=d[tmp]
                tmp=""
                return res 

#RANDOM PROBLEM : https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths):
        source,destination=[],[]
        for a,b in paths:
                
	        source.append(a)
	        destination.append(b)
        for i in destination:
	        if i not in source:
		        return i



#PROBLEM : https://leetcode.com/problems/valid-parentheses


 class Solution:
     def isValid(self, s: str) -> bool:
        n =0
        while (len(s) != n): 
            n = len(s)
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
    
        if (len(s) == 0):
            return True
        else:
            return False

#PROBLEM : https://leetcode.com/problems/generate-parentheses
class Solution(object):
    def generateParenthesis(self, N):
        def helper(open_remain, close_remain, s):
            if open_remain==0 and close_remain==0:
                ans.append(s)
            if close_remain>open_remain and close_remain>0:
                helper(open_remain, close_remain-1, s+')')
            if open_remain>0:
                helper(open_remain-1, close_remain, s+'(')
        ans = []
        helper(N, N, '')
        return ans
      


#PROBLEM : https://leetcode.com/problems/validate-stack-sequences

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i=0
        while i<len(pushed):
            if not pushed:
                return True
            if pushed[i]==popped[0]:
                pushed.remove(pushed[i])
                popped.pop(0)
                if i!=0:
                    i=i-1
            else:
                i=i+1
        if pushed:
            return False
        else:
            return True
