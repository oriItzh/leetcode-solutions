def find_max_subarray_sum(nums: list[int]):
    """
    Find the maximum subarray sum using Kadane's algorithm.

    Args:
        nums (List[int]): List of integers.

    Returns:
        int: Maximum subarray sum.
    """
    max_sum = (
        nums[0] if not nums else float("-inf")
    )  # Initialize to negative infinity to handle all negative numbers
    current_sum = 0  # Start with the first element or 0 if the list is empty
    for num in nums:
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)

    return max_sum


def find_max_subarray_sum_with_indices(nums: list[int]):
    """
    Find the maximum subarray sum using Kadane's algorithm and return the start and end indices.

    Args:
        nums (List[int]): List of integers.

    Returns:
        Tuple[int, int, int]: Maximum subarray sum, start index, end index.
    """
    max_sum = float(
        "-inf"
    )  # Initialize to negative infinity to handle all negative numbers
    current_sum = 0  # Start with the first element or 0 if the list is empty
    start = 0
    max_start = max_end = 0
    for end in range(len(nums)):
        if current_sum < 0:
            start = end
            current_sum = 0
        current_sum += nums[end]
        if current_sum > max_sum:
            max_start, max_end = start, end
            max_sum = current_sum

    return max_sum, max_start, max_end
