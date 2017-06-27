desserts = ["ice cream", "cookies"]
desserts.sort()
print(desserts)
desserts.index("ice cream")
food = desserts
food.extend(["brocoli", "turnips"])
print("desserts: {} and foor: {}".format(desserts, food))

list1 = [1, 3, 44, 34, 12, 3434, 20, 33]


def only120(list1):
    for i in list1:
        if i <= 20:
            print("Number < 20: {}".format(i))
        else:
            continue


only120(list1)
