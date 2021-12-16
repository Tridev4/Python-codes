import matplotlib.pyplot as p
o=('Python','C++','Java','Perl','Scala','Lisp')
pe=[10,8,6,4,2,1]
p.barh(o,pe,align='center',color='b')
p.xlabel('Usage')
p.title('Lang. usage')
p.show()