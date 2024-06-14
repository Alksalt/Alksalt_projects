def common_elements():
    set_first = set(range(100))
    set3 = set()
    for i in set_first:
        if i % 3 == 0:
            set3.add(i)
    set_second = set(range(100))
    set5 = set()
    for j in set_second:
        if j % 5 == 0:
            set5.add(j)
    new_set = set3.union(set5)
    common_set = set()
    for a in new_set:
        if a % 3 ==0 and a % 5 == 0:
            common_set.add(a)

    return common_set


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")