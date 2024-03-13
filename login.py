import customtkinter as ctk
import pyautogui as py
from pyautogui import hotkey

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("400x250")
root.title('New Aplocation')

def comando1(c1, c2, main):
    hotkey(c1, c2)
    print('Funcionando!')
    main.destroy()

txt = ctk.CTkLabel(root, text='Fazer Login:', font=ctk.CTkFont(size=30, weight='bold'))
txt.pack(pady=20, padx=20)

email = ctk.CTkEntry(root, placeholder_text='Seu E-mail')
email.pack(pady=10, padx=20)

senha = ctk.CTkEntry(root, placeholder_text='Sua Senha')
senha.pack(pady=5, padx=10)

checkbox = ctk.CTkCheckBox(root, text='Lembrar Login?')
checkbox.pack(pady=5, padx=10)

btn = ctk.CTkButton(root, text='Entrar', command=lambda: root.after(100, lambda: comando1('alt', 'f4', root)))
btn.pack(pady=10, padx=40)          

root.mainloop()