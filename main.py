from tkinter import *
root = Tk()

root.title('calculator')

equation = StringVar()

e = Entry(root, text= equation, width= 35, borderwidth= 5)
e.grid(row= 0, column= 0, columnspan= 4)

expr= ''

def ins_num(x):
    global expr
    expr = expr+str(x)
    equation.set(expr)

def evaluate():
    try:
        global expr
        answr= str(eval(expr))
        equation.set(answr)
    except:
        equation.set('error')
        expr=''

def clear():
    global expr
    expr= ''
    equation.set(expr)


b_1 = Button(root,text=1, width = 7, height = 4, command= lambda: ins_num(1) )
b_2 = Button(root, text=2, width = 7, height = 4, command= lambda: ins_num(2) )
b_3 = Button(root, text=3, width = 7, height = 4, command= lambda: ins_num(3))
b_4 = Button(root, text=4, width = 7, height = 4, command= lambda: ins_num(4) )
b_5 = Button(root, text=5, width = 7, height = 4, command= lambda: ins_num(5) )
b_6 = Button(root, text=6, width = 7, height = 4, command= lambda: ins_num(6) )
b_7 = Button(root, text=7, width = 7, height = 4, command= lambda: ins_num(7) )
b_8 = Button(root, text=8, width = 7, height = 4, command= lambda: ins_num(8) )
b_9 = Button(root, text=9, width = 7, height = 4, command= lambda: ins_num(9) )
b_0 = Button(root, text=0, width = 7, height = 4, command= lambda: ins_num(0) )
b_dot = Button(root, text='.', width = 7, height = 4, command= lambda: ins_num('.') )
b_clear = Button(root, text='clear', width = 7, height = 4,command = clear )
b_equal = Button(root, text='=', width = 7, height = 4, command =evaluate)
b_add = Button(root, text = '+', width = 7, height = 4, command= lambda: ins_num('+'))
b_sub = Button(root, text = '-', width = 7, height = 4, command= lambda: ins_num("-"))
b_mult = Button(root, text = 'X', width = 7, height = 4, command= lambda: ins_num('*') )

root.rowconfigure((0,1), weight=1)  # make buttons stretch when
root.columnconfigure((0,2), weight=1)  # when window is resized

b_1.grid(row= 3, column =0)
b_2.grid(row= 3, column =1)
b_3.grid(row= 3, column =2)
b_4.grid(row =2, column =0)
b_5.grid(row =2, column =1)
b_6.grid(row =2, column =2)
b_7.grid(row =1,column =0)
b_8.grid(row =1, column =1)
b_9.grid(row =1, column =2)
b_0.grid(row =4, column =1)
b_dot.grid(row =4, column =2)
b_clear.grid(row =4, column =0)
b_equal.grid(row =4, column =3)
b_add.grid(row =3, column =3)
b_sub.grid(row =2, column =3)
b_mult.grid(row =1, column =3)

root.mainloop()