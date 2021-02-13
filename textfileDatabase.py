
# Roll # SE-056
from tkinter import *
main_window = Tk()
var1 = StringVar()
str1 = StringVar()


def number():
    n = int(msgentry.get())
    fact = factorial(n)
    checked = checker(n)

    str1 = "Factorial of " + str(n) + " is " + str(fact)
    var1 = str(checked)
    # output_label.configure(text=str1)



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def checker(n):

    if (n % 2) == 0:
       return n
    else:
       return n




main_window.title("Question6")
message_label = Label(text=' Enter no',
                      bg = 'red',
                      font=(' Verdana ', 12))
output_label = Label(text='Result',
                      bg = 'red',
                      font=(' Verdana ', 12)
                     )
msgentry = Entry(font=(' Verdana ', 12), width=50)
outputentry = Entry(font=(' Verdana ', 12), width=50, textvariable=str1)

calc_fact = Button(text=' Calculate Factorial ', font=(' Verdana ', 12),
                     command=number)
check = Button(text=' Check Even or odd', font=(' Verdana ', 12), command=lambda: checker)

message_label.grid(row=0, column=0, padx=10, pady=10)
msgentry.grid(row=0, column=1, padx=10, pady=10, ipady=10)
outputentry.grid(row=1, column=1, padx=10, ipady=20)
calc_fact.grid(row=2, column=1, padx=10, pady=10)
output_label.grid(row=1, column=0,  padx=10, pady=10)
check.grid(row=3, column=1, padx=10, pady=10)

mainloop()
