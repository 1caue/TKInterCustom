from customtkinter import * 
from pyautogui import hotkey
from time import sleep
import pyautogui as py

def search():
    py.press('win')
    sleep(1)
    
    py.write('Edge')
    sleep(0.5)
    
    py.press('enter')
    sleep(1)
    
    hotkey('win', 'up')
    sleep(0.5)
    
    py.write('https://chat.openai.com/')
    sleep(1)
    
    py.press('enter')
    sleep(3)

    py.write(f'Crie um artigo sobre o/a {ent1.get()} com no maximo 30 linhas')
    py.press('enter')
    
    sleep(19)
    py.scroll(-800)

    sleep(1)
    image = py.locateOnScreen(r'C:\Users\CAUÊ\Documents\Python - Tkinter\Custom Tkinter\Search\cp.png')
    py.click(image)

    sleep(2)
    img = py.locateOnScreen(r'C:\Users\CAUÊ\Documents\Python - Tkinter\Custom Tkinter\Search\bn.png')
    py.click(img)

    sleep(1)
    hotkey('ctrl', 'v')
    hotkey('ctrl', 's')

    sleep(1)
    sv = ent2.get()
    py.write(sv)
    py.press('enter')

def cmd(c1, c2, main):
    hotkey(c1, c2)
    main.destroy()

def get_value():
    v1 = ent1.get()
    print(v1)

root = CTk(fg_color="grey")
root.geometry("500x350")
root.title('Artigos')

f = CTkFrame(root, width=700, height=60, fg_color='#515151', corner_radius=0)
f.place(rely=1, relx=1)
f.pack()

lbl = CTkLabel(f, text='Criador de Artigos', font=("Arial", 30), corner_radius=162, text_color='#ffffff')
lbl.place(rely=0.2, relx=0.24)

lbl1 = CTkLabel(root, text='Assunto do artigo: ', text_color='white', font=("Arial", 20))
lbl1.place(rely=0.18, relx=0.15)

ent1 = CTkEntry(root, placeholder_text='Digite Aqui', width=250)
ent1.place(rely=0.28, relx=0.15)

lbl2 = CTkLabel(root, text='Com qual nome deseja salvar o artigo?: ', text_color='white', font=("Arial", 20))
lbl2.place(rely=0.38, relx=0.15)

ent2 = CTkEntry(root, placeholder_text='Digite Aqui', width=250)
ent2.place(rely=0.48, relx=0.15)

convertbt = CTkButton(root, text="Pesquisar", corner_radius=32, fg_color="black", hover_color='#b9b6ac', text_color='white',
                      command=search)
convertbt.place(rely=0.65, relx=0.35)

closebt = CTkButton(root, text='Fechar', corner_radius=32, fg_color='red', hover_color='#8b0000', text_color='#ffffff',
                    command=lambda: root.after(100, lambda: cmd('alt', 'f4', root)))
closebt.place(rely=0.85, relx=0.05)

root.mainloop()

'Finalizado!!'