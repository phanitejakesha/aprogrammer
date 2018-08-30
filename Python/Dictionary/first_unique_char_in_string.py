# Nikhil Kumar Mengani
# First Unique Character in a String

'''
	Given a string, find the first non-repeating character in it and return it's index.
	If it doesn't exist, return -1.
	
	Example:
	s = "Nikhil"
    return 0.
	
'''

#solution_01
def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        mapper = Counter(s)
        for index, value in enumerate(s):
            num =  mapper[value]
            if num == 1:
                return index
        return -1    