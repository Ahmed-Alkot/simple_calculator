#from wolf_api import *π
# simple calculator in python
# importing everything from tkinter module
from tkinter import *
import math
# main GUI window
from tkinter import *
root=Tk()
root.title('calculator')
# creating a variable class
root.configure(bg='black')
equation = StringVar()
# creating an entry box for showing expressions, and palcing it in root
e = Entry(root, text=equation, width= 70, borderwidth= 10)
e.grid(row= 0, column= 0, columnspan= 10)
# globally declaring an expression and an equation variable
expr= ''
eq = ''

# defining a function that activates
# every button appropriately
def ins_num(x):
    global expr
    global eq
    if x=='*':
        eq = eq + str('x')
        equation.set(eq)
        expr = expr + str(x)
    elif x=='**':
        eq = eq + str('^')
        equation.set(eq)
        expr = expr + str(x)
    elif x=='/':
        eq = eq + str('÷')
        equation.set(eq)
        expr = expr + str(x)
    elif x=='math.e':
        eq = eq + str('e')
        equation.set(eq)
        expr = expr + str(x)

    elif x=='ln(':

        eq = eq + str(x)
        equation.set(eq)
        expr = expr + str('math.log(')

    elif x=='log(':

        eq = eq + str(x)
        equation.set(eq)
        expr = expr + str('(1/math.log(10))*math.log(')



    else:
        eq = eq + str(x)
        equation.set(eq)
        expr = expr + str(x)

def sin(x):
    global expr
    global eq
    eq = eq + str("sin(")
    equation.set(eq)
    expr = expr + str(x)
def cos(x):
    global expr
    global eq
    eq = eq + str("cos(")
    equation.set(eq)
    expr = expr + str(x)
def tan(x):
    global expr
    global eq
    eq = eq + str("tan(")
    equation.set(eq)
    expr = expr + str(x)
def fact(x):
    global expr
    global eq
    eq = eq + str("!")
    equation.set(eq)
    s= expr
    expr=""
    expr =  str(x)+str(s)+str(')')
# defining a function that evaluates
# the user-input expression
def evaluate():
    try:
        global expr
        answr= str(eval(expr))
        equation.set(answr)
    except:
        equation.set('error')
        expr=''
def pi(x):
    global expr
    global eq
    eq = eq + str("π")
    equation.set(eq)
    expr = expr+str(x)
# defining a function that clears the entry box

def clear():
    global expr
    global eq
    expr= ''
    eq = ''
    equation.set(eq)
def sqrt(x):
    global expr
    global eq
    eq = eq + str("sqrt(")
    equation.set(eq)
    expr = expr+str(x)
def arcsin(x):
    global expr
    global eq
    eq = eq + str("arcsin(")
    equation.set(eq)
    expr = expr+str(x)



def arccos(x):

    global expr
    global eq
    eq = eq + str("arccos(")
    equation.set(eq)
    expr = expr+str(x)


def arctan(x):
    global expr
    global eq
    eq = eq + str("arctan(")
    equation.set(eq)
    expr = expr+str(x)




b_rpar = PhotoImage(file = "bra1.png")
b_rparimage = b_rpar.subsample(10,10)
b_rpar = Button(root, text="AC", fg="black", image=b_rparimage, bg="black", command= lambda: ins_num(')')
               ).grid(row=1, column=1)

b_lpar = PhotoImage(file = "bra2.png")
b_lparimage = b_lpar.subsample(10,10)
b_lpar = Button(root, text="AC", fg="black", image=b_lparimage, bg="black", command= lambda: ins_num('(')
               ).grid(row=1, column=0)

b_factorial= PhotoImage(file = "fact.png")
b_factorialimage = b_factorial.subsample(10,10)
b_factorial = Button(root, text="AC", fg="black", image=b_factorialimage, bg="black",command= lambda: fact('math.factorial(')).grid(row=1, column=2)


