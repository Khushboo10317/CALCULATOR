from tkinter import*
import math as m
import tkinter.messagebox

window=Tk()
window.title('My Calculator')
window.configure(background="powder blue")
window.geometry("480x568")

heading = Label(window, text='My Calculator', font='bold')
calculator= Frame(window)
calculator.grid()
font=('arial',20,'bold')
class Calculator():

    def __init__(self):
        self.total=0
        self.current=""
        self.input=True
        self.check_sum=False
        self.option= ""
        self.result=False
    def enterednumber(self,num):
        self.result=False
        firstnum=textDisplay.get()
        secondnum=str(num)
        if self.input:
           self.current=secondnum
           self.input=False
        else :
            if secondnum=='.':
                if secondnum in firstnum:
                    return
            self.current=firstnum+secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.func()
        else:
            self.total=float(textDisplay.get())


    def display(self,value):
        textDisplay.delete(0,END)
        textDisplay.insert(0,value)

    def func(self):
        if self.option=="add":
           self.total+=self.current
        if self.option == "sub":
           self.total -= self.current
        if self.option == "multi":
           self.total *= self.current
        if self.option == "divide":
           self.total /= self.current
        if self.option == "mod":
           self.total %= self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)

    def operation(self,option):
        self.current=float(self.current)
        if self.check_sum:
            self.func()
        elif not self.result:
            self.total=self.current
            self.input=True
        self.check_sum=True
        self.option=option
        self.result=False


    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input = True
    def all_clear_Entry(self):
        self.Clear_Entry()
        self.total=0
    def mathsPM(self):
        self.result = False
        self.current =-(float(textDisplay.get()))
        self.display(self.current)
    def squared(self):
        self.result = False
        self.current =m.sqrt(float(textDisplay.get()))
        self.display(self.current)
    def cos(self):
        self.result = False
        self.current =m.cos(m.radians(float(textDisplay.get())))
        self.display(self.current)
    def cosh(self):
        self.result = False
        self.current =m.cosh(m.radians(float(textDisplay.get())))
        self.display(self.current)
    def tan(self):
        self.result = False
        self.current =m.tan(m.radians(float(textDisplay.get())))
        self.display(self.current)
    def tanh(self):
        self.result = False
        self.current =m.tanh(m.radians(float(textDisplay.get())))
        self.display(self.current)
    def log2(self):
        self.result = False
        self.current =m.log2(float(textDisplay.get()))
        self.display(self.current)
    def ln(self):
        self.result = False
        self.current =m.log(float(textDisplay.get()))
        self.display(self.current)
    def  exp(self):
        self.result = False
        self.current =m.exp(float(textDisplay.get()))
        self.display(self.current)
    def sin(self):
        self.result = False
        self.current =m.sin(m.radians(float(textDisplay.get())))
        self.display(self.current)
    def sinh(self):
        self.result = False
        self.current =m.sinh(m.radians(float(textDisplay.get())))
        self.display(self.current)
    def power3(self):
        self.result = False
        self.current =m.pow(float(textDisplay.get()),3)
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current =m.log10(float(textDisplay.get()))
        self.display(self.current)

    def pi(self):
        self.result = False
        self.current=m.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current=m.tau
        self.display(self.current)
    def e(self):
        self.result = False
        self.current=m.e
        self.display(self.current)
    def acosh(self):
        self.result = False
        self.current =m.acosh(float(textDisplay.get()))
        self.display(self.current)
    def asinh(self):
        self.result = False
        self.current =m.asinh(float(textDisplay.get()))
        self.display(self.current)
    def factorial(self):
        self.result = False
        self.current =m.factorial(float(textDisplay.get()))
        self.display(self.current)

    def power2(self):
        self.result = False
        self.current = m.pow(float(textDisplay.get()),2)
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = m.degrees(float(textDisplay.get()))
        self.display(self.current)

action=Calculator()
textDisplay=Entry(calculator,font=('arial',20,'bold'),bg="white",bd=30,width=28,justify=RIGHT)
textDisplay.grid(row=0,column=0,columnspan=4,pady=1)
textDisplay.insert(0,"0")

number = "789456123"
p=0
b=[]
for i in range(2,5):
    for j in range(3):
        b.append(Button(calculator,width=6,height=2,font=font,bd=4,text=number[p],bg="light grey"))
        b[p].grid(row=i,column=j,pady=1)
        b[p]["command"]=lambda y=number [p]:action.enterednumber(y)
        p=p+1
