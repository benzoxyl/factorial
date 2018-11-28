from tkinter import Tk, Label, Button, Entry, mainloop

def fakultaet(n):
    global result
    result = 1
    
    if n == 0:
        return 1
    
    for i in range(1,n+1):
        result *= i
    return result

def getFakultaet():
    try:
        n = int(e1.get())
    except:
        print("Error")
    resultLabel['text'] = str(fakultaet(n))
    
    
master = Tk()
Label(master, text="The factorial of").grid(column=0, row=0)
e1 = Entry(master)
e1.grid(column=1, row=0)
Label(master, text="is:").grid(column=2, row=0)
resultLabel = Label(master)
resultLabel.grid(column=3, row=0)
Button(master, text="Calculate!", command=getFakultaet).grid(column=0, row=1)

mainloop()
