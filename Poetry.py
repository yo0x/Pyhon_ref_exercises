import random
nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert",
         "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over",
                "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]
aaa = ["A", "An", "a", "an"]


def makePoem():
    vaa = ''
    vadverb = random.choice(adverbs)
    vprep = random.choice(prepositions)
    vadj = random.choice(adjectives)
    vver = random.choice(verbs)
    vnouns = random.choice(nouns)
    vaa1 = random.choice(aaa)
    vadverb1 = random.choice(adverbs)
    vprep1 = random.choice(prepositions)
    vadj1 = random.choice(adjectives)
    vver1 = random.choice(verbs)
    vnouns1 = random.choice(nouns)
    vaa2 = random.choice(aaa)
    vadverb2 = random.choice(adverbs)
    vprep2 = random.choice(prepositions)
    vadj2 = random.choice(adjectives)
    vver2 = random.choice(verbs)
    vnouns2 = random.choice(nouns)
    if vadj1[0] == "a":
        vaa = aaa[1]
    elif vadj1[0] == "e":
        vaa = aaa[1]
    elif vadj1[0] == "i":
        vaa = aaa[1]
    elif vadj1[0] == "o":
        vaa = aaa[1]
    elif vadj1[0] == "u":
        vaa = aaa[1]
    else:
        vaa = aaa[0]

    print('''{0} {3} {5}
    {0} {3} {11} {10} {8} the {9} {17}
    {7}, the {11} {16}
    the {11} {16} {8} a {15} {17}.
    '''.format(vaa, vadverb, vprep, vadj, vver, vnouns, vaa1, vadverb1, vprep1, vadj1, vver1, vnouns1, vaa2, vadverb2,
               vprep2, vadj2, vver2, vnouns2))


makePoem()
