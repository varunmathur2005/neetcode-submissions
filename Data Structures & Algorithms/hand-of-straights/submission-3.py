class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for h in sorted(hand):
            if count[h] > 0:
                freq = count[h]
                for i in range(h, h + groupSize):
                    if count[i] < freq:
                        return False
                    count[i] -= freq
        
        return True