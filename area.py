import circle
import rectangle
c=0
ch='y'
while ch=='y':
    print('Menu:')
    print('1.Area of circle')
    print('2.Circumference of circle')
    print('3.Area of rectangle')
    print('4.Perimeter of rectangle')
    print('5.Quit')
    c=int(input('Enter the choice:'))
    if c==1:
        r=int(input('Enter the radius:'))
        print('The area is:',circle.area(r))
    elif c==2:
        r=int(input('Enter the radius:'))
        print('The circumference is:',circle.circumference(r))
    elif c==3:
        w=int(input('Enter the width:'))
        l=int(input('Enter the length:'))
        print('The area of rectangle is:',rectangle.area(w,l))
    elif c==4:
        w=int(input('Enter the width:'))
        l=int(input('Enter the length:'))
        print('The perimeter of rectangle is:',rectangle.perimeter(w,l))
    elif c==5:
        print('Quiting!!!!')
        ch='n'
    else:
        print('Error: invalid selection.')