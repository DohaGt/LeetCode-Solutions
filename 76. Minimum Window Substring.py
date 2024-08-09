class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        count, window={},{}
        for c in t:
            count[c]=1+count.get(c,0)
        x,y=0,len(count)
        result, resultL=[-1,1],float("infinity")
        l=0
        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)
            if c in count and window[c]==count[c]:
                x+=1
            while x==y:
                if(r-l+1<resultL):
                    result=[l,r]
                    resultL=r-l+1
                window[s[l]]-=1
                if s[l] in count and window[s[l]]<count[s[l]]:
                    x-=1
                l+=1
        l,r=result
        return s[l:r+1] if resultL!=float("infinity") else ""