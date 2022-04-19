class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        l = [-1]
        flag = False
        for bi in board[::-1]:
            if flag:
                l += bi[::-1]
            else:
                l += bi
            flag = not flag
            #print(l)
        queue = [1]
        step = 0
        d = dict()
        while queue:
            new_queue = set()
            for qi in queue:
                if l[qi] != -1:
                    qi = l[qi]
                if qi not in d:
                    d[qi] = step
                    # make 1 to 6 move
                    for i in range(1, 7):
                        new_queue.add(min(qi+i, len(l)-1))
            step += 1
            queue = new_queue
        #print(d)
        if len(l)-1 in d:
            return d[len(l)-1]
        else:
            return -1