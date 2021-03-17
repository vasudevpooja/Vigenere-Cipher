from tkinter import *
import random
import time
import datetime
root=Tk()
root.geometry("1920x1080")
Tops=Frame(root,width=1600,relief=SUNKEN)
Tops.pack(side=TOP)
f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
localtime=time.asctime(time.localtime(time.time()))
lblInfo=Label(Tops,font=('Lucida Calligraphy',40,'bold'),text="Vigenère Cipher",fg="dark blue",bd=40,anchor='n')
lblInfo.grid(row=0,column = 0)
lblInfo=Label(Tops,font=('Algerian',20,'bold'),text=localtime,fg="deep sky blue",bd=20,anchor='n')
lblInfo.grid(row=1,column=0)
name=StringVar()
text=StringVar()
shift=StringVar()
eord=StringVar()
Leave=StringVar()
def qExit():
    root.destroy()
def Reset():
    name.set("")
    text.set("")
    shift.set("")
    eord.set("")
    Leave.set("")
lblReference=Label(f1,font=('Elephant',16,'bold'),text="SENDER/RECEIVER'S NAME:",bd=16,anchor="w")
lblReference.grid(row =0,column=0)
txtReference=Entry(f1,font=('Times New Roman',20,'bold'),textvariable=name,bd=8,insertwidth=4,bg="medium purple",justify='left')
txtReference.grid(row=0,column=1)
lbltext=Label(f1,font=('Elephant',16,'bold'),text="MESSAGE TO BE SENT:",bd=16,anchor="w")
lbltext.grid(row=1,column=0)
txttext=Entry(f1,font=('Times New Roman',20,'bold'),textvariable=text,bd=8,insertwidth=4,bg="light goldenrod",justify='left')
txttext.grid(row=1,column=1)
lblshift=Label(f1,font=('Elephant',16,'bold'),text = "SHIFTED BY:", bd = 16, anchor = "w")
lblshift.grid(row=2,column = 0)
txtshift=Entry(f1,font=('Times New Roman',20,'bold'),textvariable=shift,bd=8,insertwidth=4,bg ="medium purple",justify='left')
txtshift.grid(row = 2, column = 1)
lbleord=Label(f1,font=('Elephant',16,'bold'),text="CHOOSE (E/D):",bd=16,anchor="w")
lbleord.grid(row=3,column=0)
txteord=Entry(f1,font=('Times New Roman',20,'bold'),textvariable=eord,bd=8,insertwidth=4,bg="light goldenrod",justify='left')
txteord.grid(row=3,column=1)
lblService=Label(f1,font=('Elephant',16,'bold'),text="AFTER (E/D):",bd=16,anchor="w")
lblService.grid(row=4,column=0)
txtService=Entry(f1,font=('Times New Roman',20,'bold'),textvariable=Leave,bd=8,insertwidth=4,bg="medium purple",justify='left')
txtService.grid(row =4,column=1)
import base64
def encode(shift,clear):
    e=[]
    for i in range(len(clear)):
        shift_c=shift[i%len(shift)]
        e_c=chr((ord(clear[i]) +ord(shift_c))%256)
        e.append(e_c)
    return base64.urlsafe_b64encode("".join(e).encode()).decode()
def decode(shift,e):
    dec=[]
    e=base64.urlsafe_b64decode(e).decode()
    for i in range(len(e)):
        shift_c=shift[i%len(shift)]
        dec_c=chr((256+ord(e[i])-ord(shift_c))%256)
        dec.append(dec_c)
    return"".join(dec)
def Ref():
    print("Message=",(text.get()))
    clear=text.get()
    k=shift.get()
    m=eord.get()
    if (m=='e'):
        Leave.set(encode(k,clear))
    else:
        Leave.set(decode(k,clear))
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('Elephant',12,'bold'),width=10,text="E/D:",bg="light sky blue",command=Ref).grid(row=0,column=6)
btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('Elephant',12,'bold'),width=10,text="E/D NEW",bg="light green",command=Reset).grid(row=2,column=5)
btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('Elephant',12,'bold'),width=10,text="LEAVE",bg="coral",command=qExit).grid(row=4,column=4)
root.mainloop()
