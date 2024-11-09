"""
Desafío 1: Gestor de notas con Tkinter y almacenamiento en archivo CSV

Descripción:
Crear una interfaz gráfica con tkinter que permita al usuario ingresar su nombre y una nota en un campo de texto,
y luego guardar estos datos en un archivo CSV.
"""

import tkinter as tk
import csv
import tkinter.messagebox
import os

def save_data():

    name = entry_name.get().strip()
    grade = entry_grade.get().strip()
    
    
    if not name or not grade:
        tkinter.messagebox.showerror("Error", "Los campos no pueden estar vacíos.")
        return
    
    try:
        grade = float(grade)
    except ValueError:
        tkinter.messagebox.showerror("Error", "La nota debe ser un número.")
        return
    
    file_exists = os.path.isfile('notas.csv')
    with open('notas.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Nombre", "Nota"])
        writer.writerow([name, grade])
    
    entry_name.delete(0, tk.END)
    entry_grade.delete(0, tk.END)
    tkinter.messagebox.showinfo("Éxito", "Datos guardados correctamente.")

root = tk.Tk()
root.title("Gestor de Notas")

label_name = tk.Label(root, text="Nombre:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_grade = tk.Label(root, text="Nota:")
label_grade.pack()
entry_grade = tk.Entry(root)
entry_grade.pack()

save_button = tk.Button(root, text="Guardar", command=save_data)
save_button.pack(pady=10)

root.geometry("300x200")

root.mainloop()
