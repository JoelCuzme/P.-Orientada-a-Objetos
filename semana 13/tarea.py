import tkinter as tk

def agregar_item():
    if entrada.get():
        lista.insert(tk.END, entrada.get())
        entrada.delete(0, tk.END)

def limpiar_lista():
    lista.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("App Simple")

entrada = tk.Entry(ventana)
entrada.pack()

tk.Button(ventana, text="Agregar", command=agregar_item).pack()
tk.Button(ventana, text="Limpiar", command=limpiar_lista).pack()

lista = tk.Listbox(ventana)
lista.pack()

ventana.mainloop()