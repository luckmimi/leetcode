class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = collections.Counter(tasks)
        max_f = max(cnt.values())
        n_max = len([v for v in cnt.keys() if cnt[v] == max_f])
        return max(len(tasks),n_max + (max_f -1)*(n+1))
