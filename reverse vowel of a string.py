class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        m=('aeiouAEIOU')
        s_list=list(s)
        while i<j:
            if s_list[i] in m and s_list[j] in m:
                s_list[i],s_list[j]=s_list[j],s_list[i]
                i+=1
                j-=1
            elif s_list[i] in m:
                j-=1
            elif s_list[j] in m:
                i+=1
            else:
                i+=1
                j-=1
        return "".join(s_list)
