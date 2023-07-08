import cv2
import string
import os
from tkinter import *
import tkinter as tk

window=tk.Tk()
window.title("project")
window.geometry("1000x1000")
window.configure(background="green")
lbl=tk.Label(window,text="IMAGE STEGNOGRAPHY...",width=25,height=1,fg="white",bg="red",font=("times",15))
lbl.place(x=200,y=200)

def encryption():
    window=tk.Tk()
    window.title("project")
    window.geometry("1000x1000")
    window.configure(background="green")
    lbl=tk.Label(window,text="ENTER THE SECURITY KEY :",width=25,height=1,fg="white",bg="red",font=("times",15))
    lbl.place(x=200,y=200)
    lbl=tk.Label(window,text="ENTER THE TEXT TO HIDE :",width=25,height=1,fg="white",bg="red",font=("times",15))
    lbl.place(x=200,y=300)
    txt=tk.Entry(window,width=15,fg="white",bg="red",font=("times",15))
    txt.place(x=500,y=200)
    txt1=tk.Entry(window,width=15,fg="white",bg="red",font=("times",15))
    txt1.place(x=500,y=300)
    def submit():
        global key,text,c,x,n,m,z,d,k1
        key=txt.get()
        text=txt1.get()
        d={}
        c={}

        for i in range(255):
            d[chr(i)]=i
            c[i]=chr(i)
            
        x=cv2.imread("pic.jpeg")

        i=x.shape[0]
        j=x.shape[1]
        print(i,j)
        kl=0
        tln=len(text)
        z=0 #decides plane
        n=0 #number of row
        m=0 #number of column
        global l
        l=len(text)

        for i in range(l):
            x[n,m,z]=d[text[i]]^d[key[kl]]
            n=n+1
            m=m+1
            m=(m+1)%3 #this is for every value of z , remainder will be between 0,1,2 . i.e G,R,B plane will be set automatically.
                        #whatever be the value of z , z=(z+1)%3 will always between 0,1,2 . The same concept is used for random number in dice and card games.
            kl=(kl+1)%len(key)
            
        cv2.imwrite("encrypted_img.jpg",x)
        cv2.imshow("encrypted_img",x)
##        os.startfile("encrypted_img.jpg")
        print("Data Hiding in Image completed successfully.")
    #x=cv2.imread(“encrypted_img.jpg")
    btn=tk.Button(window,text="submit",command=submit,width=10,height=1,fg="white",bg="red",font=("times",15))
    btn.place(x=200,y=500)
    btn=tk.Button(window,text="quit",command=window.destroy,width=10,height=1,fg="white",bg="red",font=("times",15))
    btn.place(x=300,y=500)
def decryption():        
    window=tk.Tk()
    window.title("project")
    window.geometry("1000x1000")
    window.configure(background="green")
    lbl=tk.Label(window,text="ENTER THE SECURITY KEY\n TO EXTRACT THE TEXT :",width=25,height=2,fg="white",bg="red",font=("times",15))
    lbl.place(x=200,y=200)
    txt2=tk.Entry(window,width=15,fg="white",bg="red",font=("times",15))
    txt2.place(x=500,y=200)
    
    global text
    tln=len(text)

##    ch = int(input("\nEnter 1 to extract data from Image : "))
##
##    if ch == 1:
    def submit():
        key1=txt2.get()
##        key1=input("\n\nRe enter key to extract text : ")
        decrypt=""
        global key
        if key == key1 :
            global l,n,m,z,d,c,k1
            kl=0
            z=0 #decides plane
            n=0 #number of row
            m=0 #number of column
            for i in range(l):
                decrypt+=c[x[n,m,z]^d[key[kl]]]
                n=n+1
                m=m+1
                m=(m+1)%3
                kl=(kl+1)%len(key)
            print("Encrypted text was : ",decrypt)
            lbl=tk.Label(window,text="THE DECRYPTED TEXT :"+ decrypt,width=40,height=2,fg="white",bg="red",font=("times",15))
            lbl.place(x=200,y=600)
            cv2.imshow("decrypted_img",x)
        else:
            print("Key doesn't matched.")
            lbl=tk.Label(window,text="KEY DOES'NT MATCHED....",width=25,height=2,fg="white",bg="red",font=("times",15))
            lbl.place(x=200,y=600)
            
    btn=tk.Button(window,text="submit",command=submit,width=10,height=1,fg="white",bg="red",font=("times",15))
    btn.place(x=200,y=500)
    btn=tk.Button(window,text="quit",command=window.destroy,width=10,height=1,fg="white",bg="red",font=("times",15))
    btn.place(x=300,y=500)
    btn=tk.Button(window,text="encryption",command=encryption,width=10,height=1,fg="white",bg="red",font=("times",15))
    btn.place(x=200,y=400)
    btn=tk.Button(window,text="decryption",command=decryption,width=10,height=1,fg="white",bg="red",font=("times",15))
    btn.place(x=200,y=500)
    btn=tk.Button(window,text="quit",command=window.destroy,width=10,height=1,fg="white",bg="red",font=("times",15))
    btn.place(x=300,y=600)
    window.mainloop()   
