import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
import collections


def flash_sort(arr):
    n = len(arr)
    m = int(0.45 * n)
    l = 0
    r = n - 1
    k = int(flash_partition(arr, m, l, r))
    while k != m:
        if k > m:
            r = k - 1
            k = int(flash_partition(arr, m, l, r))
        else:
            l = k + 1
            k = int(flash_partition(arr, m, l, r))
    flash_sort_helper(arr, 0, m)
    flash_sort_helper(arr, m + 1, n - 1)
    return arr

def flash_partition(arr, m, l, r):
    i = l
    j = r
    pivot = arr[int((l + r) / 2)]
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return i

def flash_sort_helper(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        flash_sort_helper(arr, low, pi - 1)
        flash_sort_helper(arr, pi + 1, high)

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def sort_data():
    try:
        data = [int(x) for x in input_text.get().split(', ')]
        sorted_data = flash_sort(data)
        output_text.config(state='normal')
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, str(sorted_data))
        output_text.config(state='normal')
        with open("sorted_data.txt", "w") as file:
            file.write(str(sorted_data))
        plt.hist(sorted_data, edgecolor='green', color='purple', bins=100, linewidth=1, rwidth=1)
        plt.xticks(range(min(sorted_data), max(sorted_data)+1, 100))

        plt.xlabel("Data Value")
        plt.ylabel("# Of Occurrences")
        plt.show()
    except ValueError:
        messagebox.showerror("Error", "Invalid Input, Please enter a list of integers separated by a ', ' and space")
        clear_button = ttk.Button(root, text="Clear", command=clear_data)
        clear_button.grid(row=1, column=0, padx=10, pady=10)

    counts = collections.Counter(sorted_data)


def clear_data():
        input_text.delete(0, 'end')
        output_text.config(state='normal')
        output_text.delete(1.0, tk.END)
        output_text.config(state='disable')

root = tk.Tk()
root.title("Better Sort")

input_label = tk.Label(root, text="Enter the dataset (separated by a comma and space) :")
input_label.grid(row=0, column=0, padx=10, pady=10)

input_text = tk.Entry(root)
input_text.grid(row=0, column=1, padx=10, pady=10)

sort_button = tk.Button(root, text="Sort", command=sort_data)
sort_button.grid(row=1, column=0, padx=10, pady=10)


clear_button = ttk.Button(root, text="Clear", command=clear_data)
clear_button.grid(row=1, column=1, padx=10, pady=10)

output_label = tk.Label(root, text="Sorted Dataset:")
output_label.grid(row=2, column=0, padx=10, pady=10)

output_text = tk.Text(root, height=5, width=30, state='disable')
output_text.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()