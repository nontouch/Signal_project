from tkinter import*
import time
import datetime
import pygame
from sound_generate_signal import*

wave_obj = None

def Key_sine_wave() :
    btnCs["state"] = "disabled"
    btnCsq["state"] = "normal"
    btnCt["state"] = "normal"
    btnCsaw["state"] = "normal"
    wave_obj = play(sps=44100 , freq_hz=440.00, duration_s=5, atten=0.3, wave_type= 'sine')
def Key_square_wave() :
    btnCs["state"] = "normal"
    btnCsq["state"] = "disabled"
    btnCt["state"] = "normal"
    btnCsaw["state"] = "normal"
    wave_obj = play(sps=44100 , freq_hz=440.00, duration_s=5, atten=0.3, wave_type= "squ")
def Key_triangle_wave() :
    btnCs["state"] = "normal"
    btnCsq["state"] = "normal"
    btnCt["state"] = "disabled"
    btnCsaw["state"] = "normal"
    wave_obj = play(sps=44100 , freq_hz=440.00, duration_s=5, atten=0.3, wave_type= "tri")
def Key_sawtooth_wave() :
    btnCs["state"] = "normal"
    btnCsq["state"] = "normal"
    btnCt["state"] = "normal"
    btnCsaw["state"] = "disabled"
    wave_obj = play(sps=44100 , freq_hz=440.00, duration_s=5, atten=0.3, wave_type= "saw")
def type_c() :
    if wave_obj == None :
        pass
    else :
        wave_obj.play_sound('C')
def type_d() :
    pass
def type_e() :
    pass
def type_f() :
    pass
def type_g() :
    pass
def type_a() :
    pass
def type_b() :
    pass

pygame.init()
root = Tk()
root.title("Music Box")
root.geometry('1352x700+0+0')
root.configure(background = 'white')

ABC =Frame(root, bg="powder blue", bd=20, relief= RIDGE)
ABC.grid()

ABC1 =Frame(ABC, bg="powder blue", bd=20, relief= RIDGE)
ABC1.grid()
ABC2 =Frame(ABC, bg="powder blue", bd=20, relief= RIDGE)
ABC2.grid()
ABC3 =Frame(ABC, bg="powder blue", bd=20, relief= RIDGE)
ABC3.grid()

str1 = StringVar()
str1.set("Ject Like Music")
Data1 = StringVar()
Time1=StringVar()

Data1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S"))
#============================Label with title =====================
Label(ABC1, text="Synthesizer",font=('arial',25,'bold'),padx=8,pady=8,bd=4,bg="powder blue",
fg="white").grid(row=0,column=0,columnspan=11)

C = Canvas(ABC1, height=200, width=200, bg = 'white' )
C.grid(row=1,column=2)

#==================================================================
#txtDate=Entry(ABC1, textvariable=Data1, font=('arial',18,'bold'),bd=34,bg="powder blue",
#fg="white",width=28,justify=CENTER).grid(row=1,column=0,columnspan=1)

#txtDate=Entry(ABC1, textvariable=str1, font=('arial',18,'bold'),bd=34,bg="powder blue",
#fg="white",width=28,justify=CENTER).grid(row=1,column=1,columnspan=1)

#txtDate=Entry(ABC1, textvariable=Time1, font=('arial',18,'bold'),bd=34,bg="powder blue",
#fg="white",width=28,justify=CENTER).grid(row=1,column=2,columnspan=1)
btnCr=Button(ABC, height=2, width=4,bd=4, text="Rec", font=('arial',18,'bold'),bg="black",fg="white")
btnCr.grid(row=0,column=1,padx=5,pady=5)

btnCs=Button(ABC1, height=2, width=6,bd=4, text="sin", font=('arial',18,'bold'),bg="black",fg="white", command= Key_sine_wave )
btnCs.grid(row=1,column=4,padx=5,pady=5)

btnCsq=Button(ABC1, height=2, width=6,bd=4, text="square", font=('arial',18,'bold'),bg="black",fg="white", command= Key_square_wave)
btnCsq.grid(row=1,column=5,padx=5,pady=5)

