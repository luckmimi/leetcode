class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x:(-x[0],x[1]))
        res = []
        print(people)
        for p in people:
            res.insert(p[1],p)
            print(res)
        return res
