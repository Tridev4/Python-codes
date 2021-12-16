
import sympy as sp
from Tkinter import*

def icalc(source,side):
    storeobj=Frame(source, borderwidth=18, bd=40, bg="grey")
    storeobj.pack(side=side, expand=YES,fill=BOTH)
    return storeobj

def button(source, side, text, command=None):
    storeobj=Button(source, text=text, command=command)
    storeobj.pack(side=side, expand=YES,fill=BOTH)
    return storeobj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font','arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('calculator')

        display=StringVar()
        Entry(self, relief=RIDGE,#we can also use flat and raise and groove here in place of ridge
              textvariable=display,justify="right",bd=90,bg="grey").pack(side=TOP, expand=YES, fill=BOTH)

        for clearbut in (["CE"],["C"]):
            erase=icalc(self,TOP)
            for ichar in clearbut:
                button(erase, LEFT, ichar,
                       lambda storeobj=display, q=ichar: storeobj.set(''))


        for Numbut in ("123456789", "0+-*/.e"):
            functionnum=icalc(self,TOP)
            for iEquals in Numbut:
                       button(functionnum, LEFT, iEquals,
                              lambda storeobj=display, q=iEquals : storeobj.set(storeobj.get() + q))

        Equalsbutton= icalc(self, TOP)
        for iEquals in "=":
            if iEquals == "=":
                btniEquals=button(Equalsbutton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>',
                                 lambda e, s=self, storeobj=display: s.calc(storeobj),'+')
            else:
                btniEquals=button(Equalsbutton, LEFT, iEquals,
                                  lambda storeobj=display, s=' %s  '%iEquals: storeobj.set(storeobj.get()+s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
            
        except :
                display.set("ERROR")


                
                
                       
        

if __name__=='__main__':
    app().mainloop()
    
