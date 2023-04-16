from tkinter import *
import os.path
from tkinter import filedialog
import pytesseract
from PIL import Image
from tkinter import messagebox

window1= Tk()   # widget deja defini
window1.geometry('560x450')
window1.title('Extract text from image and video')
window1.resizable(False,False)
window1.configure(bg='blue')
#-----------------------------------------------------------------------fonctions--------------------------------------------------------#
def imo():
    file=filedialog.askopenfile(mode='r',filetypes=[('PNG Files','*.png')])
    if file:
        filepath=os.path.abspath(file.name)
        En1.insert(0,filepath)
    
def ORC():
    pytesseract.pytesseract.tesseract_cmd= r"C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
    savo =En2.get()
    file =En1.get()
    lang=En3.get()
    img=Image.open(file)
    txt=pytesseract.image_to_string(img)
    with open(savo,"w") as f:
        f.write(txt)
    messagebox.showinfo('Driss','\n the file saved successfully.')

#-----------------------------------------------------tools--------------------------------------------------------------------#
f1=Frame(window1,width=600,height=368,bg='blue',bd=1,relief=SOLID)
f1.place(x=1,y=1)
#text=Label(f1,text='your image',font=('times for roman',13),fg='black',bg='white')
#text.place(x=1,y=4)

En1_text=Label(f1,text='image path',fg='black',bg='white',font=('times for roman',11))
En1_text.place(x=10,y=51)
En1=Entry(f1,font=('times for roman',16),width=30,bd=1,relief=SOLID)
En1.place(x=100,y=51)


btn1=Button(f1,text='+',cursor='hand2',command=imo)
btn1.place(x=445,y=51)


#En2_text=Label(f1,text='save path',fg='black',bg='white',font=('times for roman',11))
#En2_text.place(x=10,y=84)
#En2=Entry(f1,font=('times for roman',16),width=30,bd=1,relief=SOLID)
#En2.place(x=100,y=500)





En3_text=Label(f1,text='language',fg='black',bg='white',font=('times for roman',11))
En3_text.place(x=10,y=117)
En3=Entry(f1,font=('times for roman',16),width=30,bd=1,relief=SOLID)
En3.place(x=100,y=117)


b1=Button(f1,text='Extract text',width=10,height=6,fg='white',bg='#383838',cursor='hand2',command=ORC)
b1.place(x=470,y=49)




En2_text=Label(f1,text='save path',fg='black',bg='white',font=('times for roman',11))
En2_text.place(x=10,y=84)
En2=Entry(f1,font=('times for roman',16),width=30,bd=1,relief=SOLID)
En2.place(x=100,y=84)


images=PhotoImage(file='images.png')
logo_lbl=Label(window1,image=images)
logo_lbl.place(x=65,y=160)


window1.mainloop() # functioned windgget
