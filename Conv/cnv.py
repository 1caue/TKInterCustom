from customtkinter import * 
from pyautogui import hotkey
from tkinter import messagebox
from forex_python.converter import CurrencyRates as cot
import pyautogui as py

root = CTk()
root.geometry('400x250')
root.title('Conversor')

curreny = cot()

def conv():
    try:
        global a 
        usd_to_brl = curreny.get_rate('USD', 'BRL', timeout=None)
        a = float(ent.get()) * usd_to_brl
        lb3.configure(text=f'U$D: {a}')

    except Exception as e:
        print('Erro', e)
        messagebox.showinfo('Atenção', 'Informe o Valor', icon='error')

f = CTkFrame(root, width=700, height=50, fg_color='#0A146E')
f.place(rely=0.2, relx=0.3)
f.pack()

lb1 = CTkLabel(f, text='Conversor', font=("SemiBold", 30), text_color='#ffffff')
lb1.place(rely=0.2, relx=0.3)

lb2 = CTkLabel(root, text='Conversor de Moeda U$D:', text_color='White', font=("Arial", 20))
lb2.place(rely=0.25, relx=0.03)

ent = CTkEntry(root, placeholder_text='Digite o Valor em R$:', width=200)
ent.place(rely=0.4, relx=0.03)

lb3 = CTkLabel(root, text='U$D:', text_color='White')
lb3.place(rely=0.55, relx=0.03)

btn = CTkButton(root, text='Converter', fg_color='Black', hover_color='#393d42', corner_radius=30, command=conv)
btn.place(rely=0.8, relx=0.03)

root.mainloop()