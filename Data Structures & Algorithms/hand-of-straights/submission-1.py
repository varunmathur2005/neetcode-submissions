class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        hand.sort()
        for h in hand:
            if count[h] > 0:
                count[h] -= 1
                for i in range(1, groupSize):
                    next_h = h + i
                    if count[next_h] <= 0:
                        return False
                    count[next_h] -= 1
        
        return True