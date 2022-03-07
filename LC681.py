class Solution:
    def nextClosestTime(self, time: str) -> str:
        hour, minute = time.split(':')
        nums = sorted(set(hour+minute))
        choices = [a+b for a in nums for b in nums]
        # print(choices)
        pos = choices.index(minute)
        if pos + 1 < len(choices) and choices[pos+1] < '60':
            return hour + ":"+ choices[pos+1]
        pos = choices.index(hour)
        if pos + 1 < len(choices) and choices[pos+1] < '24':
            return choices[pos+1] + ':' + choices[0]
        
        return choices[0] + ':' + choices[0]
