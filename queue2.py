current_queue = []

current_queue.append(5)
current_queue.append(7)
current_queue.append(2)

# Queue: First In First Out
# Masuk lebih dulu keluar lebih dulu
# Seperti antrian

print(current_queue.pop(0))
print(current_queue.pop(0))
print(current_queue.pop(0))

if len(current_queue) == 0:
    print("Queue is empty")
else:
    print(len(current_queue))
