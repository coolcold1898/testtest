s1 = '../app/'+input()
s2 = '../app/'+input()
f1 = open(s1,'r')
c1 = f1.readlines()
f1.close()
f2 = open(s2,'r')
c2 = f2.readlines()
f2.close()
l1 = [int(x) for x in c1[0].split()]
l2 = [int(x) for x in c2[0].split()]
for i in range(len(l2)):
    l1.append(l2[i])
l1.sort()
for i in l1:
    print(i,end=' ')
print('')