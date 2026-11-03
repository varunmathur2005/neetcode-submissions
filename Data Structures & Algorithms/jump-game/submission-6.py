class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canReach = [False] * len(nums)
        canReach[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            max_jump = min(nums[i] + i + 1, len(nums))
            print(max_jump)
            for j in range(i, max_jump):
                print("reached")
                if canReach[j] == True:
                    canReach[i] = True
                    break
        print(canReach)
        return canReach[0]
            



