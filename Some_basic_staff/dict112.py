birth_dic = dict(lukeskywalker='5/24/19', Obiwankenobi='3/11/57', darthvader='4/1/41')


def checkdict(birth_dic):
    if "Yoda" in birth_dic and "Darth Vader" in birth_dic:
        print("Good")
    else:
        birth_dic["Yoda"] = "Unknown"
        birth_dic["Darth Vader"] = "Unknown"
        print(birth_dic)
    for i in birth_dic:
        print("""{}
                """.format(i))


checkdict(birth_dic)
