// Time Complexity :
// Space Complexity :
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach

## Problem1 (https://leetcode.com/problems/sort-colors/)

## Problem2 (https://leetcode.com/problems/3sum/)

## Problem3 (https://leetcode.com/problems/container-with-most-water/)
## Time Complexity : O(n)
## Space Complexity : O(1)
## Did this code successfully run on Leetcode : Yes

class Solution:
    def maxArea(self, height: List[int]) -> int:
        #brute force = nested for loop

        maxarea = 0
        i,j = 0,len(height)-1

        while i < j:
            area = min(height[i],height[j]) * abs(j-i)
            maxarea = max(area,maxarea)
            if height[i] <= height[j]:
                i += 1
            elif height[j] < height[i]:
                j -= 1

        return maxarea