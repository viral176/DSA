class Solution:
    def rotateArray(self, nums, k):
        n = len(nums)
        k = k % n  # To handle k > n
        # Rotate left by slicing and modifying in-place
        nums[:] = nums[k:] + nums[:k]
