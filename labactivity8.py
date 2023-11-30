def create_Q():
    Q = []
    return Q

def is_empty(Q):
    return len(Q) == 0

def enqueue(Q, item):
    Q.append(item)
    print("Enqueued Element: " + item)

def dequeue(Q):
    if (is_empty(Q)):
        return "The queue is empty"
    return Q.dequeue()
queue = create_Q()
enqueue(queue, str(1))
enqueue(queue, str(2))
enqueue(queue, str(3))
enqueue(queue, str(4))
enqueue(queue, str(5))
print("The elements in the queue are:"+ str(queue))