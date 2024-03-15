from customtkinter import * 
from pyautogui import hotkey

spacey = 0.1
spacex1 = 0.13
spacex2 = 0.23 
c = 0

def adicionar():
    global spacey, spacex1, spacex2, c
    if c >= 11:
        spacey = 0.1
        spacex1 = 0.50
        spacex2 = 0.60  
        if c > 11:
          for a in range(0, 1): 
            spacey += 0.07
            
    check = CTkCheckBox(app, text='')
    ent = CTkEntry(app)
    check.place(rely=spacey, relx=spacex1, anchor='center')
    ent.place(rely=spacey, relx=spacex2, anchor='center')
    c += 1
    if c < 11:
        spacey += 0.07

def comand(c1, c2, main):
    hotkey(c1, c2)
    main.destroy()

app = CTk()
app.geometry("500x600")
app.title("Lista de Tarefas")

# Close Button
btn = CTkButton(app, text="Fechar", corner_radius=32, fg_color='#FF0000', hover_color='#8b0000', border_color='#FF0000',
                command=lambda: app.after(50, lambda:comand('alt', 'f4', app)))
btn.place(rely=0.9, relx=0.3, anchor='center')

# New Task
for x in range(0, 2):
    btn2 = CTkButton(app, text="Nova Tarefa", corner_radius=32, fg_color='#000000', hover_color='#3B3C3C',
                 command=lambda: adicionar())
    btn2.place(rely=0.9, relx=0.6, anchor='center')

app.mainloop()