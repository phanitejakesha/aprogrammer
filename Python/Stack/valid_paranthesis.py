'''
    Program : To check given string is valid parathesis or not
    valid pairs are ( ), [ ], { }

'''



class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for brace in s:
            if brace == '(' or brace == '{' or brace == '[':
                stack.insert(0,brace)
            elif brace == ')':
                if len(stack)==0 or stack.pop(0) != '(':
                    return False
            elif brace == ']':
                if len(stack)==0 or stack.pop(0) != '[':
                    return False
            elif brace == '}':
                if len(stack)==0 or stack.pop(0) != '{':
                    return False
        if len(stack)!=0:
            return False
        return True
