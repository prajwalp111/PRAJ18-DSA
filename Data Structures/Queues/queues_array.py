MAX = 5

Queue = [None] * MAX
front = 0
rear = 0


def is_empty():
    return front == rear


def is_full():
    return (rear + 1) % MAX == front


def enqueue(item):
    global rear

    if is_full():
        raise IndexError("Queue is full")

    Queue[rear] = item
    rear = (rear + 1) % MAX


def dequeue():
    global front

    if is_empty():
        raise IndexError("Queue is empty")

    item = Queue[front]
    Queue[front] = None
    front = (front + 1) % MAX

    return item


def peek():
    if is_empty():
        raise IndexError("Queue is empty")

    return Queue[front]

enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)

print("Queue:", Queue)

print("Peek:", peek())

print("Dequeue:", dequeue())
print("Dequeue:", dequeue())

enqueue(50)
enqueue(60)

print("Queue:", Queue)
print("Peek:", peek())

print("Dequeue:", dequeue())
print("Dequeue:", dequeue())