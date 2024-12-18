import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# Simulasi data login
USER_DATA = {
    "guru": {"password": "123", "role": "teacher"},
    "student": {"password": "stud123", "role": "student"},
    "pome": {"password": "123450062", "role": "student"},
    "rahma": {"password": "123450102", "role": "student"},
    "ale": {"password": "123450075", "role": "student"},
    "keren": {"password": "123450020", "role": "student"},
    "ridwan": {"password": "123450091", "role": "student"}
}

# File JSON untuk menyimpan soal dan skor
DATA_FILE = r"D:\FIKRI\LEARN DATA ANALYSIS\TUBES\datatubes.json"
SCORE_FILE = r"D:\FIKRI\LEARN DATA ANALYSIS\TUBES\scores.json"

# Variabel global
questions = []
scores = {}
current_user = None

# Fungsi untuk memuat soal dari file JSON
def load_questions():
    global questions
    try:
        if os.path.exists(DATA_FILE):  # Cek apakah file ada
            with open(DATA_FILE, "r") as file:
                questions = json.load(file)
                if not isinstance(questions, list):  # Pastikan questions adalah list
                    questions = []
        else:
            questions = []
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan saat memuat soal: {e}")
        questions = []

# Fungsi untuk menyimpan soal ke file JSON
def save_questions():
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(questions, file, indent=4)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan saat menyimpan soal: {e}")

# Fungsi untuk memuat skor dari file JSON
def load_scores():
    global scores
    try:
        if os.path.exists(SCORE_FILE):  # Cek apakah file skor ada
            with open(SCORE_FILE, "r") as file:
                scores = json.load(file)
        else:
            scores = {}
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan saat memuat skor: {e}")
        scores = {}

# Fungsi untuk menyimpan skor ke file JSON
def save_scores():
    try:
        with open(SCORE_FILE, "w") as file:
            json.dump(scores, file, indent=4)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan saat menyimpan skor: {e}")

# Fungsi login
def login():
    global current_user
    username = username_entry.get()
    password = password_entry.get()

    user = USER_DATA.get(username)
    if user and user["password"] == password:
        current_user = {"username": username, "role": user["role"]}
        messagebox.showinfo("Login Berhasil", f"Selamat datang, {username}!")
        main_menu()
    else:
        messagebox.showerror("Login Gagal", "Username atau password salah!")

# Menu utama
def main_menu():
    clear_screen()
    tk.Label(root, text=f"Menu Utama ({current_user['role'].capitalize()})", font=("Arial", 16)).pack(pady=20)

    if current_user["role"] == "teacher":
        tk.Button(root, text="Tampilkan Soal", command= display_questions).pack(pady=10)
        tk.Button(root, text="Tambah Soal", command=add_question).pack(pady=10)
        tk.Button(root, text="Edit Soal", command=edit_question).pack(pady=10)
        tk.Button(root, text="Hapus Soal", command=delete_question).pack(pady=10)
        tk.Button(root, text="Lihat Nilai Murid", command=view_scores).pack(pady=10)
    elif current_user["role"] == "student":
        tk.Button(root, text="Mulai Kuis", command=start_quiz).pack(pady=10)
        tk.Button(root, text="Lihat Skor Saya", command=view_my_score).pack(pady=10)

    tk.Button(root, text="Logout", command=logout).pack(pady=10)

# Bersihkan layar
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

# Logout
def logout():
    global current_user
    current_user = None
    clear_screen()
    init_login_screen()

