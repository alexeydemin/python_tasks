def bioHazard_old(n, allergic, poisonous):
    rules = get_rules(allergic, poisonous)
    #   print(rules)

    count = 0
    a = []
    for i in range(1, n + 1):
        print(i)
        # print('=== step' + str(i) + '===')
        temp = []
        #print(len(a))
        for elem in a:
            # if is_compatible(elem, i, rules):
            #     # print('Y')
            # else:
            #     # print('N')
            #if len(elem) == 1:
            #    continue
            if len(elem) == 1 or is_compatible(elem, i, rules):
                temp.append(elem + [i])
                print('A')
                count += 1
        a = temp
        a.append([i])
        print('B')
        count += 1
        #print(a)
        # print('=== end step' + str(i) + '===')
    return count


def is_compatible(elem, i, rules):
    print("launched")
    if i not in rules:
        #print('one')
        return True
    for al in rules[i]:
        if al in elem:
            #print('two')
            return False
    #print('three')
    return True


def get_rules(al, po):
    res = {}
    for i in range(len(al)):
        if po[i] in res:
            res[po[i]].append(al[i])
        else:
            res[po[i]] = [al[i]]

        if al[i] in res:
            res[al[i]].append(po[i])
        else:
            res[al[i]] = [po[i]]
    return res

def get_rules_old(allergic, poisonous):
    res = {}
    for i, p in enumerate(poisonous):
        if p in res:
            res[p].append(allergic[i])
        else:
            res[p] = [allergic[i]]

    for j, a in enumerate(allergic):
        if a in res:
            res[a].append(poisonous[j])
        else:
            res[a] = [poisonous[j]]
    return res


# for m in range(1, 21):
#     res = bioHazard(m, [], [])
#     print(m, res, int((m+1)*m/2))

# res = bioHazard(8, [], [])

# print(res)

#  2 3 4 5 6  7  8
# 1       5 6  7  8  8 (8-1+1)
# 2       8 10 12 14 7 (8-2+1)
# 3       9 12 15 18 6 (8-3+1)
# 4       8 12 16 20 5 (8-4+1)_
# 5       5 10 15 20 4 (8-5+1)
# 6       0 6  12 18 3
# 7       0 0  7  14 2
# 8               8

# entries = ()
def entries_num(n, digit):
    return (n - digit + 1) * digit


# r = entries_num(3, 2)
# print(r)

def bh2(m, al, po):
    pers = int((m + 1) * m / 2)
    for i in range(len(al)):
        big = max(al[i], po[i])
        small = min(al[i], po[i])
        sub = (m - big + 1) * small
        pers -= sub
    return pers +1

#r = bh2(5, [1, 2], [3, 5])
#print(r)

def bh3(m, al, po):
    f = [[0] * m for i in range(m)]
    for i in range(m):
        for j in range(m):
            if i >= j:
                f[i][j] = 1
    print(f)
    print(al)
    print('====')
    for k, a in enumerate(al):
        print(al[k], po[k])
        big = max(al[k], po[k])
        print('big =' + str(big))
        small = min(al[k], po[k])
        print('small =' + str(small))
        print('----')
        for j in range(1, small + 1):
            for i in range(big, m + 1):
                print('i=' + str(i), 'j=' + str(j))
                f[i - 1][j - 1] = 0
    print('===end===')
    print(f)
    return sum(sum(f, []))


# r = bh2(4, [1, 2], [3, 4])
# print(r)
# r = bh3(5, [1, 2], [3, 5])
# print(r)


def bioHazard4(m, al, po):
    # f = [[0] * m for i in range(m)]
    f = []
    for i in range(m):
        # print(i)
        f.append([0] * m)
        for j in range(m):
            if i >= j:
                f[i][j] = 1

    for k, a in enumerate(al):
        big = max(al[k], po[k])
        small = min(al[k], po[k])
        for j in range(0, small):
            for i in range(big - 1, m):
                f[i][j] = 0
    return sum(map(sum, f))


def bioHazard4(m, al, po):
    f = {}
    for k in range(len(al)):
        big = max(al[k], po[k])
        small = min(al[k], po[k])
        for j in range(0, small):
            for i in range(big - 1, m):
                f[str(i) + str(j)] = 1
    return int((m + 1) * m / 2 - len(f))


#r = bioHazard_old(5, [1, 2], [3, 5])
r = bioHazard_old(8, [2,3,4,3], [8,5,6,4])
print(r)
#print(get_rules([1, 2], [3, 5]))
#print(get_rules_old([1, 2], [3, 5]))