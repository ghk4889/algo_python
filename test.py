a = [-4, -1, -1, 0, 1, 1, 2]
a.reverse()
print(a[1:].index(-1))


def setting(prev, slowHead):
    tmpPrev = rev
    tmpNext = slowHead.next

    rev = slowHead
    rev.next = tmpPrev
    slowHead = tmpNext







