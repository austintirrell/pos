#PPPPOS
from tkinter import *

#delivery or no?
delivery = False

#global variables
cust_name = ''
cust_phone = ''
cust_address = ''

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
  nameAndNumber = Tk()
  nameAndNumber.title('PPPPOS Customer Info')
  nameAndNumber.configure(bg='red')
  nameAndNumber.geometry('1920x1080')

  #name input
  Label (nameAndNumber, text='Name:', bg='red', fg='black', font='none 32') .place(relx=0.5, rely=0.2, anchor=CENTER)
  name = Text(nameAndNumber, width=50, height=2, bg='white', fg='black', font='none 32')
  name.place(relx=0.5, rely=0.3, anchor=CENTER)

  #phone input
  Label (nameAndNumber, text='Phone:', bg='red', fg='black', font='none 32') .place(relx=0.5, rely=0.4, anchor=CENTER)
  phone = Text(nameAndNumber, width=50, height=2, bg='white', fg='black', font='none 32')
  phone.place(relx=0.5, rely=0.5, anchor=CENTER)

  #if delivery is selected, add address box
  if delivery == True:
    Label (nameAndNumber, text='Address:', bg='red', fg='black', font='none 32') .place(relx=0.5, rely=0.6, anchor=CENTER)
    address = Text(nameAndNumber, width=50, height=2, bg='white', fg='black', font='none 32')
    address.place(relx=0.5, rely=0.7, anchor=CENTER)

  #submit button
  Button (nameAndNumber, text='SUBMIT', bg='white', fg='black', font='none 32 bold', height=2) .place(relx=0.5, rely=0.85, anchor=CENTER)

  #run windows
  nameAndNumber.mainloop()

#carry-out or deliery window
start = Tk()
start.title('PPPPOS')
start.configure(bg='red')
start.geometry('1920x1080')

#carryout button
carryOutButton = Button(start, command=toCustomerInfo, text='CARRYOUT', font='none 32 bold', bg='white', fg='black', height=5) 
carryOutButton.place(relx=0.35, rely=0.5, anchor=CENTER)

#delivery button
deliveryButton = Button(start, command=toDelivery, text='DELIVERY', font='none 32 bold', bg='white', fg='black', height=5) 
deliveryButton.place(relx=0.65, rely=0.5, anchor=CENTER)

#run window
start.mainloop()