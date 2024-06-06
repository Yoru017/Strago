import tkinter as tk
from tkinter import ttk
import time

def calculate_greedy_combinations():
    start_time = time.time()
    
    coin_values = coin_entry.get().split(',')
    coin_values = [int(coin.strip()) for coin in coin_values]
    target_amount = int(amount_entry.get())
    result = []
    
    coin_values.sort(reverse=True)

    original_target = target_amount 
    for coin in coin_values:
        if coin == 0:
            break
        else:
            while target_amount >= coin:
                target_amount -= coin
                result.append(coin)
        
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Clear the result text area
    result_text.delete(1.0, tk.END)
    
    # Check if there is any leftover amount (indicating no solution)
    if target_amount != 0:
        result_text.insert(tk.END, f"Tidak ada kombinasi koin yang memenuhi jumlah {original_target} dengan koin yang diberikan.\n")
    else:
        result_text.insert(tk.END, f"Kombinasi koin untuk jumlah {original_target} adalah: {result}\n")

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
calculate_button = ttk.Button(mainframe, text="Hitung Kombinasi (Greedy)", command=calculate_greedy_combinations)
calculate_button.grid(column=2, row=3, sticky=tk.W)

# Result text area
result_text = tk.Text(mainframe, width=100, height=80)
result_text.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

# Configure grid
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
