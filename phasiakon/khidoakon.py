from tkinter import * 

N = Tk() #ສະເເດງໜ້າ GUI ຂື້ນມາ
N.geometry('1000x1000') # ຂະໜາດຂອງGUI
N.title('ໂປຣເເກຣມຄຳນວນເກັບຄ່າພາສີ001') # ຊື່ໂປຣເເກຣມ


###########Font ທັ້ງໝົດ #############
FONT1 = ('Phetsarath OT',20)
ຟື້ນຫຼັງ = PhotoImage(file='unclemedia.png').subsample(2)
p = Label(N, image=ຟື້ນຫຼັງ)
p.pack(pady=20)
############# ຊ່ອງກອກຂໍ້ມູນ #######################
L = Label(N,text='ຊື່ສີນຄ້າ',font=FONT1).pack() #ສະເເດງຂໍ້ຄວາມ
n_ຊື່ສີນຄ້າ =StringVar() # ຕົວເເປສຳຫຼັບເກັບລາຄາສີນຄ້າຕອນພີມ
U1 = Entry(N,textvariable=n_ຊື່ສີນຄ້າ,font=FONT1)
U1.pack()

L = Label(N,text='ລາຄາສີນຄ້າ',font=FONT1).pack() #ສະເເດງຂໍ້ຄວາມ
n_ລາຄາສີນຄ້າ =StringVar() 
U2 = Entry(N,textvariable=n_ລາຄາສີນຄ້າ,font=FONT1)
U2.pack()

L = Label(N,text='ຈຳນວນສີນຄ້າ',font=FONT1).pack() #ສະເເດງຂໍ້ຄວາມ
n_ຈຳນວນສີນຄ້າ =StringVar()
U3 = Entry(N,textvariable=n_ຈຳນວນສີນຄ້າ,font=FONT1)
U3.pack()


######### ເລືອກປະເພດເກັບພາສີ ##########
A1 = Frame(N)
A1.pack(pady=10)

s_ປະເພດ = StringVar()

R1 = Radiobutton(A1,text='ລາຄາລວມ ພາສີ ເເລ້ວ',variable=s_ປະເພດ,value='ic')
R1.grid(row=0,column=0)

R1.invoke() #เลือกเป็นค่าเริ่มต้น

R2 = Radiobutton(A1,text='ລາຄາ + ພາສີ 7%',variable=s_ປະເພດ,value='av')
R2.grid(row=0,column=1)

R3 = Radiobutton(A1,text='ບໍ່ລວມພາສີ',variable=s_ປະເພດ,value='nic')
R3.grid(row=0,column=2)


def unclemedia(event=None): # ຄື funtion ການຄຳນວນ
	# print(type(int( n_ຕົວເເປ.get())))
	#price = int(n_ຕົວເເປ.get()) * int(n_ຈຳນວນສີນຄ້າ.get()) #int ຄືຄຳສັ່ງເເປງຂໍ້ຄວາມເປັນຕົວເລກ'2'- - > 2
	ສີນຄ້າ = (n_ຊື່ສີນຄ້າ.get())
	ລາຄາ = int(n_ລາຄາສີນຄ້າ.get())
	ຈຳນວນ = int(n_ຈຳນວນສີນຄ້າ.get())
	ລວມ = ລາຄາ * ຈຳນວນ
	#print('ລາຄາ',ລາຄາ)
	#ພາສີ7 = ລວມ * (7/107)
	#ລາຄາລວມພາສີເເລ້ວ = ລວມ * (100/107)

	#print('ລາຄາກ່ອນ ພາສີ7: {:.2f} (ພາສີ7%:{:.2f})'.format(ລາຄາລວມພາສີເເລ້ວ,ພາສີ7))
	if s_ປະເພດ.get() == 'ic':
		ພາສີ7 = ລວມ * (7/107)
		ລາຄາລວມພາສີເເລ້ວ = ລວມ * (100/107)
		n_ຜົນລັບ.set('ສີນຄ້າ:{} ຈຳນວນ {} ຊີ້ນ ທັ້ງໝົດ {} ກີບ ({} ກີບ/ຊີ້ນ\nລາຄາສີນຄ້າ:{:.2f}).-ພາສີ7%: {:.2f}.-'.format(ສີນຄ້າ,ຈຳນວນ,ລວມ,ລາຄາ,ລາຄາລວມພາສີເເລ້ວ,ພາສີ7))

	elif s_ປະເພດ.get() == 'av':
		ພາສີ7 = (ລວມ * (7/100))
		ລາຄາລວມພາສີເເລ້ວ = ລວມ
		ບວກລວມ = ລວມ + ພາສີ7
		n_ຜົນລັບ.set('ສີນຄ້າ: {} ຈຳນວນ {} ຊີ້ນ ທັ້ງໝົດ {:.2f} ກີບ ({:.2f} ກີບ/ຊີ້ນ)\nລາຄາສີນຄ້າ: {:.2f}.- ພາສີ7%: {:.2f}.-'.format(ສີນຄ້າ,ຈຳນວນ,ບວກລວມ,ລາຄາ + (ພາສີ7 / ຈຳນວນ),ລາຄາລວມພາສີເເລ້ວ,ພາສີ7))
	else:
		n_ຜົນລັບ.set('ສີນຄ້າ: {} ຈຳນວນ {} ຊີ້ນ ທັ້ງໝົດ {:.2f} ກີບ ({:.2f} ກີບ/ຊີ້ນ)\n'.format(ສີນຄ້າ,ຈຳນວນ,ລວມ,ລາຄາ))






################### ປຸ່ມກົດເພືອຄຳນວນ ###############
B1 = Button(N,text='ຄຳນວນ',command=unclemedia)
B1.pack(ipadx=20,ipady=10,pady=10)

U3.bind('<Return>',unclemedia) # Return ເເລະ eventຄືການເຊືອມຕໍ່Enter None ຄືເພືອໃຫ້ສາມາດທຳງານໄດ້ທັ້ງສອງ 
########### ຜົນລັບຈາກການຄຳນວນ ##################
n_ຜົນລັບ = StringVar()
n_ຜົນລັບ.set('<<ຜົນລັບຈາກການຄຳນວນ>>')
H1 = Label(N,textvariable=n_ຜົນລັບ)


E1 = Label(N,textvariable=n_ຜົນລັບ,font=FONT1)
E1.pack()

N.mainloop()
