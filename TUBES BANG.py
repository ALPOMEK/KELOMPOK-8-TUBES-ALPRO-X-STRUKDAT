import tkinter as tk
from tkinter import messagebox

# Simulasi data login (username dan password)
USER_DATA = {
    "admin": "1234",
    "user": "password"
}

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in USER_DATA and USER_DATA[username] == password:
        messagebox.showinfo("Login Berhasil", f"Selamat datang, {username}!")
        main_menu()  # Pindah ke menu utama
    else:
        messagebox.showerror("Login Gagal", "Username atau password salah!")

def main_menu():
    # Bersihkan layar login
    for widget in root.winfo_children():
        widget.destroy()

    # Buat menu utama
    tk.Label(root, text="Menu Utama", font=("Arial", 16)).pack(pady=20)
    tk.Button(root, text="Tambah Soal", command=add_question).pack(pady=10)
    tk.Button(root, text="Keluar", command=root.quit).pack(pady=10)

def add_question():
    messagebox.showinfo("Tambah Soal", "Fitur ini akan ditambahkan nanti.")

# GUI utama
root = tk.Tk()
root.title("Sistem Login Kuis")
root.geometry("300x200")

# Elemen login
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()
