class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      seen_numbers = {}                          # empty dict
      for i in range(len(nums)):                 # walk by index
          complement = target - nums[i]          # what partner do I need?
          if complement in seen_numbers:         # have I seen that partner before?
              return [seen_numbers[complement], i]   # yes! return its index + my current index
          seen_numbers[nums[i]] = i              # no — record me, in case a future number needs me