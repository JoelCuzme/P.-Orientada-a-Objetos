import tkinter as tk
from tkinter import messagebox, ttk

class Agenda:
    def __init__(self, rot):
        self.root = rot
        self.root.title("Agenda Personal")

        # TreeView para mostrar eventos
        self.tree = ttk.Treeview(rot, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Campos de entrada
        ttk.Label(rot, text="Fecha (YYYY-MM-DD):").pack()
        self.fecha_entry = ttk.Entry(rot)
        self.fecha_entry.pack()

        ttk.Label(rot, text="Hora:").pack()
        self.hora_entry = ttk.Entry(rot)
        self.hora_entry.pack()

        ttk.Label(rot, text="Descripción:").pack()
        self.descripcion_entry = ttk.Entry(rot)
        self.descripcion_entry.pack()

        # Botones
        ttk.Button(rot, text="Agregar Evento", command=self.agregar_evento).pack(pady=5)
        ttk.Button(rot, text="Eliminar Evento", command=self.eliminar_evento).pack(pady=5)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", tk.END, values=(fecha, hora, descripcion))
            self.fecha_entry.delete(0, tk.END)
            self.hora_entry.delete(0, tk.END)
            self.descripcion_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Todos los campos son obligatorios.")

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            confirmar = messagebox.askyesno("Confirmar", "¿Eliminar este evento?")
            if confirmar:
                self.tree.delete(seleccionado)
        else:
            messagebox.showwarning("Error", "Selecciona un evento para eliminar.")

rot = tk.Tk()
app = Agenda(rot)
rot.mainloop()