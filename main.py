import sudoku_constraints as sudoku
from collections import deque
import csps 



def main():
    csp4 = make_csp_for_4()
    #revise(make_csp_for_4(),'C12','C11')
    ac_3(csp4)
    backtraking_search(csp4)

def revise(csp,x1,x2):
    revise = False
    res = False
    domain1 = csp.domain[x1]
    domain2 = csp.domain[x2]
    for i in domain1:
        for j in domain2:
            if i != j:
                res = True
                break
        if res:
            res = False
        else:
            domain1.remove(i)
            revise = True
    csp.domain[x1] = domain1
    return revise

def ac_3(csp):
    checkboard = []
    queue = deque()
    queue_view = set()
    for i in sudoku.board_4: #initial the queue
        queue.append([i[0],i[1]])
        queue_view.add(i[0]+i[1])
        queue.append([i[1],i[0]])
        queue_view.add(i[1]+i[0])
        checkboard.append([i[0],i[1]])
        checkboard.append([i[1],i[0]])
    while queue:
        tem = queue.popleft()
        queue_view.discard(tem[0]+tem[1])
        if revise(csp,tem[0],tem[1]):
            for i in checkboard:
                if i[1] == tem[0]:
                    istr = i[0]+i[1] 
                    if istr not in queue_view:
                        queue.append(i)
                        queue_view.add(istr)
    if not check(csp):
        return False
    return True
    
def make_csp_for_4():
    variable = ['C11','C12','C13','C14','C21','C22','C23','C24','C31','C32','C33','C34','C41','C42','C43','C44']
    domain = {"C11": [1], "C12": [1, 2, 3, 4], "C13": [1, 2, 3, 4], "C14": [1, 2, 3, 4],
               "C21": [1, 2, 3, 4], "C22": [2], "C23": [1, 2, 3, 4], "C24": [1, 2, 3, 4],
               "C31": [1, 2, 3, 4], "C32": [1, 2, 3, 4], "C33": [3], "C34": [1, 2, 3, 4],
               "C41": [1, 2, 3, 4], "C42": [1, 2, 3, 4], "C43": [1, 2, 3, 4], "C44": [4]}
    csp4 = csps.csp(variable,domain,sudoku.board_4)
    return csp4

def minimum_remaining_values(csp,x1,x2):
    if len(csp.domain[x1]) > len(csp.domain[x2]):
        return x1
    else:
        return x2

def backtraking_search(csp):
    def backtraking(csp):
        if not unassign_array:
            print('FOUND IT')
            return csp.domain
        tem = unassign_array.pop(0)
        print(tem)
        
    assign_array , unassign_array = findassign(csp.domain)
    print(unassign_array)
    backtraking(csp)

def findassign(domain):
    assign_array = []
    unassign_array = []
    for i in domain:
        if len(domain[i]) == 1:
            assign_array.append(i)
        else:
            unassign_array.append(i)
    return assign_array,unassign_array


def assigned(domain):
    for i in domain:
        if len(domain[i]) != 1:
            return False
    return True

def check(csp): #check is any val with not domain
    domain = csp.domain
    for i in domain:
        if len(domain[i]) == 0:
            print("no solution")
            return False
    return True

if __name__ == '__main__':
    main()