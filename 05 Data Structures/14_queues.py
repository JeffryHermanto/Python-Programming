# Queues

# FIFO
# First In First Out

from collections import deque

queue = deque([])

queue.append(1)
queue.append(2)
queue.append(3)

queue.popleft()
print(queue)

queue.clear()
if not queue:
    print("Empty")
