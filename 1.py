from queue import Queue
import random

queue = Queue()

class StopCycle(Exception): pass

def generate_request():
    if queue.qsize() > 10:
        print('Queue overflow')
        return

    for i in range(0, random.randint(1, 4)):
        id = random.randint(0, 100)
        queue.put(f"Application {id}")
        print(f"Application {id} added to queue")

def process_request():
    for i in range(0, random.randint(1, 4)):
        if queue.empty():
            print('Queue is empty')
            raise StopCycle

        last = queue.get()
        print(f"{last} processed")

try:
    while True:
        generate_request()
        process_request()
except StopCycle:
    pass