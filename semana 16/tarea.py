import tkinter as tk


class ListaTareas:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Lista de Tareas")

        self.tareas = []

        # Entrada de texto
        self.entrada = tk.Entry(self.ventana, width=30)
        self.entrada.pack(pady=10)
        self.entrada.bind("<Return>", self.agregar)

        # Lista
        self.lista = tk.Listbox(self.ventana, width=40)
        self.lista.pack()

        # Botones
        tk.Button(self.ventana, text=" Completar", command=self.completar).pack(side=tk.LEFT)
        tk.Button(self.ventana, text=" Eliminar", command=self.eliminar).pack(side=tk.RIGHT)

        # Atajos
        self.ventana.bind("<c>", lambda e: self.completar())
        self.ventana.bind("<d>", lambda e: self.eliminar())
        self.ventana.bind("<Escape>", lambda e: self.ventana.destroy())

    def agregar(self, event=None):
        tarea = self.entrada.get()
        if tarea:
            self.tareas.append(tarea)
            self.actualizar_lista()
            self.entrada.delete(0, tk.END)

    def completar(self, event=None):
        seleccion = self.lista.curselection()
        if seleccion:
            item = self.lista.get(seleccion)
            self.lista.delete(seleccion)
            self.lista.insert(seleccion, "✓ " + item)

    def eliminar(self, event=None):
        seleccion = self.lista.curselection()
        if seleccion:
            self.lista.delete(seleccion)

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for t in self.tareas:
            self.lista.insert(tk.END, t)


app = ListaTareas()
app.ventana.mainloop()