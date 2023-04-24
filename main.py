import sudoku_constraints as sudoku
from collections import deque
import csps 
import copy



def main():
    #csp4 = make_csp_for_4()
    #ac_3(csp4)
    #backtraking_search(csp4)
    csp9 = make_csp_for_9()

    custom = [['C11',7],['C12',0],['C13',0],['C14',4],['C15',0],['C16',0],['C17',0],['C18',8],['C19',6],
              ['C21',0],['C22',5],['C23',1],['C24',0],['C25',8],['C26',0],['C27',4],['C28',0],['C29',0],
              ['C31',0],['C32',4],['C33',0],['C34',3],['C35',0],['C36',7],['C37',0],['C38',9],['C39',0],
              ['C41',3],['C42',0],['C43',9],['C44',0],['C45',0],['C46',6],['C47',1],['C48',0],['C49',0],
              ['C51',0],['C52',0],['C53',0],['C54',0],['C55',2],['C56',0],['C57',0],['C58',0],['C59',0],
              ['C61',0],['C62',0],['C63',4],['C64',9],['C65',0],['C66',0],['C67',7],['C68',0],['C69',8],
              ['C71',0],['C72',8],['C73',0],['C74',1],['C75',0],['C76',2],['C77',0],['C78',6],['C79',0],
              ['C81',0],['C82',0],['C83',6],['C84',0],['C85',5],['C86',0],['C87',9],['C88',1],['C89',0],
              ['C91',2],['C92',1],['C93',0],['C94',0],['C95',0],['C96',3],['C97',0],['C98',0],['C99',5]]

    for i in custom:
        if i[1] != 0:
            csp9.domain[i[0]] = [i[1]]
    backtraking_search(csp9)


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
    for i in sudoku.board: #initial the queue
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

