from random import randrange


def partition(lst, start, end, pivot):
    lst[pivot], lst[end] = lst[end], lst[pivot]
    store_index = start
    for i in range(start, end):
        if lst[i] < lst[end]:
            lst[store_index], lst[i] = lst[i], lst[store_index]
            store_index += 1

    lst[end], lst[store_index] = lst[store_index], lst[end]

    return store_index


def quick_sort(lst, start, end):
    if start >= end:
        return lst

    pivot = randrange(start, end + 1)
    new_pivot = partition(lst, start, end, pivot)
    quick_sort(lst, start, new_pivot - 1)
    quick_sort(lst, new_pivot + 1, end)


def sort(lst):
    quick_sort(lst, 0, len(lst) - 1)
    return lst

def bt_dups(node, subtrees):
    if node == None:
        return False

    lst = subtrees[node.value]
    tup = (node.left, node.right)

    if tup in lst:
        return True
    else:
        lst += tup
        subtrees[node.value] = lst
        return bt_dups(node.left, subtrees) or bt_dups(node.right, subtrees)




print(sort([]))
print(sort([1, 2, 3, 4]))
print(sort([-5, 3, -2, 3, 19, 5]))
