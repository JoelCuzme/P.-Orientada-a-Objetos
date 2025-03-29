import tkinter as tk
from tkinter import messagebox

# Crear la ventana
ventana = tk.Tk()
ventana.title("Lista de Tareas")

# Lista para guardar tareas
lista_tareas = []

# Funciones básicas
def agregar_tarea():
    tarea = entrada.get()
    if tarea:
        listbox.insert(tk.END, tarea)
        lista_tareas.append(False)  # False = no completada
        entrada.delete(0, tk.END)

def completar_tarea():
    try:
        indice = listbox.curselection()[0]
        if lista_tareas[indice]:
            listbox.itemconfig(indice, fg='black')
            lista_tareas[indice] = False
        else:
            listbox.itemconfig(indice, fg='gray')
            lista_tareas[indice] = True
    except:
        messagebox.showwarning("Error", "Selecciona una tarea")

def borrar_tarea():
    try:
        indice = listbox.curselection()[0]
        listbox.delete(indice)
        del lista_tareas[indice]
    except:
        messagebox.showwarning("Error", "Selecciona una tarea")

# Elementos de la interfaz
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)

tk.Button(ventana, text="Agregar", command=agregar_tarea).pack()

listbox = tk.Listbox(ventana, width=40, height=12)
listbox.pack(pady=10)

tk.Button(ventana, text="Completar", command=completar_tarea).pack(side=tk.LEFT, padx=20)
tk.Button(ventana, text="Borrar", command=borrar_tarea).pack(side=tk.LEFT)

ventana.mainloop()