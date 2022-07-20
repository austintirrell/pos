#PPPPOS
from tkinter import *

#delivery or no?
delivery = False

#global variables
cust_name = ''
cust_phone = ''
cust_address = ''

#order screen
def toOrder():
  global delivery
  global food
  food = 0.00

  #order window
  orderWindow = Tk()
  orderWindow.title('PPPPOS Order')
  orderWindow.configure(bg='red')
  orderWindow.geometry('1920x1080')

  def addCheese():
    global food
    food += 5.00
    order.insert(END, 'Cheese: 5.00' + '\n')
    display()

  def addPepperoni():
    global food
    food += 7.50
    order.insert(END, 'Pepperoni: 7.50' + '\n')
    display()
  
  def addSausage():
    global food
    food += 7.50
    order.insert(END, 'Sausage: 7.50' + '\n')
    display()
  
  def addSupreme():
    global food
    food += 10.00
    order.insert(END, 'Supreme: 10.00' + '\n')
    display()
  
  def display():
    global food
    global charge
    global total

    if delivery == True:
      charge = 4.00
    elif delivery == False:
      charge = 0.00

    tax = (food + charge) * 0.07
    total = food + charge + tax

    totalDisplay.delete('1.0', END)
    totalDisplay.insert(END, 'Food: ' + "{:.2f}".format(food) + '\n')
    if delivery == True:
      totalDisplay.insert(END, 'Delivery: ' + "{:.2f}".format(charge) + '\n')
    totalDisplay.insert(END, 'Tax: ' + "{:.2f}".format(tax) + '\n')
    totalDisplay.insert(END, 'Total: ' + "{:.2f}".format(total))

  order = Text(orderWindow, width=20, height=10, bg='white', fg='black', font='none 32')
  order.place(relx=0.7, rely=0.3, anchor=CENTER)

  totalDisplay = Text(orderWindow, width=20, height=4, bg='white', fg='black', font='none 32')
  totalDisplay.place(relx=0.7, rely=0.70, anchor=CENTER)

  Button (orderWindow, command=addCheese, text='Cheese', bg='white', fg='black', font='none 32 bold', width=10, height=2) .place(relx=0.3, rely=0.2, anchor=CENTER)
  Button (orderWindow, command=addPepperoni, text='Pepperoni', bg='white', fg='black', font='none 32 bold', width=10, height=2) .place(relx=0.3, rely=0.35, anchor=CENTER)
  Button (orderWindow, command=addSausage, text='Sausage', bg='white', fg='black', font='none 32 bold', width=10, height=2) .place(relx=0.3, rely=0.5, anchor=CENTER)
  Button (orderWindow, command=addSupreme, text='Supreme', bg='white', fg='black', font='none 32 bold', width=10, height=2) .place(relx=0.3, rely=0.65, anchor=CENTER)
  Button (orderWindow, text='Finish', bg='white', fg='black', font='none 32 bold', width=40, height=2) .place(relx=0.5, rely=0.9, anchor=CENTER)

  display()

#if delivery is clicked
def toDelivery():
  global delivery
  delivery = True
  toCustomerInfo()

#customer info window
def toCustomerInfo():
  global delivery
  global cust_address

  if delivery == False:
    cust_address = 'CARRYOUT'

  #window for name and number
  custInfoWindow = Tk()
  custInfoWindow.title('PPPPOS Customer Info')
  custInfoWindow.configure(bg='red')
  custInfoWindow.geometry('1920x1080')

  #name input
  Label (custInfoWindow, text='Name:', bg='red', fg='black', font='none 32') .place(relx=0.5, rely=0.2, anchor=CENTER)
  name = Text(custInfoWindow, width=50, height=2, bg='white', fg='black', font='none 32')
  name.place(relx=0.5, rely=0.3, anchor=CENTER)

  #phone input
  Label (custInfoWindow, text='Phone:', bg='red', fg='black', font='none 32') .place(relx=0.5, rely=0.4, anchor=CENTER)
  phone = Text(custInfoWindow, width=50, height=2, bg='white', fg='black', font='none 32')
  phone.place(relx=0.5, rely=0.5, anchor=CENTER)

  #if delivery is selected, add address box
  if delivery == True:
    Label (custInfoWindow, text='Address:', bg='red', fg='black', font='none 32') .place(relx=0.5, rely=0.6, anchor=CENTER)
    address = Text(custInfoWindow, width=50, height=2, bg='white', fg='black', font='none 32')
    address.place(relx=0.5, rely=0.7, anchor=CENTER)

  #submit button
  Button (custInfoWindow, command=toOrder, text='SUBMIT', bg='white', fg='black', font='none 32 bold', height=2) .place(relx=0.5, rely=0.85, anchor=CENTER)

  #run windows
  custInfoWindow.mainloop()

#carry-out or deliery window
root = Tk()
root.title('PPPPOS')
root.configure(bg='red')
root.geometry('1920x1080')

#carryout button
carryOutButton = Button(root, command=toCustomerInfo, text='CARRYOUT', font='none 32 bold', bg='white', fg='black', height=5) 
carryOutButton.place(relx=0.35, rely=0.5, anchor=CENTER)

#delivery button
deliveryButton = Button(root, command=toDelivery, text='DELIVERY', font='none 32 bold', bg='white', fg='black', height=5) 
deliveryButton.place(relx=0.65, rely=0.5, anchor=CENTER)

#run window
root.mainloop()