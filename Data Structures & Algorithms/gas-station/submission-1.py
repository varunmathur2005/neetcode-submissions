class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1

        for i in range(n):
            curGas = gas[i] - cost[i]
            goal = i
            j = (goal + 1) % n
            while curGas >= 0 and j % n != goal:
                curGas = curGas + gas[j] - cost[j]
                j = (j + 1) % n
            if j == goal:
                return goal

        return -1