# Tambah soal
def add_question():
    try:
        # Input pertanyaan
        question = simpledialog.askstring("Tambah Soal", "Masukkan pertanyaan:")
        if not question:  # Jika input kosong atau ditekan cancel
            messagebox.showwarning("Peringatan", "Pertanyaan tidak boleh kosong!")
            return
        
        # Input pilihan jawaban
        options = []
        for i in range(1, 5):
            option = simpledialog.askstring("Tambah Soal", f"Masukkan pilihan {i}:")
            if not option:  # Jika salah satu pilihan kosong
                messagebox.showwarning("Peringatan", f"Pilihan {i} tidak boleh kosong!")
                return
            options.append(option)
        
        # Input nomor jawaban benar
        correct_option = simpledialog.askinteger("Tambah Soal", "Masukkan nomor jawaban benar (1-4):")
        if correct_option is None:  # Jika dialog dibatalkan
            messagebox.showwarning("Peringatan", "Nomor jawaban tidak boleh kosong!")
            return
        if correct_option not in [1, 2, 3, 4]:  # Validasi rentang input
            messagebox.showwarning("Peringatan", "Jawaban benar harus antara 1-4!")
            return

        # Tambahkan soal ke list
        questions.append({
            "question": question,
            "options": options,
            "answer": correct_option
        })

        # Simpan soal ke file
        save_questions()
        messagebox.showinfo("Sukses", "Soal berhasil ditambahkan!")

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

#Tampilkan soal
def display_questions():
    if not questions:
        messagebox.showwarning("Peringatan", "Belum ada soal yang ditambahkan!")
        return

    # Bangun teks untuk menampilkan semua soal
    question_text = ""
    for idx, question in enumerate (questions):
        question_text += f"Soal {idx + 1}:\n{question['question']}\n"
        for i, option in enumerate (question ["options"], start=1):
            question_text += f" {i}. {option}\n"
        question_text += f"Jawaban Benar: Pilihan {question['answer']}\n\n"
            
    #Tampilkan semua soal di dalam pop-up
    messagebox.showinfo("Daftar Soal", question_text)

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
                questions[index - 1] = {"question": question, "options": options, "answer": correct_option}
                save_questions()
                messagebox.showinfo("Sukses", "Soal berhasil diubah!")
            else:
                messagebox.showwarning("Peringatan", "Input tidak valid!")
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
            save_questions()
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
            scores[current_user["username"]] = score
            save_scores()
            main_menu()
            return

        clear_screen()
        question = questions[index]
        tk.Label(root, text=f"Soal {index + 1}: {question['question']}", wraplength=400, font=("Arial", 14)).pack(pady=20)
        selected_option = tk.IntVar(value=0)

        for i, option in enumerate(question["options"]):
            tk.Radiobutton(root, text=option, variable=selected_option, value=i + 1).pack(anchor="w", padx=20)

        def submit_answer():
            if selected_option.get() == question["answer"]:
                next_question(index + 1, score + 1)
            else:
                next_question(index + 1, score)

        tk.Button(root, text="Submit", command=submit_answer).pack(pady=20)

    next_question(0, 0)

# Lihat skor sendiri
def view_my_score():
    score = scores.get(current_user["username"], 0)
    messagebox.showinfo("Skor Saya", f"Skor Anda: {score}")

# Lihat skor semua murid (khusus teacher)
def view_scores():
    if current_user["role"] != "teacher":
        messagebox.showerror("Error", "Akses ditolak!")
        return

    if not scores:
        messagebox.showinfo("Skor Murid", "Belum ada murid yang mengikuti kuis.")
    else:
        score_text = "\n".join([f"{username}: {score}" for username, score in scores.items()])
        messagebox.showinfo("Skor Murid", f"Skor Murid:\n{score_text}")

# Inisialisasi aplikasi
def init_login_screen():
    global username_entry, password_entry

    clear_screen()
    tk.Label(root, text="Login", font=("Arial", 20)).pack(pady=20)

    tk.Label(root, text="Username:").pack()
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)

    tk.Label(root, text="Password:").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    tk.Button(root, text="Login", command=login).pack(pady=20)

    load_questions()
    load_scores()

# Setup tkinter root window
root = tk.Tk()
root.title("Quiz Application")
root.geometry("500x400")

init_login_screen()

root.mainloop()
