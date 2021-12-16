import matplotlib.pyplot as p
l=('Python','C++','Ruby','Java')
s=[215,130,245,210]
c=['yellow','green','red','skyblue']
p.pie(s,labels=l,colors=c)
p.axis('equal')
p.show()