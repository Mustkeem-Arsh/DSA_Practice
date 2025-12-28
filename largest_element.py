# Given an array of integers nums, return the value of the largest element in the array
# Examples:
# Input: nums = [3, 3, 6, 1]
# Output: 6
# Explanation: The largest element in array is 6

# Input: nums = [3, 3, 0, 99, -40]
# Output: 99
# Explanation: The largest element in array is 99

def largestElement(nums):
        max = nums[0]
        for i in nums:
             if i > max:
                max = i
        return max

if __name__ == "__main__":
    l = [3, 3, 6,1]
    print(largestElement(l))

    # Correct implementation of the largestElement function
    
# def largestElement(nums):
#     if not nums:  # Handle empty array case
#         return None
#     max_element = nums[0]
#     for num in nums:
#         if num > max_element:
#             max_element = num
#     return max_element

# if __name__ == "__main__":
#     l = [3, 3, 6, 1]
#     print(largestElement(l))  # Output: 6
#     l = [3, 3, 0, 99, -40]
#     print(largestElement(l))  # Output: 99