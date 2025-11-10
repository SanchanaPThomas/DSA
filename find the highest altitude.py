class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m=0
        highest_altitude=0
        for i in gain:
            m+=i
            highest_altitude=max(highest_altitude,m)
        return highest_altitude
