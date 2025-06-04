from math import log2, ceil


def MergeSort(lst: list) -> list:
    length = len(lst)
    temp = [0] * length
    shift = lambda p1, p2, p3, lst, cur, size, bottom, cond, expression: [[lst[bottom:expression]], [cur * size * 2, size * (cur * 2 + 1), cur * 2 * size, cur + 1]] if (cond % size == 0) else [[temp[p3:cur * size * 2]], [p1, p2, p3, cur]]
    for i in range(ceil(log2(length))):
        size = 2 ** i; complete, p1, p2, p3 = False, 0, size, 0; cur = 1
        

        while not complete:
            if p1 >= length:
                complete = True
            elif p2 >= length:
                complete, temp[p3:] = True, lst[p1:((cur-1) * size * 2 + size) * (size * ((cur-1) * 2 + 1) <= length) + length * (size * ((cur-1) * 2 + 1) > length)]
            else:
                first = lst[p1] <= lst[p2]; [temp[p3], p1, p2] = [lst[p1],  p1 + 1, p2] if first else [lst[p2], p1, p2 + 1]; [[temp[p3+1:cur * size * 2]],[p1, p2, p3, cur]] = shift(p1, p2, p3 + 1, lst, cur, size, p2, p1, 2 * cur * size) if first else shift(p1, p2, p3 + 1, lst, cur, size, p1, p2, size * (2 * cur -1))   
            
                        
        lst = temp.copy()
    return lst


lst = [81,2,7,1,0, -1, 5,-5,-9]
print(MergeSort(lst))