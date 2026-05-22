import tkinter as tk
from tkinter import messagebox

#teks file
USER_FILE = "users.txt"
JADWAL_FILE = "jadwal.txt"

#warna dan font
FONT_JUDUL = ("Segoe UI", 18, "bold")
FONT_LABEL = ("Segoe UI", 11)
FONT_ENTRY = ("Segoe UI", 11)
BG_MAIN = "#f0f4f8"
BG_FRAME = "#ffffff"

#Registrasi
def register_user():
    username = entry_reg_user.get()
    password = entry_reg_pass.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Data tidak boleh kosong")
        return

    with open(USER_FILE, "a") as file:
        file.write(f"{username}|{password}\n")

    messagebox.showinfo("Sukses", "Registrasi berhasil!")
    reg_window.destroy()

#login ulang
def login_user():
    username = entry_login_user.get()
    password = entry_login_pass.get()

    try:
        with open(USER_FILE, "r") as file:
            for line in file:
                user, pw = line.strip().split("|")
                if username == user and password == pw:
                    messagebox.showinfo("Login", "Login Berhasil")
                    login_window.destroy()
                    main_menu()
                    return
    except FileNotFoundError:
        pass

    messagebox.showerror("Login Gagal", "Username atau Password salah")

#simpan jadwal
def simpan_jadwal():
    data = f"{kelas.get()}|{hari.get()}|{jam.get()}|{matkul.get()}|{dosen.get()}|{ruang.get()}\n"
    with open(JADWAL_FILE, "a") as file:
        file.write(data)

    messagebox.showinfo("Sukses", "Jadwal berhasil disimpan")

#tampilan jadwal
def tampil_jadwal():
    text_jadwal.delete("1.0", tk.END)
    try:
        with open(JADWAL_FILE, "r") as file:
            for line in file:
                kelas, hari, jam, mk, dosen, ruang = line.strip().split("|")
                text_jadwal.insert(tk.END, f"""
Kelas   : {kelas}
Hari    : {hari}
Jam     : {jam}
Matkul  : {mk}
Dosen   : {dosen}
Ruangan : {ruang}
----------------------------------------
""")
    except FileNotFoundError:
        messagebox.showerror("Error", "File jadwal tidak ditemukan")

#menu utama
def main_menu():
    root = tk.Tk()
    root.title("Aplikasi Jadwal Mata Kuliah")
    root.geometry("1000x750")
    root.configure(bg=BG_MAIN)

#menu bar
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Keluar", command=root.destroy)
    menu_bar.add_cascade(label="File", menu=file_menu)

    jadwal_menu = tk.Menu(menu_bar, tearoff=0)
    jadwal_menu.add_command(label="Lihat Jadwal", command=tampil_jadwal)
    menu_bar.add_cascade(label="Jadwal", menu=jadwal_menu)

#Judul
    tk.Label(root, text="INPUT JADWAL MATA KULIAH",
             font=FONT_JUDUL, bg=BG_MAIN).pack(pady=20)

#Frame Input   
    frame = tk.Frame(root, bg=BG_FRAME, padx=30, pady=20)
    frame.pack()

    global kelas, hari, jam, matkul, dosen, ruang, text_jadwal

    kelas = tk.StringVar()
    hari = tk.StringVar()
    jam = tk.StringVar()
    matkul = tk.StringVar()
    dosen = tk.StringVar()
    ruang = tk.StringVar()

    labels = ["Kelas", "Hari", "Jam", "Mata Kuliah", "Dosen", "Ruangan"]
    vars_ = [kelas, hari, jam, matkul, dosen, ruang]

    for i, (lbl, var) in enumerate(zip(labels, vars_)):
        tk.Label(frame, text=lbl, font=FONT_LABEL, bg=BG_FRAME)\
            .grid(row=i, column=0, sticky="w", pady=5)
        tk.Entry(frame, textvariable=var, font=FONT_ENTRY, width=30)\
            .grid(row=i, column=1, pady=5)

    tk.Button(frame, text="Simpan Jadwal", font=FONT_LABEL,
              bg="#4CAF50", fg="white", width=20,
              command=simpan_jadwal).grid(row=6, column=1, pady=15)

    #Area Teks Jadwal   
    text_jadwal = tk.Text(root, width=110, height=20,
                          font=("Arial", 12))
    text_jadwal.pack(pady=20)

    root.mainloop()

#Registrasi Window
def open_register():
    global reg_window, entry_reg_user, entry_reg_pass

    reg_window = tk.Toplevel()
    reg_window.title("Registrasi")
    reg_window.geometry("400x300")
    reg_window.configure(bg=BG_MAIN)

    tk.Label(reg_window, text="REGISTRASI",
             font=FONT_JUDUL, bg=BG_MAIN).pack(pady=20)

    tk.Label(reg_window, text="Username", font=FONT_LABEL, bg=BG_MAIN).pack()
    entry_reg_user = tk.Entry(reg_window, font=FONT_ENTRY)
    entry_reg_user.pack()

    tk.Label(reg_window, text="Password", font=FONT_LABEL, bg=BG_MAIN).pack(pady=5)
    entry_reg_pass = tk.Entry(reg_window, show="*", font=FONT_ENTRY)
    entry_reg_pass.pack()

    tk.Button(reg_window, text="Daftar", font=FONT_LABEL,
              bg="#2196F3", fg="white",
              command=register_user).pack(pady=20)

#Login Window
login_window = tk.Tk()
login_window.title("Login Jadwal Kuliah")
login_window.geometry("400x300")
login_window.configure(bg=BG_MAIN)

tk.Label(login_window, text="LOGIN",
         font=FONT_JUDUL, bg=BG_MAIN).pack(pady=20)

tk.Label(login_window, text="Username", font=FONT_LABEL, bg=BG_MAIN).pack()
entry_login_user = tk.Entry(login_window, font=FONT_ENTRY)
entry_login_user.pack()

tk.Label(login_window, text="Password", font=FONT_LABEL, bg=BG_MAIN).pack(pady=5)
entry_login_pass = tk.Entry(login_window, show="*", font=FONT_ENTRY)
entry_login_pass.pack()

tk.Button(login_window, text="Login", font=FONT_LABEL,
          bg="#4CAF50", fg="white",
          command=login_user).pack(pady=10)

tk.Button(login_window, text="Registrasi", font=FONT_LABEL,
          command=open_register).pack()

login_window.mainloop()