def make_csp_for_9():
    variable = ['C11','C12','C13','C14','C15','C16','C17','C18','C19','C21','C22','C23','C24','C25','C26','C27','C28','C29',
                'C31','C32','C33','C34','C35','C36','C37','C38','C39','C41','C42','C43','C44','C45','C46','C47','C48','C49',
                'C51','C52','C53','C54','C55','C56','C57','C58','C59','C61','C62','C63','C64','C65','C66','C67','C68','C69',
                'C71','C72','C73','C74','C75','C76','C77','C78','C79','C81','C82','C83','C84','C85','C86','C87','C88','C89',
                'C91','C92','C93','C94','C95','C96','C97','C98','C99']
    domain = {"C11": [1,2,3,4,5,6,7,8,9],"C12": [1,2,3,4,5,6,7,8,9],"C13": [1,2,3,4,5,6,7,8,9],
              "C14": [1,2,3,4,5,6,7,8,9],"C15": [1,2,3,4,5,6,7,8,9],"C16": [1,2,3,4,5,6,7,8,9],
              "C17": [1,2,3,4,5,6,7,8,9],"C18": [1,2,3,4,5,6,7,8,9],"C19": [1,2,3,4,5,6,7,8,9],
              "C21": [1,2,3,4,5,6,7,8,9],"C22": [1,2,3,4,5,6,7,8,9],"C23": [1,2,3,4,5,6,7,8,9],
              "C24": [1,2,3,4,5,6,7,8,9],"C25": [1,2,3,4,5,6,7,8,9],"C26": [1,2,3,4,5,6,7,8,9],
              "C27": [1,2,3,4,5,6,7,8,9],"C28": [1,2,3,4,5,6,7,8,9],"C29": [1,2,3,4,5,6,7,8,9],
              "C31": [1,2,3,4,5,6,7,8,9],"C32": [1,2,3,4,5,6,7,8,9],"C33": [1,2,3,4,5,6,7,8,9],
              "C34": [1,2,3,4,5,6,7,8,9],"C35": [1,2,3,4,5,6,7,8,9],"C36": [1,2,3,4,5,6,7,8,9],
              "C37": [1,2,3,4,5,6,7,8,9],"C38": [1,2,3,4,5,6,7,8,9],"C39": [1,2,3,4,5,6,7,8,9],
              "C41": [1,2,3,4,5,6,7,8,9],"C42": [1,2,3,4,5,6,7,8,9],"C43": [1,2,3,4,5,6,7,8,9],
              "C44": [1,2,3,4,5,6,7,8,9],"C45": [1,2,3,4,5,6,7,8,9],"C46": [1,2,3,4,5,6,7,8,9],
              "C47": [1,2,3,4,5,6,7,8,9],"C48": [1,2,3,4,5,6,7,8,9],"C49": [1,2,3,4,5,6,7,8,9],
              "C51": [1,2,3,4,5,6,7,8,9],"C52": [1,2,3,4,5,6,7,8,9],"C53": [1,2,3,4,5,6,7,8,9],
              "C54": [1,2,3,4,5,6,7,8,9],"C55": [1,2,3,4,5,6,7,8,9],"C56": [1,2,3,4,5,6,7,8,9],
              "C57": [1,2,3,4,5,6,7,8,9],"C58": [1,2,3,4,5,6,7,8,9],"C59": [1,2,3,4,5,6,7,8,9],
              "C61": [1,2,3,4,5,6,7,8,9],"C62": [1,2,3,4,5,6,7,8,9],"C63": [1,2,3,4,5,6,7,8,9],
              "C64": [1,2,3,4,5,6,7,8,9],"C65": [1,2,3,4,5,6,7,8,9],"C66": [1,2,3,4,5,6,7,8,9],
              "C67": [1,2,3,4,5,6,7,8,9],"C68": [1,2,3,4,5,6,7,8,9],"C69": [1,2,3,4,5,6,7,8,9],
              "C71": [1,2,3,4,5,6,7,8,9],"C72": [1,2,3,4,5,6,7,8,9],"C73": [1,2,3,4,5,6,7,8,9],
              "C74": [1,2,3,4,5,6,7,8,9],"C75": [1,2,3,4,5,6,7,8,9],"C76": [1,2,3,4,5,6,7,8,9],
              "C77": [1,2,3,4,5,6,7,8,9],"C78": [1,2,3,4,5,6,7,8,9],"C79": [1,2,3,4,5,6,7,8,9],
              "C81": [1,2,3,4,5,6,7,8,9],"C82": [1,2,3,4,5,6,7,8,9],"C83": [1,2,3,4,5,6,7,8,9],
              "C84": [1,2,3,4,5,6,7,8,9],"C85": [1,2,3,4,5,6,7,8,9],"C86": [1,2,3,4,5,6,7,8,9],
              "C87": [1,2,3,4,5,6,7,8,9],"C88": [1,2,3,4,5,6,7,8,9],"C89": [1,2,3,4,5,6,7,8,9],
              "C91": [1,2,3,4,5,6,7,8,9],"C92": [1,2,3,4,5,6,7,8,9],"C93": [1,2,3,4,5,6,7,8,9],
              "C94": [1,2,3,4,5,6,7,8,9],"C95": [1,2,3,4,5,6,7,8,9],"C96": [1,2,3,4,5,6,7,8,9],
              "C97": [1,2,3,4,5,6,7,8,9],"C98": [1,2,3,4,5,6,7,8,9],"C99": [1,2,3,4,5,6,7,8,9],}
    
    csp9 = csps.csp(variable,domain,sudoku.board)
    return csp9

def minimum_remaining_values(csp,x1,x2):
    if len(csp.domain[x1]) > len(csp.domain[x2]):
        return x1
    else:
        return x2

def backtraking_search(csp):
    def backtraking(csp):
        if not unassign_array:
            print('FOUND IT')
            print(csp.domain)
            return True
        tem = unassign_array.pop(0)
        for i in csp.domain[tem]:
            newcsp = copy.deepcopy(csp)
            newcsp.domain[tem] = [i]
            if ac_3(newcsp):
                assign_array.append(tem)
                return backtraking(newcsp)
        unassign_array.append(tem)
        return False
        
    assign_array , unassign_array = findassign(csp.domain)
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