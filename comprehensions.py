nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# my_list = [n for n in nums]

# my_list = [n * n for n in nums]

# my_list = map(lambda n: n * n, nums)

# my_list = filter(lambda n: n % 2 == 0, nums)
# my_list = [n for n in nums if n % 2 == 0]

# my_list = [(letter, num) for letter in "abcd" for num in range(4)]

# print(my_list)

names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]

# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero

# my_dict = {name: hero for name, hero in zip(names, heros) if name != "Peter"}
# print(my_dict)

nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 9]
# my_set = set()
# for n in nums:
#     my_set.add(n)

# my_set = {n for n in nums}
# print(my_set)


# def gen_func(nums):
#     for n in nums:
#         yield n * n


# my_gen = gen_func(nums)

# for i in my_gen:
#     print(i)

my_gen = (n * n for n in nums)