b_pi = PhotoImage(file = "bi.png")
b_piimage = b_pi.subsample(10,10)
b_pi = Button(root, text="AC", fg="black", image=b_piimage, bg="black",command= lambda: pi('math.pi')
               ).grid(row=1, column=3)


b_sin = PhotoImage(file = "sin.png")
b_sinimage = b_sin.subsample(10,10)
b_sin = Button(root, text="AC", fg="black", image=b_sinimage, bg="black", command= lambda: sin('math.sin(')
               ).grid(row=2, column=0)


b_cos = PhotoImage(file = "cos.png")
b_cosimage = b_cos.subsample(10,10)
b_cos = Button(root, text="AC", fg="black", image=b_cosimage, bg="black", command= lambda: cos('math.cos(')
               ).grid(row=2, column=1)


b_tan= PhotoImage(file = "tan.png")
b_tanimage =b_tan.subsample(10,10)
b_tan = Button(root, text="AC", fg="black", image=b_tanimage, bg="black", command= lambda: tan('math.tan(')).grid(row=2, column=2)


b_power = PhotoImage(file = "power.png")
b_powerimage = b_power.subsample(10,10)
b_power = Button(root, text="AC", fg="black", image=b_powerimage, bg="black", command= lambda: ins_num('**')
               ).grid(row=2, column=3)


e = PhotoImage(file = "e.png")
eimage = e.subsample(10,10)
e = Button(root, text="AC", fg="black", image=eimage, bg="black", command= lambda: ins_num('math.e')
               ).grid(row=3, column=0)


b_ln = PhotoImage(file = "ln.png")
b_lnimage = b_ln.subsample(11,10)
b_ln = Button(root, text="AC", fg="black", image=b_lnimage, bg="black",  command= lambda: ins_num('ln(')
               ).grid(row=3, column=1)


b_log= PhotoImage(file = "log.png")
b_logimage =b_log.subsample(11,10)
b_log = Button(root, text="AC", fg="black", image=b_logimage, bg="black", command= lambda: ins_num('log(')).grid(row=3, column=2)


b_root = PhotoImage(file = "sqrt.png")
b_rootimage = b_root.subsample(10,10)
b_root = Button(root, text="AC", fg="black", image=b_rootimage, bg="black", command= lambda: sqrt('math.sqrt(')
               ).grid(row=3, column=3)

b_7 = PhotoImage(file = "7.png")
b_7image = b_7.subsample(10,10)
b_7 = Button(root, text="AC", fg="black", image=b_7image, bg="black",command= lambda: ins_num(7)
               ).grid(row=1, column=4)
b_8 = PhotoImage(file = "8.png")
b_8image = b_8.subsample(10,10)
b_8 = Button(root, text="AC", fg="black", image=b_8image, bg="black",command= lambda: ins_num(8)
               ).grid(row=1, column=5)
b_9 = PhotoImage(file = "9.png")
b_9image = b_9.subsample(10,10)
b_9 = Button(root, text="AC", fg="black", image=b_9image, bg="black",command= lambda: ins_num(9)
               ).grid(row=1, column=6)

b_4 = PhotoImage(file = "4.png")
b_4image = b_4.subsample(10,10)
b_4 = Button(root, text="AC", fg="black", image=b_4image, bg="black",command= lambda: ins_num(4)
               ).grid(row=2, column=4)
b_5 = PhotoImage(file = "5.png")
b_5image = b_5.subsample(10,10)
b_5 = Button(root, text="AC", fg="black", image=b_5image, bg="black",command= lambda: ins_num(5)
               ).grid(row=2, column=5)
b_6 = PhotoImage(file = "6.png")
b_6image = b_6.subsample(10,10)
b_6 = Button(root, text="AC", fg="black", image=b_6image, bg="black",command= lambda: ins_num(6)
               ).grid(row=2, column=6)

