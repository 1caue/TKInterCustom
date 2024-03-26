from customtkinter import *
from time import sleep
from tkinter import messagebox

app = CTk(fg_color='#D3D3D3')
app.geometry('320x180')
app.title('Cronômetro')

# Def
def cron():
        global s, m, h
        s += 1
        if s >= 60:
            m += 1
            s = 0
            if m >= 60:
                h += 1
                m = 0
                if h >= 99:
                    return
                lbl1.configure(text=f'{h:02}')
            lbl2.configure(text=f':{m:02}')
        lbl3.configure(text=f':{s:02}')
        lbl3.after(1000, cron)  

def start_cron():
    global stop_flag
    stop_flag = True
    cron()

def stop():
    global stop_flag
    stop_flag = False

# Butons
bt1 = CTkButton(app, text='Comecar', fg_color='#8C8C8C', hover_color='#272727', border_color='black', width=100, border_width=1, command=start_cron)
bt1.place(relx=0.01, rely=0.8)

bt2 = CTkButton(app, text='Parar', fg_color='#8C8C8C', hover_color='red', border_color='black', width=104, border_width=1, command=stop)
bt2.place(relx=0.34, rely=0.8) 

bt3 = CTkButton(app, text='Recomeçar', fg_color='#8C8C8C', hover_color='#272727', border_color='black', width=100, border_width=1, command=start_cron)
bt3.place(relx=0.68, rely=0.8)

# Labels
lbl1 = CTkLabel(app, text='00', text_color='black', font=('Arial', 50))
lbl1.place(relx=0.19, rely=0.3)

lbl2 = CTkLabel(app, text=':00', text_color='black', font=('Arial', 50))
lbl2.place(relx=0.36, rely=0.3)

lbl3 = CTkLabel(app, text=':00', text_color='black', font=('Arial', 50))
lbl3.place(relx=0.58, rely=0.3)

stop_flag = True

s = 0
m = 0
h = 0

app.mainloop()