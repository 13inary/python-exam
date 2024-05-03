lists = ["需要被删除的元素", 6, True]

lists.append("追加元素")
print(lists)

lists.remove("需要被删除的元素")
print(lists)

length = len(lists)
print(length)

element = lists[0]
print(element)

lists[1] = 10
print(lists)

maxs = max(lists)
mins = min(lists)
sortList = sorted(lists)
