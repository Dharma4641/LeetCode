class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        max_=0
        chara=set()
        for right in range(len(s)):
            if s[right] not in chara:
                chara.add(s[right])
                max_=max(max_,right-left+1)
            else:
                while s[right] in chara:
                    chara.remove(s[left])
                    left+=1
                chara.add(s[right])
        return max_

