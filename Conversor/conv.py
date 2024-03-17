from customtkinter import * 
from tkinter import messagebox
from pyautogui import hotkey

def get_value(a, b):
    try:
        valor_num = float(a)
        result = a * b
        print(result) 
    except ValueError:
        print('Por favor')

def cmd(c1, c2, main):
    hotkey(c1, c2)
    main.destroy()

def get_value(val):
     val = box1.get()
     v1 = ent1.get()
    
     if val in 'Real para Dólar':
          print('Real x Dólar')
          get_value(v1, 0.2)

     if val in 'Real para Euro':
          print('Real x Euro')
     
     if val in 'Dolar para Real':
          print('Dolar x Real')
     
     if val in 'Dolar para Euro':
          print('Dolar x Euro')

     if val in 'Euro para Dolar':
          print('Euro x Dolar')

     if val in 'Euro para Real':
          print('Euro x Real')

root = CTk(fg_color="#111188")
root.geometry("500x350")
root.title('Conversor de Moeda')

lbl = CTkLabel(root, text='Conversor de Moeda', font=("Arial", 30), corner_radius=62, bg_color='#111188', text_color='#ffbf00')
lbl.place(rely=0.01, relx=0.2)

lblmeio = CTkLabel(root, text='=', text_color='white', font=("Arial", 40))
lblmeio.place(rely=0.28, relx=0.47)

box1 = CTkComboBox(root, values=['Real para Dólar',
                                 'Real para Euro',
                                 'Dolar para Real', 
                                 'Dolar para Euro', 
                                 'Euro para Dolar', 
                                 'Euro para Real'], command=get_value)
box1.place(rely=0.2, relx=0.15)

ent1 = CTkEntry(root, placeholder_text='Digite o valor')
ent1.place(rely=0.3, relx=0.15)

ent2 = CTkEntry(root, placeholder_text='Valor de Saída')
ent2.place(rely=0.3, relx=0.55)

convertbt = CTkButton(root, text="Converter", corner_radius=32, fg_color="black", hover_color='#b9b6ac', text_color='white')
convertbt.place(rely=0.45, relx=0.35)

closebt = CTkButton(root, text='Fechar', corner_radius=32, fg_color='red', hover_color='#8b0000', text_color='#ffffff',
                    command=lambda: root.after(100, lambda: cmd('alt', 'f4', root)))
closebt.place(rely=0.85, relx=0.05)

root.mainloop()

'Incompleto'