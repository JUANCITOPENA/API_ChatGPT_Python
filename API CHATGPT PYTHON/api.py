import tkinter as tk
from tkinter import filedialog, messagebox
import openai

openai.api_key = "TU API AQUI" #AQUI VA TU API LA CUAL TE DA OPEN-AI

def generate_text():
    prompt = prompt_input.get()
    if prompt in ['exit','salir','quit','terminar']:
        root.destroy()
        return
    with open("consulta.txt", "a") as file:
        file.write(prompt + "\n")
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.3
    )
    response = completion.choices[0].text
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, response)
    prompt_input.delete(0, tk.END)

def clear_results():
    text_area.delete('1.0', tk.END)
    prompt_input.delete(0, tk.END)

def save_results():
    result = text_area.get('1.0', tk.END)
    if not result.strip():
        messagebox.showerror("Error", "No hay resultados para guardar.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_path:
        with open(file_path, "w") as f:
            f.write(result)
            messagebox.showinfo("Guardado", f"Los resultados se han guardado en {file_path}.")

root = tk.Tk()
root.title("Generador de Texto")

canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()

prompt_label = tk.Label(root, text="Introduzca el prompt:", font=("Arial", 14, "bold"), justify=tk.CENTER, wraplength=600)
prompt_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

prompt_input = tk.Entry(root, width=80, font=("Arial", 12, "bold"))
prompt_input.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

generate_button = tk.Button(root, text="Generar Texto", command=generate_text, fg="white", bg="green", font=("Arial", 16, "bold"))
generate_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

results_label = tk.Label(root, text="Resultados:", font=("Arial", 14, "bold"), justify=tk.CENTER, wraplength=600)
results_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

text_area = tk.Text(root, width=60, height=10, font=("Arial", 14, "bold"), fg="black", wrap=tk.WORD)
text_area.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

clear_button = tk.Button(root, text="Limpiar", command=clear_results, fg="black", bg="yellow", font=("Arial", 16, "bold"))
clear_button.place(relx=0.3, rely=0.9, anchor=tk.CENTER)

save_button = tk.Button(root, text="Guardar", command=save_results, bg="white", font=("Arial", 16, "bold"))
save_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

exit_button = tk.Button 
exit_button = tk.Button(root, text="Salir", command=root.destroy, bg="red", fg="white", font=("Arial", 16, "bold"))
exit_button.place(relx=0.7, rely=0.9, anchor=tk.CENTER)

root.mainloop()
