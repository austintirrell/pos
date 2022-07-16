#Celcius to Fahrenheit
from tkinter import *

#convert functions
def convertToC():
  f = int(input.get())
  output.delete(0.0, END)
  conversion = int((f - 32) * 5 / 9)
  output.insert(END, conversion)

def convertToF():
  c = int(input.get())
  output.delete(0.0, END)
  conversion = int(9 / 5 * c + 32)
  output.insert(END, conversion)

#main
window = Tk()
window.title('Celcius to Fahrenheit')
window.configure(background='#333333')

#create title label
Label (window, text='Celcius to Fahrenheit', bg='#333333', fg='#EEEEEE', font='none 20 bold') .grid(row=0, column=0, sticky=W)

#create tip label
Label (window, text='Enter value in Celcius, and submit to see conversion result to Fahrenheit', bg='#333333', fg='#EEEEEE', font='none 12', wraplength=300) .grid(row=1, column=0, sticky=W)

#create text entry box
input = Entry(window, width=20, bg='#EEEEEE', fg='#333333')
input.grid(row=2, column=0, sticky=W)

#convert button
Button(window, text='C to F', width=0, command=convertToF) .grid(row=3, column=0, sticky=W)
Button(window, text='F to C', width=0, command=convertToC) .grid(row=3, column=1, sticky=W)

#output label
output = Text(window, width=5, height=1, bg='#EEEEEE', fg='#333333', font='none 12 bold')
output.grid(row=4, column=0, sticky=W)

#run window
window.mainloop()