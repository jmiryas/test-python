# Membuat empty stack

current_stack = []

# Menambahkan nilai

current_stack.append(5)
current_stack.append(7)
current_stack.append(2)

# Konsep:
# Last In First Out
# Terakhir Masuk Keluar Lebih Dulu
# Seperti tumpukan piring

# Mengeluarkan nilai dari stack

print(current_stack.pop())
print(current_stack.pop())
print(current_stack.pop())

# Jika stack empty, tampilkan empty
# Selain itu, tampilkan panjangnya

if len(current_stack) == 0:
    print("Stack is empty")
else:
    print(len(current_stack))
