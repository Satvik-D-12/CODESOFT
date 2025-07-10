from tkinter import *

def buttonClick(number):
    global operator
    operator = operator + str(number)
    input_value.set(operator)

def buttonClear():
    global operator
    operator = ""
    input_value.set("")

def buttonEqual():
    global operator
    result = str(eval(operator))
    input_value.set(result)
    operator = ""

def buttonBackspace():
    global operator
    operator = operator[:-1]
    input_value.set(operator)

main = Tk()
main.title("CALCULATOR")

operator = ""
input_value = StringVar()
display_text = Entry(main, font = ("arial",20,"bold"),textvariable=input_value,bd=30,insertwidth=4,bg="orange",justify=RIGHT)
display_text.grid(columnspan=4)

# Creating Buttons 

# Row 1

btn_1 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),bg="orange",text="1",command=lambda: buttonClick(1))
btn_1.grid(row=1,column=0,sticky="snew")

btn_2 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),bg="orange",text="2",command=lambda: buttonClick(2))
btn_2.grid(row=1,column=1,sticky="snew")

btn_3 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),bg="orange",text="3",command=lambda: buttonClick(3))
btn_3.grid(row=1,column=2,sticky="snew")

btn_back = Button(main,padx=16,pady=8,bd=8,fg="black",font=("arial",15,"bold"),bg="orange",text="⌫",command=buttonBackspace)
btn_back.grid(row=1,column=3,sticky="snew")

# Row 2

btn_4 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="4",command=lambda: buttonClick(4))
btn_4.grid(row=2,column=0,sticky="snew")

btn_5 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="5",command=lambda: buttonClick(5))
btn_5.grid(row=2,column=1,sticky="snew")

btn_6 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="6",command=lambda: buttonClick(6))
btn_6.grid(row=2,column=2,sticky="snew")

btn_add = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="+",command=lambda: buttonClick("+"))
btn_add.grid(row=2,column=3,sticky="snew")

# Row 3

btn_7 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="7",command=lambda: buttonClick(7))
btn_7.grid(row=3,column=0,sticky="snew")

btn_8 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="8",command=lambda: buttonClick(8))
btn_8.grid(row=3,column=1,sticky="snew")

btn_9 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="9",command=lambda: buttonClick(9))
btn_9.grid(row=3,column=2,sticky="snew")

btn_sub = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="-",command=lambda: buttonClick("-"))
btn_sub.grid(row=3,column=3,sticky="snew")

# Row 4 

btn_dec = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),bg="green",text=".",command=lambda: buttonClick("."))
btn_dec.grid(row=4,column=0,sticky="snew")

btn_0 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),bg="green",text="0",command=lambda: buttonClick(0))
btn_0.grid(row=4,column=1,sticky="snew")

btn_div = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),bg="green",text="/",command=lambda: buttonClick("/"))
btn_div.grid(row=4,column=2,sticky="snew")

btn_mul = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),bg="green",text="*",command=lambda: buttonClick("*"))
btn_mul.grid(row=4,column=3,sticky="snew")
 
# Row 5

btn_clear = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),bg="green",text="C",command=buttonClear)
btn_clear.grid(row=5,column=0,columnspan=2,sticky="snew")

btn_equal = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),bg="green",text="=",command=buttonEqual)
btn_equal.grid(row=5,column=2,columnspan=2,sticky="snew")

main.mainloop()