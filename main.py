from tkinter import *
import math
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
        expr= ''
    except:
        equation.set('error')
        expr=''

def clear():
    global expr
    expr= ''
    equation.set(expr)





b_1 = Button(root,text=1, fg='white', bg='black', width = 7, height = 4, command= lambda: ins_num(1) )
b_2 = Button(root, text=2, fg='white', bg='black', width = 7, height = 4, command= lambda: ins_num(2) )
b_3 = Button(root, text=3, fg='white', bg='black', width = 7, height = 4, command= lambda: ins_num(3))
b_4 = Button(root, text=4, fg='white', bg='black', width = 7, height = 4, command= lambda: ins_num(4) )
b_5 = Button(root, text=5, fg='white', bg='black', width = 7, height = 4, command= lambda: ins_num(5) )
b_6 = Button(root, text=6, fg='white', bg='black', width = 7, height = 4, command= lambda: ins_num(6) )
b_7 = Button(root, text=7, fg='white', bg='black', width = 7, height = 4, command= lambda: ins_num(7) )
b_8 = Button(root, text=8, fg='white', bg='black', width = 7, height = 4, command= lambda: ins_num(8) )
b_9 = Button(root, text=9, fg='white', bg='black', width = 7, height = 4, command= lambda: ins_num(9) )
b_0 = Button(root, text=0, fg='white', bg='black', width = 7, height = 4, command= lambda: ins_num(0) )
b_dot = Button(root, text='.',fg='black', bg='light green', width = 7, height = 4, command= lambda: ins_num('.') )
b_clear = Button(root, text='clear',fg='black', bg='orange', width = 7, height = 4,command = clear )
b_equal = Button(root, text='=',fg='black', bg='orange', width = 7, height = 4, command =evaluate)
b_add = Button(root, text = '+',fg='black', bg='light green', width = 7, height = 4, command= lambda: ins_num('+'))
b_sub = Button(root, text = '-', fg='black', bg='light green',width = 7, height = 4, command= lambda: ins_num("-"))
b_mult = Button(root, text = 'x',fg='black', bg='light green', width = 7, height = 4, command= lambda: ins_num('*') )

b_division = Button(root, text = '/',fg='black', bg='light green', width = 7, height = 4, command= lambda: ins_num('/') )
b_power = Button(root, text = '^',fg='black', bg='light green', width = 7, height = 4, command= lambda: ins_num('**') )
b_rpar = Button(root, text = '(',fg='black', bg='light green', width = 7, height = 4, command= lambda: ins_num('(') )
b_lpar = Button(root, text = ')',fg='black', bg='light green', width = 7, height = 4, command= lambda: ins_num(')') )
b_factorial = Button(root, text = '!',fg='black', bg='light green', width = 7, height = 4, command=lambda: ins_num(' math.factorial( '))
b_sin = Button(root, text = 'sin',fg='black', bg='light green', width = 7, height = 4, command= lambda: ins_num('math.sin(') )
b_cos = Button(root, text = 'cos',fg='black', bg='light green', width = 7, height = 4, command= lambda: ins_num('math.cos(') )
b_tan = Button(root, text = 'tan',fg='black', bg='light green', width = 7, height = 4, command= lambda: ins_num('math.tan(') )
b_expo = Button(root, text = 'e',fg='black', bg='light green', width = 7, height = 4, command= lambda: ins_num('math.e') )
b_log = Button(root, text = 'log',fg='black', bg='light green', width = 7, height = 4, command= lambda: ins_num('math.log(') )
b_ln = Button(root, text = 'ln',fg='black', bg='light green', width = 7, height = 4, command= lambda: ins_num('math.log(') )
b_pi = Button(root, text = '兀',fg='black', bg='light green', width = 7, height = 4, command= lambda: ins_num('math.pi') )

root.rowconfigure((0,1), weight=1)  # make buttons stretch when
root.columnconfigure((0,2), weight=1)  # when window is resized

b_1.grid(row= 6, column =0)
b_2.grid(row= 6, column =1)
b_3.grid(row= 6, column =2)
b_4.grid(row =5, column =0)
b_5.grid(row =5, column =1)
b_6.grid(row =5, column =2)
b_7.grid(row =4,column =0)
b_8.grid(row =4, column =1)
b_9.grid(row =4, column =2)
b_0.grid(row =7, column =1)
b_dot.grid(row= 7, column =3)
b_clear.grid(row =7, column =0)
b_equal.grid(row =7, column =2)
b_add.grid(row =5, column =3)
b_sub.grid(row =6, column =3)
b_mult.grid(row =4, column =3)

b_division.grid(row =3, column =3)
b_power.grid(row =2, column =3)
b_rpar.grid(row =1, column =0)
b_lpar.grid(row =1, column =1)
b_factorial.grid(row =1, column =2)
b_sin.grid(row =2,column =0)
b_cos.grid(row =2, column =1)
b_tan.grid(row =2, column =2)
b_expo.grid(row= 3, column =0)
b_log.grid(row= 3, column =1)
b_ln.grid(row= 3, column =2)
b_pi.grid(row= 1, column =3)




root.mainloop()
