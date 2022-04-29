class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(segment):
            if segment[0] != '0' :
                return int(segment) <= 255
            return len(segment) == 1
        def update_output(curr_pos):
            segment = s[curr_pos + 1: n]
            if valid(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()
        def backtrack(prev_pos = -1, dots = 3):
            """
            prev_pos: the postion of the previously placed dot
            dots: number of dots to place
            """
            # the current dot curr_pos could be place
            # in a range from prev_pos + 1 to prev_pos + 4
            # the dot could not be placed
            # after the last character in the string
            for curr_pos in range(prev_pos + 1, min(n - 1, prev_pos + 4)):
                segment = s[prev_pos+ 1: curr_pos + 1]
                if valid(segment):
                    segments.append(segment)
                    if dots - 1 == 0:
                        update_output(curr_pos)
                    else:
                        backtrack(curr_pos,dots - 1)
                    segments.pop()
        n = len(s)
        output, segments = [], []
        backtrack()
        return output
        
        
        
