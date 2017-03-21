
def allSubstrings(S):
    found = {}
    substrings = []
    getAllSubstrings(S, found, substrings)
    for s in substrings:
        print(s)

def getAllSubstrings(S, found, substrings):
    if (len(S) == 0):
        return

    if (S in found):
        return

    for i in range(len(S)):
        if(S not in found):
            substrings.append(S)
            found[S] = True

        getAllSubstrings(S[i + 1:], found, substrings)
        getAllSubstrings(S[:len(S) - i - 1], found, substrings)


def lskd(S, K):
    ''' longest substring with k distinct'''
    pass



def main():
    allSubstrings("house")

if __name__ == '__main__':
    main()
