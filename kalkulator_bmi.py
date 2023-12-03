import tkinter as tk
from tkinter import ttk
from rumus import hitung_bmi, bb_status, ideal_bb
import time

class BMIKalkulator:
    def __init__(self, root):
        self.root = root
        self.root.title('Kalkulator BMI')
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self.root, text='\nMari Hitung Skor BMI mu')
        self.label.pack()

        self.gender_label = ttk.Label(self.root, text='Pilih Gender Anda:')
        self.gender_label.pack()

        self.gender = tk.StringVar()
        self.gender_menu = ttk.OptionMenu(self.root, self.gender, 'Laki-Laki', 'Laki-Laki', 'Perempuan')
        self.gender_menu.pack()

        self.tb_label = ttk.Label(self.root, text='Tinggi Badan (cm):')
        self.tb_label.pack()

        self.tb_var = tk.StringVar()
        self.tb_entry = ttk.Entry(self.root, textvariable=self.tb_var)
        self.tb_entry.pack()

        self.bb_label = ttk.Label(self.root, text='Berat Badan (kg):')
        self.bb_label.pack()

        self.bb_var = tk.StringVar()
        self.bb_entry = ttk.Entry(self.root, textvariable=self.bb_var)
        self.bb_entry.pack()

        self.hitung_button = ttk.Button(self.root, text='Hitung', command=self.hitung)
        self.hitung_button.pack()

        self.reset_button = ttk.Button(self.root, text='Reset', command=self.reset)
        self.reset_button.pack()

        self.hasil_label = ttk.Label(self.root, text='')
        self.hasil_label.pack()

    def hitung(self):
        try:
            tb = float(self.tb_var.get())
            bb = float(self.bb_var.get())

            #nested loop hitung waktu mundur
            for i in range(3, 0, -1):
                self.hasil_label.config(text=f'Menghitung data anda... {i}')
                self.root.update()
                time.sleep(1)

            #menghitung BMI, BB status, dan ideal BB
            bmi = hitung_bmi(tb, bb)
            bb_stat = bb_status(bmi)
            ideal_bb_kg = ideal_bb(tb, bb, self.gender.get())
            self.hasil_label.config(text=f'Skor BMI: {bmi:.2f}\nStatus: {bb_stat}\nTarget Berat Badan Ideal: {ideal_bb_kg:.2f} kg')
        
        #error handling
        except ValueError:
            self.hasil_label.config(text='Error: Masukkan angka')

    def reset(self):
        self.hasil_label.config(text='')
        self.tb_var.set('')
        self.bb_var.set('')
        self.gender.set('Laki-Laki')

def main():
    root = tk.Tk()
    bmi_kalkulator = BMIKalkulator(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
