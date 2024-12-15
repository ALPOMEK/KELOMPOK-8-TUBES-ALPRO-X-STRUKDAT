import tkinter as tk
from tkinter import messagebox, simpledialog

# Simulasi data login (username dan password)
USER_DATA = {
    "admin": "1234",
    "user": "password",
    "pome": "123450062",
    "ridwan": "1234500",
    "rahma": "123450102",
    "ale": "1234500",
    "keren":"1234500"
}

# Data soal dan jawaban
questions = []
scores = []

# Fungsi login
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in USER_DATA and USER_DATA[username] == password:
        messagebox.showinfo("Login Berhasil", f"Selamat datang, {username}!")
        main_menu()
    else:
        messagebox.showerror("Login Gagal", "Username atau password salah!")

# Menu utama
def main_menu():
    clear_screen()
    tk.Label(root, text="Menu Utama", font=("Arial", 16)).pack(pady=20)
    tk.Button(root, text="Tambah Soal", command=add_question).pack(pady=10)
    tk.Button(root, text="Edit Soal", command=edit_question).pack(pady=10)
    tk.Button(root, text="Hapus Soal", command=delete_question).pack(pady=10)
    tk.Button(root, text="Mulai Kuis", command=start_quiz).pack(pady=10)
    tk.Button(root, text="Keluar", command=root.quit).pack(pady=10)

# Bersihkan layar
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

# Tambah soal
def add_question():
    try:
        question = simpledialog.askstring("Tambah Soal", "Masukkan pertanyaan:")
        options = []
        for i in range(1, 5):
            option = simpledialog.askstring("Tambah Soal", f"Masukkan pilihan {i}:")
            options.append(option)
        correct_option = simpledialog.askinteger("Tambah Soal", "Masukkan nomor jawaban benar (1-4):")
        if question and all(options) and 1 <= correct_option <= 4:
            questions.append((question, options, correct_option))
            messagebox.showinfo("Sukses", "Soal berhasil ditambahkan!")
        else:
            messagebox.showwarning("Peringatan", "Input tidak boleh kosong atau salah!")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Edit soal
def edit_question():
    if not questions:
        messagebox.showwarning("Peringatan", "Belum ada soal yang ditambahkan!")
        return
    try:
        index = simpledialog.askinteger("Edit Soal", f"Masukkan nomor soal (1-{len(questions)}):")
        if 1 <= index <= len(questions):
            question = simpledialog.askstring("Edit Soal", "Masukkan pertanyaan baru:")
            options = []
            for i in range(1, 5):
                option = simpledialog.askstring("Edit Soal", f"Masukkan pilihan {i}:")
                options.append(option)
            correct_option = simpledialog.askinteger("Edit Soal", "Masukkan nomor jawaban benar (1-4):")
            if question and all(options) and 1 <= correct_option <= 4:
                questions[index - 1] = (question, options, correct_option)
                messagebox.showinfo("Sukses", "Soal berhasil diubah!")
            else:
                messagebox.showwarning("Peringatan", "Input tidak boleh kosong atau salah!")
        else:
            messagebox.showwarning("Peringatan", "Nomor soal tidak valid!")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Hapus soal
def delete_question():
    if not questions:
        messagebox.showwarning("Peringatan", "Belum ada soal yang ditambahkan!")
        return
    try:
        index = simpledialog.askinteger("Hapus Soal", f"Masukkan nomor soal (1-{len(questions)}):")
        if 1 <= index <= len(questions):
            questions.pop(index - 1)
            messagebox.showinfo("Sukses", "Soal berhasil dihapus!")
        else:
            messagebox.showwarning("Peringatan", "Nomor soal tidak valid!")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Mulai kuis
def start_quiz():
    if not questions:
        messagebox.showwarning("Peringatan", "Belum ada soal untuk kuis!")
        return

    def next_question(index, score):
        if index >= len(questions):
            messagebox.showinfo("Hasil Kuis", f"Skor Anda: {score}/{len(questions)}")
            scores.append(score)
            main_menu()
            return

        clear_screen()
        question, options, correct_option = questions[index]
        tk.Label(root, text=f"Soal {index+1}: {question}", wraplength=400, font=("Arial", 14)).pack(pady=20)
        selected_option = tk.IntVar(value=0)

        for i, option in enumerate(options):
            tk.Radiobutton(root, text=option, variable=selected_option, value=i+1).pack(anchor="w", padx=20)

        def submit_answer():
            if selected_option.get() == correct_option:
                next_question(index + 1, score + 1)
            else:
                next_question(index + 1, score)

        tk.Button(root, text="Submit", command=submit_answer).pack(pady=20)

    next_question(0, 0)

# GUI Utama
root = tk.Tk()
root.title("Sistem Kuis Interaktif")
root.geometry("500x400")

# Elemen login
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()
