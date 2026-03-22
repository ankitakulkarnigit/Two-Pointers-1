// Time Complexity :
// Space Complexity :
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach

## Problem1 (https://leetcode.com/problems/sort-colors/)

## Problem2 (https://leetcode.com/problems/3sum/)
## Time Complexity : O(nlogn)
## Space Complexity : O(1)
# Hold one pivot pivot and then run 2sum

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        def twoSum(nums,pivot,res):
            hashset = set()
            i = pivot + 1
            while i < len(nums):
            	# a+b+c=0 --> c = -a-b -> a is the pivot, b is the current number and we are finding complement
                comp = -nums[pivot] - nums[i]
                if comp in hashset:
                    res.append([nums[pivot],nums[i],comp])
                    while i + 1 < len(nums) and nums[i] == nums[i+1]:
                        i += 1
                hashset.add(nums[i])
                i += 1
        
        res = []
        nums.sort()
        prev = float(inf)

        for pivot in range(0,len(nums)):
            if nums[pivot] > 0:
                break
            if pivot == 0 or nums[pivot-1] != nums[pivot]:
                twoSum(nums,pivot,res)
        return res


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