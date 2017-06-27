univers = [['MIT', 3434, 443], ['MIT2', 232, 43445643], ['MIT3', 235762, 43443565], ['MI4T', 25632, 43445673],
           ['MI5T', 67232, 43456743], ['MIT6', 2532, 43443], ['MIT7', 2562, 43567443]]
list1 = []
list2 = []


def enrollment_stats(univers):
    for i in univers:
        appe = i[1]
        list1.append(appe)
        appe2 = i[2]
        list2.append(appe2)
    # print(list1)
    # print(list2)

    return list1, list2


def mean(enrollment_stars):
    print(enrollment_stats(univers))


mean(list1)
# enrollment_stats(univers)
