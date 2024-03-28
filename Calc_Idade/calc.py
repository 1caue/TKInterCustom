from customtkinter import *
from tkinter import messagebox
from time import sleep

def calculator():
  try:
    global a
    a = 2024 - int(ent.get()) 
    lb3.configure(text=f'Aproximadamente {a} Anos')
    f = 0
    
    for a in range(0, a):
      f += 365
    
    lb4.configure(text=f'Pouco mais de {f} Dias de vida')
  
  except:
    print('TypeError')
    messagebox.showinfo('Atenção!', 'Informe o Ano de Nascimento', icon='error')

main = CTk(fg_color='grey')
main.geometry("450x250")
main.title('Gestão de Idade')

frame = CTkFrame(main, width=500, height=50, fg_color='green', corner_radius=0)
frame.place(relx=0, rely=0)
frame.pack()

lbl1 = CTkLabel(frame, text='Calculadora de idade', font=("Arial", 30), text_color='White')
lbl1.place(relx=0.2, rely=0.2)

lb2 = CTkLabel(main, text='Digite o Ano que você nasceu:', font=("Arial", 20), text_color='White')
lb2.place(relx=0.1, rely=0.25)

lb3 = CTkLabel(main, text='--------------', font=('Arial', 20))
lb3.pack(anchor='s', expand=True, pady=10)
lb3.place(rely=0.50, relx=0.1)

lb4 = CTkLabel(main, text='------------------', font=('Arial', 20))
lb4.pack(anchor='s', expand=True, pady=10)
lb4.place(rely=0.63, relx=0.1)

ent = CTkEntry(main, placeholder_text='Digite aqui: ', width=200)
ent.place(relx=0.1, rely=0.37)

btn1 = CTkButton(main, text='Calcular', fg_color='Black', hover_color='#393d42',corner_radius=20, command=calculator)
btn1.place(relx=0.1, rely=0.80)

main.mainloop()