from customtkinter import *
from random import randint

def logic():
    itens = ('Pedra', 'Papel', 'Tesoura')
    pc = randint(0, 2)
    pl = randint(0, 2)
    # (itens[pc])

game = CTk(fg_color='#f8f1bd')
game.geometry('300x300')
game.title('Game 🎮')

lb1 = CTkLabel(game, text='Pedra, Papel, Tesoura', text_color='#000000', font=('Arial', 20))
lb1.place(relx=0.17, rely=0.01)

lb2 = CTkLabel(game, text='Selecione uma opção:', text_color='#000000', font=('Arial', 20))
lb2.place(relx=0.01, rely=0.18)

rock = CTkButton(game, text='Pedra', fg_color='black', hover_color='grey', border_color='grey', border_width=1)
rock.place(relx=0.01, rely=0.29)

paper = CTkButton(game, text='Papel', fg_color='black', hover_color='grey', border_color='grey', border_width=1)
paper.place(relx=0.01, rely=0.39)

scissors = CTkButton(game, text='Tesoura', fg_color='black', hover_color='grey', border_color='grey', border_width=1)
scissors.place(relx=0.01, rely=0.49)

lb3 = CTkLabel(game, text='--------------------', text_color='black', font=('Arial', 20))
lb3.place(relx=0.05, rely=0.65)

lb4 = CTkLabel(game, text='--------------------', text_color='black', font=('Arial', 20))
lb4.place(relx=0.05, rely=0.75)

game.mainloop()