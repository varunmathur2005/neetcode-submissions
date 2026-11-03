class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        hand.sort()
        for h in hand:
            if count[h]:
                for i in range(h, h + groupSize):
                    if count[i] <= 0:
                        return False
                    count[i] -= 1
        
        return True