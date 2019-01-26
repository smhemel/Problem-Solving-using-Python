from tkinter import *
def iCalc(source,side):
    storeObj = Frame(source, borderwidth = 1, bd = 4, bg = "powder blue")
    storeObj.pack(side=side, expand = YES, fill = BOTH)
    return storeObj
def button(source, side, text, command = None):
    storeObj = Button(source, borderwidth = 1, bd = 4, bg = "powder blue")
    storeObj.pack(side=side, expand = YES, fill = BOTH)
    return storeObj
class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font','arial 20 bold')
        self.pack(expand = YES, fill = BOTH)
        self.master.title('calculator')

        display = StringVar()
        Entry(self, relief = RIDGE,
              textvariable = display, justify = 'right',bd=30,bg='powder blue').pack(side = TOP, expand = YES,fill=BOTH)
        for clearBut in(["CE"],["C"]):
            erase = iCalc(self,TOP)
            for ichar in clearBut:
                button(erase,LEFT,ichar, lambda storeObj = display, q=ichar: storeObj.set(''))
        for numbut in("789/","456*","123-","0.+"):
            FunctionNum = iCalc(self,TOP)
            for char in numbut:
                button(FunctionNum, LEFT, char, lambda storeObj = display, q=char: storeObj.set(storeObj.get()+q))
        EqualsButton = iCalc(self, TOP)
        
if __name__ == '__main__':
    app().mainloop()
