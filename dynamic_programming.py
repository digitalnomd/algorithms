def lcs(first, second):
    results = dict()
    return lcs_mem(first, second, results)

def lcs_mem(first, second, results):
    key = ""
    if first > second:
        key = first + "," + second
    else:
        key = second + "," + first

    if len(first) == 0 or len(second) == 0:
        return ''
    elif key in results:
        return results[key]
    elif first[-1] == second[-1]:
        result = lcs(first[:-1], second[:-1]) + first[-1]
        results[key] = result
        return result
    else:
        lcsLeft = lcs(first[:-1], second)
        lcsRight = lcs(first, second[:-1])

        if len(lcsLeft) > len(lcsRight):
            return lcsLeft
        else:
            return lcsRight

def main():
    pass


if __name__ == '__main__':
    main()
