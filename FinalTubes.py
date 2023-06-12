import tkinter as tk
from tkinter import messagebox
from timeit import default_timer as timer

#Tugas Besar Strategi Algoritma

"""
KELOMPOK 8
Muhammad Ali Akbar Filayati (1301204493)
Dhandy Faridsyah Akbar (1301204356)
Virdi Rizky Elnanda (1301210490)
"""


def brute_force_encrypt(text, shift):
    start=timer()
    encrypted = ""
    for c in text:
        if c.isalpha():
            new_char_code = ord(c) + shift
            if c.isupper():
                if new_char_code > ord('Z'):
                    new_char_code -= 26
                encrypted += chr(new_char_code)
            else:
                if new_char_code > ord('z'):
                    new_char_code -= 26
                encrypted += chr(new_char_code)
        else:
            encrypted += c
    end=timer()
    print(end-start, 's')
    return encrypted


def brute_force_decrypt(text, shift):
    start=timer()
    decrypted = ""
    for c in text:
        if c.isalpha():
            new_char_code = ord(c) - shift
            if c.isupper():
                if new_char_code < ord('A'):
                    new_char_code += 26
                decrypted += chr(new_char_code)
            else:
                if new_char_code < ord('a'):
                    new_char_code += 26
                decrypted += chr(new_char_code)
        else:
            decrypted += c
    end=timer()
    print(end-start, 's')
    return decrypted


def greedy_encrypt(text):
    start=timer()
    encrypted = ""
    letter_counts = [0] * 26 #bikin array 26 index dengan nilai masing2 elemen 0

   
    for c in text:
        if c.isalpha():
            index = ord(c.lower()) - ord('a')
            letter_counts[index] += 1

    
    max_count = max(letter_counts)
    max_index = letter_counts.index(max_count)

    
    shift = (max_index - (ord('e') - ord('a'))) % 26 #ngitung shift

   
    for c in text:
        if c.isalpha():
            new_char_code = ord(c) + shift
            if c.isupper():
                if new_char_code > ord('Z'):
                    new_char_code -= 26
                encrypted += chr(new_char_code)
            else:
                if new_char_code > ord('z'):
                    new_char_code -= 26
                encrypted += chr(new_char_code)
        else:
            encrypted += c
    end=timer()
    print(end-start, 's')
    return encrypted


def greedy_decrypt(text):
    start=timer()
    decrypted = ""
    letter_counts = [0] * 26

    
    for c in text:
        if c.isalpha():
            index = ord(c.lower()) - ord('a')
            letter_counts[index] += 1

    
    max_count = max(letter_counts)
    max_index = letter_counts.index(max_count)

    
    shift = (max_index - (ord('e') - ord('a'))) % 26

    
    for c in text:
        if c.isalpha():
            new_char_code = ord(c) - shift
            if c.isupper():
                if new_char_code < ord('A'):
                    new_char_code += 26
                decrypted += chr(new_char_code)
            else:
                if new_char_code < ord('a'):
                    new_char_code += 26
                decrypted += chr(new_char_code)
        else:
            decrypted += c
    end=timer()
    print(end-start, 's')
    return decrypted


def process_message():
    message = message_entry.get()
    shift = shift_entry.get()
    try:
        shift = int(shift)
    except ValueError:
        messagebox.showerror("Error", "Shift must be an integer")
        return

    # Perform encryption or decryption based on the selected method
    if method_var.get() == 1:
        result = brute_force_encrypt(message, shift)
    elif method_var.get() == 2:
        result = brute_force_decrypt(message, shift)
    elif method_var.get() == 3:
        result = greedy_encrypt(message)
    else:
        result = greedy_decrypt(message)

    # Display the result
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, result)


# create the main window
window = tk.Tk()
window.title("Caesar Cipher Encryption and Decryption")
window.geometry("800x400")

# create the input widgets
message_label = tk.Label(window, text="Enter the message:")
message_label.pack()
message_entry = tk.Entry(window)
message_entry.pack()

shift_label = tk.Label(window, text="Enter the shift:")
shift_label.pack()
shift_entry = tk.Entry(window)
shift_entry.pack()

# create a radio button for method selection
method_var = tk.IntVar()
encrypt_radio = tk.Radiobutton(window, text="Brute Force Encrypt", variable=method_var, value=1)
encrypt_radio.pack()
decrypt_radio = tk.Radiobutton(window, text="Brute Force Decrypt", variable=method_var, value=2)
decrypt_radio.pack()
greedy_encrypt_radio = tk.Radiobutton(window, text="Greedy Encrypt", variable=method_var, value=3)
greedy_encrypt_radio.pack()
greedy_decrypt_radio = tk.Radiobutton(window, text="Greedy Decrypt", variable=method_var, value=4)
greedy_decrypt_radio.pack()

# create the button to start the encryption/decryption process
process_button = tk.Button(window, text="Process", command=process_message)
process_button.pack()

# create the output widgets
output_label = tk.Label(window, text="Result:")
output_label.pack()
output_text = tk.Text(window)
output_text.pack()

# start the event loop
window.mainloop()

