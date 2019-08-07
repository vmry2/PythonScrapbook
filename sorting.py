li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_li = sorted(li, reverse=True)

# print("Sorted Variable:\t", s_li)

li.sort(reverse=True)
# print("Original Variable:\t", li)


tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)
# print("Tuple\t", s_tup)

li = [-4, -5, -6, 3, 2, 1]
s_li = sorted(li, key=abs)
print(s_li)
