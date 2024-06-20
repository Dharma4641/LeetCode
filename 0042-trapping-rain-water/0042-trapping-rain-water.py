class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        left_max=height[0]
        right_max=height[-1]
        c=0

        while left<right:
            if height[left]<height[right]:
                left+=1
                left_max=max(height[left],left_max)
                c+=left_max-height[left]
            else:
                right-=1
                right_max=max(height[right],right_max)
                c+=right_max-height[right]
        
        return c
        
        