btnclear=Button(calculator,text=chr(67),width=6,height=2,font=font,bd=4,bg="grey",command=action.Clear_Entry).grid(row=1,column=0,pady=1)
btnAllclear=Button(calculator,text=chr(67)+chr(69),width=6,height=2,font=font,bd=4,bg="grey",command=action.all_clear_Entry).grid(row=1,column=1,pady=1)
btnsq=Button(calculator,text="√",width=6,height=2,font=font,bd=4,bg="sky blue",command=action.squared).grid(row=1,column=2,pady=1)
btnadd=Button(calculator,text="+",width=6,height=2,font=font,bd=4,bg="sky blue",command=lambda :action.operation("add")).grid(row=1,column=3,pady=1)
btnsub=Button(calculator,text="-",width=6,height=2,font=font,bd=4,bg="sky blue",command=lambda :action.operation("sub")).grid(row=2,column=3,pady=1)
btnmul=Button(calculator,text="*",width=6,height=2,font=font,bd=4,bg="sky blue",command=lambda :action.operation("multi")).grid(row=3,column=3,pady=1)
btndiv=Button(calculator,text='/',width=6,height=2,font=font,bd=4,bg="sky blue",command=lambda :action.operation("divide")).grid(row=4,column=3,pady=1)
btnzero=Button(calculator,text="0",width=6,height=2,font=font,bd=4,bg="light grey",command=lambda :action.enterednumber(0)).grid(row=5,column=0,pady=1)
btndot=Button(calculator,text=".",width=6,height=2,font=font,bd=4,bg="sky blue",command=lambda :action.enterednumber(".")).grid(row=5,column=1,pady=1)
btnpm=Button(calculator,text=chr(177),width=6,height=2,font=font,bd=4,bg="sky blue",command=action.mathsPM).grid(row=5,column=2,pady=1)
btnequals=Button(calculator,text="=",width=6,height=2,font=font,bd=4,bg="sky blue",command=action.sum_of_total).grid(row=5,column=3,pady=1)
btnpi=Button(calculator,text="π",width=6,height=2,font=font,bd=4,bg="powder blue",command=action.pi).grid(row=1,column=7,pady=1)
btnsin=Button(calculator,text="sin",width=6,height=2,font=font,bd=4,bg="powder blue",command=action.sin).grid(row=1,column=4,pady=1)
btncos=Button(calculator,text="cos",width=6,height=2,font=font,bd=4,bg="powder blue",command=action.cos).grid(row=1,column=5,pady=1)
btntan=Button(calculator,text="tan",width=6,height=2,font=font,bd=4,bg="powder blue",command=action.tan).grid(row=1,column=6,pady=1)
btnsinh=Button(calculator,text="sinh",width=6,height=2,font=font,bd=4,bg="powder blue",command=action.sinh).grid(row=2,column=4,pady=1)
btncosh=Button(calculator,text="cosh",width=6,height=2,font=font,bd=4,bg="powder blue",command=action.cosh).grid(row=2,column=5,pady=1)
btntanh=Button(calculator,text="tanh",width=6,height=2,font=font,bd=4,bg="powder blue",command=action.tanh).grid(row=2,column=6,pady=1)
btntwopi=Button(calculator,text="2π",width=6,height=2,font=font,bd=4,bg="powder blue",command=action.tau).grid(row=2,column=7,pady=1)
btnlog=Button(calculator,text="ln",width=6,height=2,font=font,bd=4,bg="powder blue",command=action.ln).grid(row=5,column=6,pady=1)
btnexp=Button(calculator,text="Exp",width=6,height=2,font=font,bd=4,bg="powder blue",command=action.exp).grid(row=3,column=5,pady=1)
btnmod=Button(calculator,text="Mod",width=6,height=2,font=font,bd=4,bg="powder blue",command=lambda :action.operation("mod")).grid(row=3,column=6,pady=1)
btnE=Button(calculator,text="e",width=6,height=2,font=font,bd=4,bg="powder blue",command=action.e).grid(row=3,column=7,pady=1)
btnpower3=Button(calculator,text="x^3",width=6,height=2,font=font,bd=4,bg="powder blue",command=action.power3).grid(row=4,column=4,pady=1)
btndeg=Button(calculator,text="deg",width=6,height=2,font=font,bd=4,bg="powder blue",command=action.degrees).grid(row=5,column=4,pady=1)
btnasinh=Button(calculator,text="asinh",width=6,height=2,font=font,bd=4,bg="powder blue",command=action.asinh).grid(row=4,column=6,pady=1)
btnacosh=Button(calculator,text="acosh",width=6,height=2,font=font,bd=4,bg="powder blue",command=action.acosh).grid(row=4,column=7,pady=1)
btnlog2=Button(calculator,text="log2",width=6,height=2,font=font,bd=4,bg="powder blue",command=action.log2).grid(row=4,column=5,pady=1)
btnlog10=Button(calculator,text="log10",width=6,height=2,font=font,bd=4,bg="powder blue",command=action.log10).grid(row=5,column=5,pady=1)
btnexpm1=Button(calculator,text="x!",width=6,height=2,font=font,bd=4,bg="powder blue",command=action.factorial).grid(row=5,column=7,pady=1)
btnpow2=Button(calculator,text="x^2",width=6,height=2,font=font,bd=4,bg="powder blue",command=action.power2).grid(row=3,column=4,pady=1)

lDisplay=Label(calculator,text="Scientific Calculator",font=('arial',30,'bold'),justify=CENTER,bg= "grey")
lDisplay.grid(row=0,column=4,columnspan=4)

def iExit():
    iExit=tkinter.messagebox.askyesno("My Calculator","Confirm if you want to exit")
    if iExit>0:
        window.destroy()
        return

def Scientific():
    window.resizable(width=False, height=False)
    window.geometry("944x568")

def Standard():
    window.resizable(width=False, height=False)
    window.geometry("480x568")

menubar = Menu(calculator)
fmode=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Mode", menu=fmode)
fmode.add_command(label="Standard",command=Standard)
fmode.add_command(label="Scientific",command=Scientific)
fmode.add_command(label="Exit",command=iExit)
window.config(menu=menubar)
window.mainloop()