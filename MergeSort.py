from math import log2, ceil


def MergeSort(lst: list) -> list:
    temp = [0] * len(lst)
    for i in range(ceil(log2(len(lst)))):
        update = lambda cur, size: [(cur) * size * 2, size * ((cur) * 2 + 1), (cur) * 2 * size];size = 2 ** i; complete, p1, p2, p3 = False, 0, size, 0; cur = 1

        while not complete:
            if p1 >= len(lst):
                complete = True
            elif p2 >= len(lst):
                complete, temp[p3:] = True, lst[p1:((cur-1) * size * 2 + size) * ((cur-1) * size * 2 + size < len(lst)) + (len(lst)) * ((cur-1) * size * 2 + size >= len(lst))]
            else:
                if lst[p1] <= lst[p2]:
                    temp[p3] = lst[p1]; p1, p3 = p1 + 1, p3 + 1
                    if p1 % size == 0: temp[p3:(cur) * size * 2] = lst[p2:2 * (cur) * size]; p1, p2, p3 = update(cur, size); cur += 1
                else:
                    temp[p3] = lst[p2]; p2, p3 = p2 + 1, p3 + 1
                    if p2 % size == 0: temp[p3:(cur) * size * 2] = lst[p1:size * (2 * (cur-1) + 1)]; p1, p2, p3 = update(cur, size); cur += 1
            
                        
        lst = temp.copy()
    return lst


lst = [4,2,7,1,0, -1, 5,-5]
print(MergeSort(lst))                  