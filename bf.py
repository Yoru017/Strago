import tkinter as tk
from tkinter import ttk
import time

def find_combinations(coins, target, combination, start_index):
    if target == 0:
        result.append(combination.copy())
        return
    if target < 0:
        return
    for i in range(start_index, len(coins)):
        combination.append(coins[i])
        find_combinations(coins, target - coins[i], combination, i)
        combination.pop()

def calculate_combinations():
    start_time = time.time()
    
    coin_values = coin_entry.get().split(',')
    coin_values = [int(coin.strip()) for coin in coin_values]
    target_amount = int(amount_entry.get())
    
    result.clear()
    find_combinations(coin_values, target_amount, [], 0)
    
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Clear the result text area
    result_text.delete(1.0, tk.END)
    
    if not result:
        result_text.insert(tk.END, f"Tidak ada kombinasi koin yang memenuhi jumlah {target_amount} dengan koin yang diberikan.\n")
    else:
        result_text.insert(tk.END, f"Kombinasi koin untuk jumlah {target_amount} adalah:\n")
        min_combination = min(result, key=len)  # Mencari kombinasi koin dengan jumlah koin terkecil
        for combination in result:
            if combination == min_combination:  # Menambahkan keterangan untuk kombinasi minimum
                result_text.insert(tk.END, f"{combination} (minimum)\n")
            else:
                result_text.insert(tk.END, f"{combination}\n")
    
    show_time_window(elapsed_time)

def show_time_window(elapsed_time):
    time_window = tk.Toplevel(root)
    time_window.title("Waktu Running")
    ttk.Label(time_window, text=f"Waktu running: {elapsed_time:.6f} detik").pack(padx=20, pady=20)
    ttk.Button(time_window, text="Tutup", command=time_window.destroy).pack(pady=10)

# Setup GUI
root = tk.Tk()
root.title("Coin Change Problem Solver")

mainframe = ttk.Frame(root, padding="10 10 20 20")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Coin entry
ttk.Label(mainframe, text="Masukkan nilai koin (dipisahkan dengan koma):").grid(column=1, row=1, sticky=tk.W)
coin_entry = ttk.Entry(mainframe, width=40)
coin_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

# Amount entry
ttk.Label(mainframe, text="Masukkan jumlah uang yang akan ditukar:").grid(column=1, row=2, sticky=tk.W)
amount_entry = ttk.Entry(mainframe, width=40)
amount_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))

# Calculate button
calculate_button = ttk.Button(mainframe, text="Hitung Kombinasi", command=calculate_combinations)
calculate_button.grid(column=2, row=3, sticky=tk.W)

# Result text area
result_text = tk.Text(mainframe, width=100, height=60)
result_text.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

# Configure grid
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

result = []

root.mainloop()
