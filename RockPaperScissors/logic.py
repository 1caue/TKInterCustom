from customtkinter import *
from random import randint

def pedra():
    itens = ('Pedra', 'Papel', 'Tesoura')
    pl = 'Pedra'
    pc = randint(0, 2)
    sort = (itens[pc])
    if sort == 'Pedra':
        lb3.configure(text='O Computador também jogou Pedra')
        lb4.configure(text='Empate!')

    if sort == 'Papel':
        lb3.configure(text='O computador jogou Papel')
        lb4.configure(text='O computador ganhou!')

    if sort == 'Tesoura':
        lb3.configure(text='O computador jogou Tesoura')
        lb4.configure(text='Você Ganhou!')

def papel():
    items = ('Pedra', 'Papel', 'Tesoura')
    pl = 'Papel'
    pc = randint(0, 2)
    sort = (items[pc])
    if sort == 'Pedra':
        lb3.configure(text='O Computador jogou Pedra')
        lb4.configure(text='Você Ganhou!')

    if sort == 'Papel': 
        lb3.configure(text='O computador também jogou Papel')
        lb4.configure(text='Empate!')  

    if sort == 'Tesoura':
        lb3.configure(text='O Computador Jogou Tesoura')
        lb4.configure(text='O Computador Ganhou')

def tesoura():
    items = ('Pedra', 'Papel', 'Tesoura')
    pl = 'Tesoura'
    pc = randint(0, 2)
    sort = (items[pc])
    if sort == 'Pedra':
        lb3.configure(text='O computador jogou Pedra')
        lb4.configure(text='O computador Ganhou!')

    if sort == 'Papel':
        lb3.configure(text='O Computador Jogou Papel')
        lb4.configure(text='Você Ganhou!')

    if sort == 'Tesoura':
        lb3.configure(text='O Computador também Jogou Tesoura')
        lb4.configure(text='Empate!')    

game = CTk(fg_color='#f8f1bd')
game.geometry('350x300')
game.title('Game 🎮')

lb1 = CTkLabel(game, text='Pedra, Papel, Tesoura', text_color='#000000', font=('Arial', 20))
lb1.place(relx=0.23, rely=0.01)

lb2 = CTkLabel(game, text='Selecione uma opção:', text_color='#000000', font=('Arial', 20))
lb2.place(relx=0.01, rely=0.18)

rock = CTkButton(game, text='Pedra', fg_color='black', hover_color='grey', border_color='grey', border_width=1, command=pedra)
rock.place(relx=0.01, rely=0.29)

paper = CTkButton(game, text='Papel', fg_color='black', hover_color='grey', border_color='grey', border_width=1, command=papel)
paper.place(relx=0.01, rely=0.39)

scissors = CTkButton(game, text='Tesoura', fg_color='black', hover_color='grey', border_color='grey', border_width=1, command=tesoura)
scissors.place(relx=0.01, rely=0.49)

lb3 = CTkLabel(game, text='--------------------', text_color='black', font=('Arial', 20))
lb3.place(relx=0.05, rely=0.65)

lb4 = CTkLabel(game, text='--------------------', text_color='black', font=('Arial', 20))
lb4.place(relx=0.05, rely=0.75)

game.mainloop()

# Incompleto
# Adicionar imagens ao Game