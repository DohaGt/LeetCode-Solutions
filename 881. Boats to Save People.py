class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        result=0
        l,r=0,len(people)-1
        while l<=r:
            remainder=limit-people[r]
            r-=1
            result+=1
            if l<=r and remainder>=people[l]:
                l+=1
        return result
