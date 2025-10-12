class Solution:
    def guessNumber(self, n: int) -> int:
        low,high=0,n
        while low<=high:
            mid=(low+high)//2
            res=guess(mid)
            if res==0:
                return mid
            elif res==-1:
                high=mid-1
            elif res==1:
                low=mid+1
