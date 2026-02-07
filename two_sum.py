"""
Two Sum Problem
Given an array of integers nums and an integer target, return the indices of the two numbers 
that add up to target.

You may assume each input has exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]
"""

def two_sum(nums, target):
    """
    Approach: Hash Map (Two-pass)
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Create a dictionary to store value -> index mapping
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_map:
            return [num_map[complement], i]
        
        num_map[num] = i
    
    return []  # No solution found


def two_sum_brute_force(nums, target):
    """
    Approach: Brute Force (Two nested loops)
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return []


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    
    for nums, target, expected in test_cases:
        result = two_sum(nums, target)
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Status: {'✓ PASS' if result == expected else '✗ FAIL'}")
        print()
