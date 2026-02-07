"""
Binary Search Problem
Given a sorted array of integers, search for a target value and return its index.
If the target is not found, return -1.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def binary_search(nums, target):
    """
    Iterative Binary Search
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Target not found


def binary_search_recursive(nums, target, left=0, right=None):
    """
    Recursive Binary Search
    """
    if right is None:
        right = len(nums) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    else:
        return binary_search_recursive(nums, target, left, mid - 1)


def binary_search_leftmost(nums, target):
    """
    Find the leftmost (first) occurrence of target
    """
    left, right = 0, len(nums) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            result = mid
            right = mid - 1  # Continue searching in left half
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def binary_search_rightmost(nums, target):
    """
    Find the rightmost (last) occurrence of target
    """
    left, right = 0, len(nums) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            result = mid
            left = mid + 1  # Continue searching in right half
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 3, 5, 7, 9], 5, 2),
        ([1, 3, 5, 7, 9], 1, 0),
        ([1, 3, 5, 7, 9], 9, 4),
        ([1, 3, 5, 7, 9], 4, -1),
        ([], 5, -1),
    ]
    
    for nums, target, expected in test_cases:
        result = binary_search(nums, target)
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Status: {'✓ PASS' if result == expected else '✗ FAIL'}")
        print()
