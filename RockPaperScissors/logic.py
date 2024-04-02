from customtkinter import *
from random import randint
from PIL import Image

def pedra():
    global cont, contp
    itens = ('Pedra', 'Papel', 'Tesoura')
    pc = randint(0, 2)
    sort = (itens[pc])
    if sort == 'Pedra':
        lb3.configure(text='O Computador também jogou Pedra')
        lb4.configure(text='Empate!')

    if sort == 'Papel':
        lb3.configure(text='O computador jogou Papel')
        lb4.configure(text='O computador ganhou!')
        contp += 1
        lb6.configure(text=f'Contador de Derrotas: {contp}')

    if sort == 'Tesoura':
        lb3.configure(text='O computador jogou Tesoura')
        lb4.configure(text='Você Ganhou!')
        cont += 1
        lb5.configure(text=f'  Contador de vitórias: {cont}  ')

def papel():
    global cont, contp
    items = ('Pedra', 'Papel', 'Tesoura')
    pc = randint(0, 2)
    sort = (items[pc])
    if sort == 'Pedra':
        lb3.configure(text='O Computador jogou Pedra')
        lb4.configure(text='Você Ganhou!')
        cont += 1
        lb5.configure(text=f'  Contador de vitórias: {cont}  ')

    if sort == 'Papel': 
        lb3.configure(text='O computador também jogou Papel')
        lb4.configure(text='Empate!')  

    if sort == 'Tesoura':
        lb3.configure(text='O Computador Jogou Tesoura')
        lb4.configure(text='O Computador Ganhou')
        contp += 1
        lb6.configure(text=f'Contador de Derrotas: {contp}')

def tesoura():
    global cont, contp 
    items = ('Pedra', 'Papel', 'Tesoura')
    pc = randint(0, 2)
    sort = (items[pc])
    if sort == 'Pedra':
        lb3.configure(text='O computador jogou Pedra')
        lb4.configure(text='O computador Ganhou!')
        contp += 1
        lb6.configure(text=f'Contador de Derrotas: {contp}')

    if sort == 'Papel':
        lb3.configure(text='O Computador Jogou Papel')
        lb4.configure(text='Você Ganhou!')
        cont += 1
        lb5.configure(text=f'  Contador de vitórias: {cont}  ')

    if sort == 'Tesoura':
        lb3.configure(text='O Computador também Jogou Tesoura')
        lb4.configure(text='Empate!')    

game = CTk(fg_color='#DCDCDC')
game.geometry('370x300')
game.title('Game 🎮')

frame = CTkFrame(game, width=700, height=40, fg_color='#515151', corner_radius=0)
frame.place(relx=0, rely=0)
frame.pack()

lb1 = CTkLabel(frame, text='Pedra, Papel, Tesoura', text_color='white', font=('Arial', 20))
lb1.place(relx=0.23, rely=0.1)

lb2 = CTkLabel(game, text='Selecione uma opção:', text_color='#000000', font=('Arial', 20))
lb2.place(relx=0.01, rely=0.18)

img1 = CTkImage(dark_image=Image.open(r'C:\Users\CAUÊ\Documents\Python - Tkinter\Custom Tkinter\RockPaperScissors\ped.png'), size=(20, 20))
rock = CTkButton(game, text='Pedra', fg_color='grey', text_color='black', hover_color='#8c8c8c', border_color='grey', border_width=1, image=img1, command=pedra)
rock.place(relx=0.01, rely=0.29)

img2 = CTkImage(dark_image=Image.open(r'C:\Users\CAUÊ\Documents\Python - Tkinter\Custom Tkinter\RockPaperScissors\pp.png'), size=(18, 18))
paper = CTkButton(game, text='Papel', fg_color='grey', text_color='black', hover_color='#8c8c8c', border_color='grey', border_width=1, image=img2, command=papel)
paper.place(relx=0.01, rely=0.39)

img3 = CTkImage(dark_image=Image.open(r'C:\Users\CAUÊ\Documents\Python - Tkinter\Custom Tkinter\RockPaperScissors\tes.png'), size=(24, 20))
scissors = CTkButton(game, text='Tesoura', fg_color='grey', text_color='black', hover_color='#8c8c8c', border_color='grey', border_width=1, image=img3,command=tesoura)
scissors.place(relx=0.01, rely=0.49)

lb3 = CTkLabel(game, text='--------------------', text_color='black', font=('Arial', 20))
lb3.place(relx=0.05, rely=0.65)

lb4 = CTkLabel(game, text='--------------------', text_color='black', font=('Arial', 20))
lb4.place(relx=0.05, rely=0.75)

lb5 = CTkLabel(game, text='Contador de Vitórias: 0', text_color='black', font=('Arial', 15), bg_color='white', width=200)
lb5.place(relx=0, rely=0.91)
 
lb6 = CTkLabel(game, text='Contador de Derrotas: 0', text_color='black', font=('Arial', 15), bg_color='red', width=180)
lb6.place(relx=0.52, rely=0.91)

cont = 0
contp = 0
game.mainloop()

# Incompleto
# Adicionar imagens ao Game
