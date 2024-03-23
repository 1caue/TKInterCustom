from customtkinter import * 
from pyautogui import hotkey
from tkinter import messagebox
from forex_python.converter import CurrencyRates as cot

root = CTk()
root.geometry('400x500')
root.title('Conversor')

curreny = cot()

def close(c1, c2, main):
    hotkey(c1, c2)
    main.destroy()

def usd():
    try:
        global a 
        usd_to_brl = curreny.get_rate('BRL', 'USD')
        a = float(ent.get()) * usd_to_brl
        lb3.configure(text=f'U$D: {a:.2f}')

    except Exception as e:
        print('Erro', e)
        messagebox.showinfo('Atenção', 'Informe um Valor válido', icon='error')

def eur():
    try:
        global b
        eur_to_brl = curreny.get_rate('BRL', 'EUR')
        b = float(ent2.get()) * eur_to_brl
        lb5.configure(text=f'EUR: {b:.2f}')

    except Exception as e:
        print('Erro', e)
        messagebox.showinfo('Atenção', 'Informe um Valor válido', icon='error')

def jpy():
    try:
        global c
        jpy_to_jpy = curreny.get_rate('BRL', 'JPY')
        c = float(ent3.get()) * jpy_to_jpy   
        lb7.configure(text=f'JPY: {c:.2f}')

    except Exception as e:
        print('Erro', e)
        messagebox.showinfo('Atenção', 'Informe um Valor válido', icon='error')


f = CTkFrame(root, width=700, height=50, fg_color='#0A146E')
f.place(rely=0.3, relx=0.3)
f.pack()

lb1 = CTkLabel(f, text='Conversor de Moeda', font=("SemiBold", 30), text_color='#ffffff')
lb1.place(rely=0.15, relx=0.18)

# U$D
lb2 = CTkLabel(root, text='BRL para U$D (Dólar americano):', text_color='White', font=("Arial", 20))
lb2.place(rely=0.12, relx=0.03)

ent = CTkEntry(root, placeholder_text='Digite o Valor em R$:', width=200)
ent.place(rely=0.20, relx=0.03)

lb3 = CTkLabel(root, text='U$D:', text_color='White')
lb3.place(rely=0.27, relx=0.03)

btn1 = CTkButton(root, text='Converter', fg_color='Black', hover_color='#393d42', corner_radius=30, command=usd)
btn1.place(rely=0.20, relx=0.6)

# EUR
lb4 = CTkLabel(root, text='BRL para EUR (Euro):', font=('SemiBold', 20), text_color='#ffffff')
lb4.place(rely=0.37, relx=0.03)

ent2 = CTkEntry(root, placeholder_text="Digite o Valor em R$:", width=200)
ent2.place(rely=0.45, relx=0.03)

lb5 = CTkLabel(root, text='EUR(Euro):', text_color='White')
lb5.place(rely=0.52, relx=0.03)

btn2 = CTkButton(root, text='Converter', fg_color='Black', hover_color='#393d42', corner_radius=30, command=eur)
btn2.place(rely=0.45, relx=0.6)

# JPY
lb6 = CTkLabel(root, text='BRL para JPY (Iene japonês):', font=('SemiBold', 20), text_color='#ffffff')
lb6.place(rely=0.61, relx=0.03)

ent3 = CTkEntry(root, placeholder_text='Digite o Valor em R$:', width=200)
ent3.place(rely=0.69, relx=0.03)

lb7 = CTkLabel(root, text='JPY:', text_color='White')
lb7.place(rely=0.76, relx=0.03)

btn3 = CTkButton(root, text='Converter', fg_color='Black', hover_color='#393d42', corner_radius=30, command=jpy)
btn3.place(rely=0.69, relx=0.6)

# Close 
closebt = CTkButton(root, text='Fechar', corner_radius=32, fg_color='red', hover_color='#8b0000', text_color='#ffffff',
                    command=lambda: root.after(100, lambda: close('alt', 'f4', root)))
closebt.place(rely=0.85, relx=0.29)

root.mainloop()