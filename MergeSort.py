from math import log2, ceil

def MergeSort(lst: list) -> list:
    temp = [0] * len(lst)
    for i in range(ceil(log2(len(lst)))):
        size = 2 ** i; complete, p1, p2, p3 = False, 0, size, 0

        while not complete:
            if p1 >= len(lst):
                complete = True
            elif p2 >= len(lst):
                complete = True
                while p3 < len(lst): temp[p3] = lst[p1]; p1, p3 = p1 + 1, p3 + 1
            else:
                if lst[p1] <= lst[p2]:
                    temp[p3] = lst[p1]; p1, p3 = p1 + 1, p3 + 1
                    if p1 % size == 0:
                        while p2 % (2 * size) != 0: temp[p3] = lst[p2]; p2, p3 = p2 + 1, p3 + 1 
                        p1, p2 = p1 + size, p2 + size
                else:
                    temp[p3] = lst[p2]; p2, p3 = p2 + 1, p3 + 1
                    if p2 % size == 0:
                        while p1 % (2 * size) != size: temp[p3] = lst[p1]; p1, p3 = p1 + 1, p3 + 1
                        p1, p2 = p1 + size, p2 + size
                        
        lst = temp.copy()
    return lst


lst = [4,2,3,1,0, -1]
print(MergeSort(lst))                  