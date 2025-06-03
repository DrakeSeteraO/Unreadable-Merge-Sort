from math import log2, ceil


def MergeSort(lst: list) -> list:
    length = len(lst)
    temp = [0] * length
    for i in range(ceil(log2(length))):
        update = lambda cur, size: [cur * size * 2, size * (cur * 2 + 1), cur * 2 * size];size = 2 ** i; complete, p1, p2, p3 = False, 0, size, 0; cur = 1

        while not complete:
            if p1 >= length:
                complete = True
            elif p2 >= length:
                complete, temp[p3:] = True, lst[p1:((cur-1) * size * 2 + size) * (size * ((cur-1) * 2 + 1) < length) + size * (length * ((cur-1) * 2 + 1) >= length)]
            else:
                if lst[p1] <= lst[p2]:
                    temp[p3] = lst[p1]; p1, p3 = p1 + 1, p3 + 1; [[temp[p3:cur * size * 2]],[p1, p2, p3], cur] = [[lst[p2:2 * cur * size]], update(cur, size), cur + 1] if p1 % size == 0 else [[temp[p3:cur * size * 2]], [p1, p2, p3], cur]
                    
                else:
                    temp[p3] = lst[p2]; p2, p3 = p2 + 1, p3 + 1; [[temp[p3:cur * size * 2]],[p1, p2, p3], cur] = [[lst[p1:size * (2 * (cur-1) + 1)]], update(cur, size), cur + 1] if p2 % size == 0 else [[temp[p3:cur * size * 2]], [p1, p2, p3], cur]
            
                        
        lst = temp.copy()
    return lst


lst = [4,2,7,1,0, -1, 5,-5]
print(MergeSort(lst))