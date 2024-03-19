from customtkinter import * 
from pyautogui import hotkey
from time import sleep
import pyautogui as py


def search(value):
    py.press('win')
    sleep(0.5)
    py.write('ok') 
def cmd(c1, c2, main):
    hotkey(c1, c2)
    main.destroy()

def get_value():
    v1 = ent1.get()
    print(v1)

root = CTk(fg_color="grey")
root.geometry("500x350")
root.title('Conversor de Moeda')

lbl = CTkLabel(root, text='Procurador', font=("Arial", 30), corner_radius=162, bg_color='grey', text_color='#ffffff')
lbl.place(rely=0.01, relx=0.35)

lbl1 = CTkLabel(root, text='O que deseja pesquisar?: ', text_color='white', font=("Arial", 20))
lbl1.place(rely=0.18, relx=0.15)

ent1 = CTkEntry(root, placeholder_text='Digite Aqui', width=250)
ent1.place(rely=0.28, relx=0.15)

lbl2 = CTkLabel(root, text='Com qual nome deseja salvar?: ', text_color='white', font=("Arial", 20))
lbl2.place(rely=0.38, relx=0.15)

ent2 = CTkEntry(root, placeholder_text='Digite Aqui', width=250)
ent2.place(rely=0.48, relx=0.15)

convertbt = CTkButton(root, text="Pesquisar", corner_radius=32, fg_color="black", hover_color='#b9b6ac', text_color='white',
                      command=search)
convertbt.place(rely=0.75, relx=0.35)

closebt = CTkButton(root, text='Fechar', corner_radius=32, fg_color='red', hover_color='#8b0000', text_color='#ffffff',
                    command=lambda: root.after(100, lambda: cmd('alt', 'f4', root)))
closebt.place(rely=0.85, relx=0.05)

root.mainloop()

'incompleto'