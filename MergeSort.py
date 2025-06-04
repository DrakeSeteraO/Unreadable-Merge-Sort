from math import log2, ceil


def MergeSort(lst: list) -> list:
    length = len(lst)
    temp = [0] * length
    for i in range(ceil(log2(length))):
        size = 2 ** i; complete, p1, p2, p3 = False, 0, size, 0; cur = 1
        shift = lambda p1, p2, p3, lst, cur, size, bottom, cond, expression: [[lst[bottom:expression]], [cur * size * 2, size * (cur * 2 + 1), cur * 2 * size, cur + 1]] if cond % size == 0 else [[temp[p3:cur * size * 2]], [p1, p2, p3, cur]]
        

        while not complete:
            if p1 >= length:
                complete = True
            elif p2 >= length:
                complete, temp[p3:] = True, lst[p1:((cur-1) * size * 2 + size) * (size * ((cur-1) * 2 + 1) <= length) + length * (size * ((cur-1) * 2 + 1) > length)]
            else:
                if lst[p1] <= lst[p2]: 
                    temp[p3], p1, p3 = lst[p1], p1 + 1, p3 + 1; [[temp[p3:cur * size * 2]],[p1, p2, p3, cur]] = shift(p1, p2, p3, lst, cur, size, p2, p1, 2 * cur * size)    
                    
                else: 
                    temp[p3], p2, p3 = lst[p2], p2 + 1, p3 + 1; [[temp[p3:cur * size * 2]],[p1, p2, p3, cur]] = shift(p1, p2, p3, lst, cur, size, p1, p2, size * (2 * cur -1))
            
                        
        lst = temp.copy()
    return lst


lst = [81,2,7,1,0, -1, 5,-5]
print(MergeSort(lst))