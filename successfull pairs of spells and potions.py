class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m=len(potions)
        res=[]
        for spell in spells:
            minPotion=math.ceil(success/spell)
            index=bisect_left(potions,minPotion)
            count=m-index
            res.append(count)
        return res
