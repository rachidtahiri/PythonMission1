# utilisation des compteurs pour savoir combien de fois le nombre est grand et combien de fois est petit

# le compteur i est incrementé si 'a' est grand
#le compteur j est incrementé si 'a' est petit
i=0
j=0
#le compteur k est incrementé si 'b' est grand
#le compteur l est incrementé si 'b' est petit
k=0
l=0
#le compteur m est incrementé si 'c' est grand
#le compteur n est incrementé si 'c' est petit
m=0
n=0
#le compteur o est incrementé si 'd' est grand
#le compteur p est incrementé si 'd' est petit
o=0
p=0
#le compteur r est incrementé si 'e' est grand
#le compteur s est incrementé si 'e' est petit
r=0
s=0

a=input("enter un nombre a ")
print("a= ",a)
a=int(a)
b=input("entrer un nombre b ")
print("b= ",b)
b=int(b)
c=input("entrer un nombre c ")
print("c= ",c)
c=int(c)
d=input("entrer un nombre d ")
print("d= ",d)
d=int(d)
e=input("enter un nombre e ")
print("e= ",e)
e=int(e)

if a>b:
    i=i+1
    l=l+1
else :
    j=j+1
    k=k+1

if a>c:
    i=i+1
    n=n+1
else :
    j=j+1
    m=m+1
if b>c:
    k=k+1
    n=n+1
else :
    l=l+1
    m=m+1
    
if a>d:
    i=i+1
    p=p+1
else:
    j=j+1
    o=o+1
if b>d:
    k=k+1
    p=p+1
else:
    l=l+1
    o=o+1
if c>d:
    m=m+1
    p=p+1
else:
    n=n+1
    o=o+1
    
if a>e:
    i=i+1
    s=s+1
else:
    j=j+1
    r=r+1
if b>e:
    k=k+1
    s=s+1
else:
    l=l+1
    r=r+1
if c>e:
    m=m+1
    s=s+1
else:
    n=n+1
    r=r+1
if d>e:
    o=o+1
    s=s+1
else:
    p=p+1
    r=r+1
    
#si les deux compteurs d'un nombre egale à 2, ça veut dire que le nombre représente la mediane

if i==2 and j==2:
    print("la mediane est a= ",a)
if k==2 and l==2 :
    print("la mediane est b= ",b)
if m==2 and n==2 :
    print("la mediane est c= ",c)
if o==2 and p==2:
    print("la mediane est d= ",d)
if r==2 and s==2:
    print("la mediane est e= ",e)


