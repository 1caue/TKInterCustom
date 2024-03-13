from customtkinter import * 
from pyautogui import hotkey

cont = 0

def contador():
    global cont
    cont += 1
    lb.configure(text=f"Você clicou no botão {cont} Vezes")

def cmd(c1, c2, main):
    hotkey(c1, c2)
    print('Funcionando!')
    main.destroy()

def selecao(valor):
    if valor in 'Opção 1':
        print(f'\033[32m{valor} Selecionada!, Boa Escolha\033[m')
    elif valor in 'Opção 2':
        print(f'\033[33m{valor} Selecionada!, Perfeita Escolha\033[m')
    else:
        print(f'\033[34m{valor} Selecionada!, Ótima Escolha\033[m')

def add():
    ent = CTkEntry(app)
    ent.place(relx=0.2, rely=0.7, anchor="center")

def click():
    print(f'Output: {box2.get()}')

app = CTk()
app.geometry("800x800")
app.title('Schema')

set_default_color_theme("dark-blue")

# Definir botão 
btn = CTkButton(app, text='Fechar', corner_radius=32, fg_color="#FF0000", hover_color="#8b0000", border_color="#ffffff", text_color='#ffffff',
                command=lambda: app.after(100, lambda: cmd('alt', 'f4', app)))
btn.place(relx=0.5, rely=0.1, anchor="center")

btn2 = CTkButton(app, text='Add', corner_radius=32, fg_color="#1425e6", hover_color="#070e5b", border_color="#ffffff", text_color='#ffffff',
                command=lambda: app.after(100, lambda: add()))
btn2.place(relx=0.2, rely=0.9, anchor="center")

# Definir Label
lb1 = CTkLabel(app, text="Label", font=("Arial", 20))
lb1.place(relx=0.5, rely=0.2, anchor="center")

# Caixa de Seleção
box = CTkComboBox(app, values=['Opção 1', 'Opção 2', 'Opção 3'], command=selecao)
box.place(relx=0.5, rely=0.3, anchor="center")

# Ativar/Desativar
ad = CTkSwitch(app, text="Ativar/Desativar")
ad.place(relx=0.5, rely=0.4, anchor="center")

# Caixa de Texto
ent = CTkEntry(app)
ent.place(relx=0.5, rely=0.5, anchor="center")

# Caixa de Texto maior
big_ent = CTkTextbox(app, scrollbar_button_color='grey')
big_ent.place(relx=0.6, rely=0.75, anchor="center")

# CheckBox
checkbox = CTkCheckBox(app, text='')
checkbox.place(relx=0.2, rely=0.8, anchor="center")

# Caixa e Entrada de dados e "Submit"
box2 = CTkEntry(app, placeholder_text="Digite algo")
bt = CTkButton(app, text='Enviar', command=click)

box2.pack(anchor='s', expand=True)
box2.place(rely=0.4, relx=0.03)
bt.pack(anchor='n', expand=True)
bt.place(rely=0.48, relx=0.03)

# Contador de Cliques
lb = CTkLabel(app, text='Você clicou no botão 0 vezes')
btcick = CTkButton(app, text='Clique aqui!', command=contador)
lb.pack(anchor='s', expand=True, pady=10)
lb.place(rely=0.6, relx=0.03)
btcick.pack(anchor='n', expand=True)
btcick.place(rely=0.68, relx=0.03)

# Janelas 
tabview = CTkTabview(app)
tabview.pack(padx=10, pady=10)
tabview.place(relx=0.01, rely=0.03)

tabview.add("Página 1")
tabview.add("Página 2")
tabview.add("Página 3")

label1 = CTkLabel(tabview.tab("Página 1"), text="Você atingirá o sucesso")
#label1.pack(padx=0.04, pady=0.18)
label1.place(relx=0.001, rely=0.1)

label2 = CTkLabel(tabview.tab("Página 2"), text="Os planos de Deus são justos e certeiros!")
#label2.pack(padx=0.04, pady=0.18)
label2.place(relx=0.001, rely=0.1)

label3 = CTkLabel(tabview.tab("Página 3"), text="Colecione memórias e acumule sorrisos.")
#label3.pack(padx=0.04, pady=0.18)
label3.place(relx=0.001, rely=0.1)

app.mainloop()