from math import log2, ceil


def MergeSort(lst: list) -> list:
    temp = [0] * len(lst)
    for i in range(ceil(log2(len(lst)))):
        increment = lambda x, y: [x + 1, y + 1]; size = 2 ** i; complete, p1, p2, p3 = False, 0, size, 0; cur = 0

        while not complete:
            if p1 >= len(lst):
                complete = True
            elif p2 >= len(lst):
                complete = True
                while p3 < len(lst): temp[p3] = lst[p1]; p1, p3 = increment(p1, p3)
            else:
                if lst[p1] <= lst[p2]:
                    temp[p3] = lst[p1]; p1, p3 = increment(p1, p3)
                    if p1 % size == 0:
                        temp[p3:(cur+1) * size * 2] = lst[p2:2 * (cur) * size + (2 * size)]
                        p1, p2, p3 = (cur+1) * size * 2, (cur+1) * size * 2 + size, (cur+1) * 2 * size
                else:
                    temp[p3] = lst[p2]; p2, p3 = increment(p2, p3)
                    if p2 % size == 0:
                        temp[p3:(cur+1) * size * 2] = lst[p1:2 * (cur) * size + size]
                        p1, p2, p3 = (cur+1) * size * 2, (cur+1) * size * 2 + size, (cur+1) * 2 * size
            cur += 1
                        
        lst = temp.copy()
    return lst


lst = [4,2,7,1,0, -1, 5]
print(MergeSort(lst))                  