btnCt=Button(ABC1, height=2, width=6,bd=4, text="Triangle", font=('arial',18,'bold'),bg="black",fg="white", command= Key_triangle_wave)
btnCt.grid(row=1,column=6,padx=5,pady=5)

btnCsaw=Button(ABC1, height=2, width=7,bd=4, text="sawtooth", font=('arial',18,'bold'),bg="black",fg="white", command= Key_sawtooth_wave)
btnCsaw.grid(row=1,column=7,padx=5,pady=5)

btnCst1=Button(ABC1, height=2, width=4,bd=4, text="Style1", font=('arial',18,'bold'),bg="black",fg="white")
btnCst1.grid(row=2,column=4,padx=5,pady=5)

btnCst2=Button(ABC1, height=2, width=4,bd=4, text="Style2", font=('arial',18,'bold'),bg="black",fg="white")
btnCst2.grid(row=2,column=5,padx=5,pady=5)

btnCst3=Button(ABC1, height=2, width=4,bd=4, text="Style3", font=('arial',18,'bold'),bg="black",fg="white")
btnCst3.grid(row=2,column=6,padx=5,pady=5)

btnCst4=Button(ABC1, height=2, width=4,bd=4, text="Style4", font=('arial',18,'bold'),bg="black",fg="white")
btnCst4.grid(row=2,column=7,padx=5,pady=5)

#==============================Black Button===============================
btnC_=Button(ABC3, height=4, width=6,bd=4, text="C#", font=('arial',18,'bold'),bg="black",fg="white")
btnC_.grid(row=0,column=1,padx=5,pady=5)

btnDs=Button(ABC3, height=4, width=6,bd=4 , text="D#", font=('arial',18,'bold'),bg="black",fg="white")
btnDs.grid(row=0,column=2,padx=5,pady=5)
btnSpace=Button(ABC3, state=DISABLED, width=2,height=6 ,bg = "powder blue",relief=FLAT)
btnSpace.grid(row=0,column=3,padx=0,pady=0)
btnFs=Button(ABC3, height=4, width=6,bd=4 , text="F#", font=('arial',18,'bold'),bg="black",fg="white")
btnFs.grid(row=0,column=4,padx=5,pady=5)

btnGs=Button(ABC3, height=4, width=6,bd=4 , text="G#", font=('arial',18,'bold'),bg="black",fg="white")
btnGs.grid(row=0,column=5,padx=5,pady=5)
btnBb=Button(ABC3, height=4, width=6,bd=4 , text="Bb", font=('arial',18,'bold'),bg="black",fg="white")
btnBb.grid(row=0,column=6,padx=5,pady=5)

#===============================White button==========================
btnC=Button(ABC3, height=4, width=8, text="C", font=('arial',18,'bold'),bg="white",fg="black", command= type_c)
btnC.grid(row=1,column=0,padx=5,pady=5)
btnD=Button(ABC3, height=4, width=8, text="D", font=('arial',18,'bold'),bg="white",fg="black")
btnD.grid(row=1,column=1,padx=5,pady=5)
btnE=Button(ABC3, height=4, width=8, text="E", font=('arial',18,'bold'),bg="white",fg="black")
btnE.grid(row=1,column=2,padx=5,pady=5)
btnF=Button(ABC3, height=4, width=8, text="F", font=('arial',18,'bold'),bg="white",fg="black")
btnF.grid(row=1,column=3,padx=5,pady=5)

btnG=Button(ABC3, height=4, width=8, text="G", font=('arial',18,'bold'),bg="white",fg="black")
btnG.grid(row=1,column=4,padx=5,pady=5)
btnA=Button(ABC3, height=4, width=8, text="A", font=('arial',18,'bold'),bg="white",fg="black")
btnA.grid(row=1,column=5,padx=5,pady=5)
btnB=Button(ABC3, height=4, width=8, text="B", font=('arial',18,'bold'),bg="white",fg="black")
btnB.grid(row=1,column=6,padx=5,pady=5)

#==================================================================


root.mainloop()

#==================================================================

