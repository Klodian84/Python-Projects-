"""
Given an array (list) nums consisted of only non-negative integers,
find the largest sum among all subarrays of length k in nums.
i.e.

in mums =[1,2,3,7,4,1], k = 3 , then the output should be 14.
"""

def subarray_sum_fixed(nums:list[int], k: int) -> int:
    window_sum = 0 # initiate a variable window_sum = 0
    for i in range (k):
        window_sum += nums[i] # save the sum of three first elements.
    largest = window_sum # currently this is the largest window sum.
    for right in range(k, len(nums)): # we move the window. Right will be in range that eliminates k first elements.
        left = right - k # index of the number that falls out of the window
        window_sum -= nums[left] # subtract the left number
        window_sum += nums[right] # add the right number
        largest = max(window_sum, largest) # this gives us the greatest value.
    return largest # return the greatest value.

print(subarray_sum_fixed([2,4,6,7,8,9,0,4,5,6], 3))

