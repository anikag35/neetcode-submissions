class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #key here is that its sorted
        slowIndex = 0
        fastIndex = len(numbers) - 1
        slow = numbers[slowIndex]
        fast = numbers[fastIndex]
        while (slow < fast):
            if slow + fast == target:
                return [slowIndex+1, fastIndex+1]
            if slow + fast < target:
                slowIndex += 1
                slow = numbers[slowIndex]
            else:
                fastIndex -= 1
                fast = numbers[fastIndex]
        
