current_stack = []

current_stack.append(5)
current_stack.append(7)
current_stack.append(2)

# Last In First Out
# Terakhir Masuk Keluar Lebih Dulu
# Seperti tumpukan piring

print(current_stack.pop())
print(current_stack.pop())
print(current_stack.pop())

if len(current_stack) == 0:
    print("Stack is empty")
else:
    print(len(current_stack))
