from Tkinter import *
import math
root=Tk()
root.title('MyCalci')

e=Entry(root,width=25,font="Arial 30 bold",bd=9,bg='grey',justify='right')
e.grid(row=0,column=0,columnspan=5)

def add_entry(x):
    e.insert(16,x)

def result(y):
    e.delete(0,16)        #if length of entry is not known...write e.delete(0,END)
    e.insert(16,y)

def remove():
    e.delete(0,END)
def evalper(z):
    e.delete(0,END)
    z=float(z)
    z=z*100
    e.insert(16,z)
    
Button(root,text='7',width=10,height=5,bg='light yellow2',command=lambda:add_entry('7')).grid(row=1,column=0,sticky=E+W+N+S)
Button(root,text='8',width=10,height=5,bg='light yellow2',command=lambda:add_entry('8')).grid(row=1,column=1,sticky=E+W+N+S)
Button(root,text='9',width=10,height=5,bg='light yellow2',command=lambda:add_entry('9')).grid(row=1,column=2,sticky=E+W+N+S)
Button(root,text='+',width=10,height=5,bg='old lace',command=lambda:add_entry('+')).grid(row=1,column=3,sticky=E+W+N+S)
Button(root,text='C',width=10,height=5,font="Arial 10 bold",bg='light yellow2',command=remove).grid(row=1,column=4,sticky=E+W+N+S)

Button(root,text='4',width=10,height=5,bg='light yellow2',command=lambda:add_entry('4')).grid(row=2,column=0,sticky=E+W+N+S)
Button(root,text='5',width=10,height=5,bg='light yellow2',command=lambda:add_entry('5')).grid(row=2,column=1,sticky=E+W+N+S)
Button(root,text='6',width=10,height=5,bg='light yellow2',command=lambda:add_entry('6')).grid(row=2,column=2,sticky=E+W+N+S)
Button(root,text='-',width=10,height=5,bg='old lace',command=lambda:add_entry('-')).grid(row=2,column=3,sticky=E+W+N+S)
Button(root,text='*',width=10,height=5,bg='old lace',command=lambda:add_entry('*')).grid(row=2,column=4,sticky=E+W+N+S)

Button(root,text='1',width=10,height=5,bg='light yellow2',command=lambda:add_entry('1')).grid(row=3,column=0,sticky=E+W+N+S)
Button(root,text='2',width=10,height=5,bg='light yellow2',command=lambda:add_entry('2')).grid(row=3,column=1,sticky=E+W+N+S)
Button(root,text='3',width=10,height=5,bg='light yellow2',command=lambda:add_entry('3')).grid(row=3,column=2,sticky=E+W+N+S)
Button(root,text='/',width=10,height=5,bg='old lace',command=lambda:add_entry('/')).grid(row=3,column=3,sticky=E+W+N+S)
Button(root,text='%',width=10,height=5,bg='old lace',command=lambda:add_entry('%')).grid(row=3,column=4,sticky=E+W+N+S)


Button(root,text='.',width=10,height=5,bg='old lace',command=lambda:add_entry('.')).grid(row=4,column=0,sticky=E+W+N+S)
Button(root,text='0',width=10,height=5,bg='light yellow2',command=lambda:add_entry('0')).grid(row=4,column=1,sticky=E+W+N+S)
Button(root,text='(',width=10,height=5,bg='light yellow2',command=lambda:add_entry('(')).grid(row=4,column=3,sticky=E+W+N+S)
Button(root,text=')',width=10,height=5,bg='light yellow2',command=lambda:add_entry(')')).grid(row=4,column=4,sticky=E+W+N+S)
Button(root,text='=',width=10,height=5,bg='old lace',command=lambda:result(eval(e.get()))).grid(row=4,column=2,sticky=E+W+N+S)


#Button(root,text='1/x',width=10,height=5,bg='pink',command=lambda:add_entry(eval(1/e.get())).grid(row=4,column=3,sticky=E+W+N+S)
#Button(root,text='CE',width=10,height=5,bg='grey',).grid(row=4,column=3,sticky=E+W+N+S,columnspan=2)



root.mainloop()
