class Solution(object):
    def reverseString(self, s):
        first = 0
        last = len(s) - 1
        while last > first:
            s[first], s[last] = s[last], s[first]
            first += 1
            last -= 1