b_1 = PhotoImage(file = "1.png")
b_1image = b_1.subsample(10,10)
b_1 = Button(root, text="AC", fg="black", image=b_1image, bg="black",command= lambda: ins_num(1)
               ).grid(row=3, column=4)
b_2 = PhotoImage(file = "2.png")
b_2image = b_2.subsample(10,10)
b_2 = Button(root, text="AC", fg="black", image=b_2image, bg="black",command= lambda: ins_num(2)
               ).grid(row=3, column=5)
b_3 = PhotoImage(file = "3.png")
b_3image = b_3.subsample(10,10)
b_3 = Button(root, text="AC", fg="black", image=b_3image, bg="black",command= lambda: ins_num(3)
               ).grid(row=3, column=6 )

b_equal = PhotoImage(file = "=.png")
b_equalimage = b_equal.subsample(6,6)
b_equal = Button(root, text="AC", fg="black", image=b_equalimage, bg="black", command =evaluate
               ).grid(row=4, column=6 ,rowspan= 2)



b_plus = PhotoImage(file = "plus.png")
b_plusimage = b_plus.subsample(10,10)
b_plus = Button(root, text="AC", fg="black", image=b_plusimage, bg="black", command= lambda: ins_num('+')
               ).grid(row=4, column=4)
b_minus = PhotoImage(file = "minus.png")
b_minusimage = b_minus.subsample(10,10)
b_minus = Button(root, text="AC", fg="black", image=b_minusimage, bg="black", command= lambda: ins_num('-')
               ).grid(row=4, column=5)
b_multiply = PhotoImage(file = "mul.png")
b_multiplyimage = b_multiply.subsample(10,10)
b_multiply= Button(root, text="AC", fg="black", image=b_multiplyimage, bg="black", command= lambda: ins_num('*')
               ).grid(row=5, column=4)
b_division = PhotoImage(file = "div.PNG")
b_divisionimage = b_division.subsample(10,10)
b_division = Button(root, text="AC", fg="black", image=b_divisionimage, bg="black", command= lambda: ins_num('/')
               ).grid(row=5, column=5)

b_0 = PhotoImage(file = "zero.PNG")
b_0image = b_0.subsample(9,6)
b_0 = Button(root, text="AC", fg="black", image=b_0image, bg="black",command= lambda: ins_num(0)
               ).grid(row=4, column=2,columnspan= 2)
ce = PhotoImage(file = "ce.PNG")
ceimage = ce.subsample(7,10)
ce = Button(root, text="AC", fg="black", image=ceimage, bg="black",command = clear
               ).grid(row=4, column=0,columnspan= 2)
dot = PhotoImage(file = "dot.PNG")
dotimage = dot.subsample(12,8)
dot = Button(root, text="AC", fg="black", image=dotimage, bg="black", command= lambda: ins_num('.')
               ).grid(row=5, column=3,columnspan= 1)

b_sininv = PhotoImage(file = "sininv.png")
b_sininvimage = b_sininv.subsample(11,11)
b_sininv = Button(root, text="AC", fg="black", image=b_sininvimage, bg="black", command= lambda: arcsin('math.asin(')
               ).grid(row=5, column=0,rowspan=1)

b_cosinv = PhotoImage(file = "cosinv.png")
b_cosinvimage = b_cosinv.subsample(11,11)
b_cosinv = Button(root, text="AC", fg="black", image=b_cosinvimage, bg="black", command= lambda: arccos('math.acos(')
               ).grid(row=5, column=1,rowspan=1)

b_taninv = PhotoImage(file = "taninv.png")
b_taninvimage = b_taninv.subsample(11,11)
b_taninv = Button(root, text="AC", fg="black", image=b_taninvimage, bg="black", command= lambda: arctan('math.atan(')
               ).grid(row=5, column=2,rowspan=1)

root.rowconfigure((0,1), weight=1)
root.columnconfigure((0,2), weight=1)

mainloop()
