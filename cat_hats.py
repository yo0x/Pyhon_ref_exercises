cats = {'': ''}
e = "0"
for i in range(1, 11):
    e = str(i)
    cats["cat" + e] = "No Hat"

for rounds in range(0, 11):
    wround = rounds
    ccround = 1
    if rounds == 0:
        continue
    if wround == 1:
        wround += 1
        ccround += 1
        for imnum in range(0, 11, 2):
            nc = str(imnum)
            ncint = int(nc)
            bncint = ncint
            while bncint == ncint:
                bncint += 1
                cats["cat" + nc] = 'Hat'
                continue
        print(cats)
    elif (ccround == ccround + 1):
        ccround += 1
        for imnum2 in range(0, 10, 3):
            nc2 = str(imnum2)
            ncint2 = int(nc2)
            bncint2 = ncint2
            if imnum2 == 0:
                continue
            while bncint2 == ncint2:
                bncint2 += 1
                if cats["cat" + nc2] == 'Hat':
                    cats["cat" + nc2] = 'No Hat'
                else:
                    cats["cat" + nc2] = 'Hat'
                continue

print(cats)
