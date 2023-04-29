class Solution:

    
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            nums = [1, 2, 3, 1]
            if n in hashset:
                return True
            hashset.add(n)
        return False
