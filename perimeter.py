def count_incremovable_subarrays(nums):
  """
  Counts the total number of incremovable subarrays in a given array,
  considering single elements as strictly increasing.

  Args:
    nums: A 0-indexed array of positive integers.

  Returns:
    The total number of incremovable subarrays in the array.
  """

  deque, count = [], 0
  for i, num in enumerate(nums):
    while deque and nums[deque[-1]] >= num:  # Modified condition (>= instead of <=)
      deque.pop()
    deque.append(i)
    if i > 0:  # Subtract 1 for all iterations except the first
      count += len(deque)
    else:
      count += len(deque) + 1  # Count all possible subarrays in the first iteration
  return count


# Example usage
nums =  [6,5,7,8]
total_incremovable_subarrays = count_incremovable_subarrays(nums)
print(f"Total number of incremovable subarrays: {total_incremovable_subarrays}")
