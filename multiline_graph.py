import matplotlib.pyplot as p
x=[2,4,6,8,10]
y=[6,7,8,2,4]
x2=[1,3,5,7,9]
y2=[7,8,2,4,2]
p.bar(x,y,label='Bar1')
p.bar(x2,y2,label='Bar2')
p.xlabel('x')
p.ylabel('y')
p.title('Multi-line graph')
p.legend()
p.show()