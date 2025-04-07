"""
BFS Approach -
TC - exponential -- since recursion
SC - recursive stack space - O(n) i.e n = length of string
Refer notes for details

BFS vs DFS --
Since BFS comparitively has lesser number of recursions than DFS, we give preference to BFS
"""
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if s is None or len(s) == 0: return []

        # declare DS
        q = deque()
        hset = set()

        rtnData = []

        q.append(s)
        hset.add(s)

        found = False

        def isValid(s):
            count = 0
            for i in range(len(s)):
                if s[i] == '(':
                    count += 1
                elif s[i] == ')':
                    count -= 1
                    # if a string starts with closing bracked OR
                    # if the count is -1 at any point, we do NOT continue
                    if count < 0: return False
            return count == 0

        while len(q) != 0 and not found:
            qsize = len(q)
            for i in range(qsize):
                # pop the left most string
                curr = q.popleft()
                if isValid(curr):
                    rtnData.append(curr)
                    found = True
                elif(found == False):
                    # remove one char from a string at a time and check if its valid
                    for j in range(len(curr)):
                        # if alphabets encountered, continue
                        if curr[j] >= 'a' and curr[j] <= 'z': continue
                        # create new baby string with one char removed till we find a valid string
                        baby = curr[0:j] + curr[j+1:]
                        # print(baby)
                        if baby not in hset:
                            hset.add(baby)
                            # print(hset)
                            q.append(baby)
        return rtnData