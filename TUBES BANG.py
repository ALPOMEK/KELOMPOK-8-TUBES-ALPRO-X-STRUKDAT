import tkinter as tk
from tkinter import messagebox, simpledialog

# Simulasi data login (username dan password)
USER_DATA = {
    "admin": "1234",
    "user": "password"
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
        answer = simpledialog.askstring("Tambah Soal", "Masukkan jawaban:")
        if question and answer:
            questions.append((question, answer))
            messagebox.showinfo("Sukses", "Soal berhasil ditambahkan!")
        else:
            messagebox.showwarning("Peringatan", "Pertanyaan atau jawaban tidak boleh kosong!")
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
            new_question = simpledialog.askstring("Edit Soal", "Masukkan pertanyaan baru:")
            new_answer = simpledialog.askstring("Edit Soal", "Masukkan jawaban baru:")
            if new_question and new_answer:
                questions[index - 1] = (new_question, new_answer)
                messagebox.showinfo("Sukses", "Soal berhasil diubah!")
            else:
                messagebox.showwarning("Peringatan", "Input tidak boleh kosong!")
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

    score = 0
    for i, (question, answer) in enumerate(questions):
        user_answer = simpledialog.askstring(f"Soal {i+1}", question)
        if user_answer and user_answer.lower() == answer.lower():
            score += 1

    scores.append(score)
    messagebox.showinfo("Hasil Kuis", f"Skor Anda: {score}/{len(questions)}")

# GUI Utama
root = tk.Tk()
root.title("Sistem Kuis Interaktif")
root.geometry("400x300")

# Elemen login
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()
