cats = {'': ''}
e = "0"
ccround1 = 0
ccround2 = 0
ccround3 = 0
for i in range(1, 101):
    e = str(i)
    cats["cat" + e] = "No Hat"

for rounds in range(0, 101):
    wround = rounds
    if rounds == 0:
        continue
    if wround == 1 or ccround1 == 1:
        wround += 1
        ccround2 = 1
        ccround1 = 0
        ccround3 = 0
        for imnum in range(0, 101):
            nc = str(imnum)
            ncint = int(nc)
            bncint = ncint
            while bncint == ncint:
                bncint += 1
                cats["cat" + nc] = 'Hat'
                continue
            #        print(cats)
    elif (ccround2 == 1):
        ccround2 = 0
        ccround1 = 0
        ccround3 = 1
        for imnum2 in range(0, 101, 2):
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
    elif (ccround3 == 1):
        ccround2 = 0
        ccround1 = 1
        ccround3 = 0
        for imnum3 in range(0, 101, 3):
            nc3 = str(imnum3)
            ncint3 = int(nc3)
            bncint3 = ncint3
            if imnum3 == 0:
                continue
            while bncint3 == ncint3:
                bncint3 += 1
                if cats["cat" + nc3] == 'Hat':
                    cats["cat" + nc3] = 'No Hat'
                else:
                    cats["cat" + nc3] = 'Hat'
                continue

print(cats)
