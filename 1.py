from queue import Queue
import random

queue = Queue()
id = 1

class StopCycle(Exception): pass

def generate_request():
    if queue.qsize() > 10:
        print('Queue overflow')
        return

    global id
    queue.put(f"Application {id}")
    print(f"Application {id} added to queue")
    id += 1

def process_request():
    if queue.empty():
        print('Queue is empty')
        raise StopCycle

    last = queue.get()
    print(f"{last} processed")

try:
    while True:
        for i in range(0, random.randint(1, 4)):
            generate_request()

        for i in range(0, random.randint(1, 4)):
            process_request()
except StopCycle:
    pass