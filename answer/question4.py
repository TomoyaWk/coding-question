def sliding_window_max(nums: list[int], k: int) -> list[int]:
    result = []

    for i in range(0, len(nums)):
        if i + k <= len(nums):
            print(nums[i : k + i])
            result.append(max(nums[i : k + i]))

    return result
