from multiprocessing import Process, Queue
import time
import datetime
import codecs


def print_w_time(message):
    print(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] {message}')


def process_a(input_queue, output_queue):
    try:
        while True:
            message = input_queue.get()
            if message is None:
                break
            processed_message = message.lower()
            output_queue.put(processed_message)
            time.sleep(5)
    except KeyboardInterrupt:
        return


def process_b(input_queue, main_queue):
    try:
        while True:
            message = input_queue.get()
            encoded_message = codecs.encode(message, "rot_13")
            print_w_time(encoded_message)
            main_queue.put(encoded_message)
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    queue_a = Queue()
    queue_b = Queue()
    queue_main = Queue()

    proc_a = Process(target=process_a, args=(queue_a, queue_b))
    proc_b = Process(target=process_b, args=(queue_b, queue_main))

    proc_a.start()
    proc_b.start()

    try:
        while True:
            input_message = input()
            queue_a.put(input_message)
            encoded_message = queue_main.get()
            print_w_time(f"Received from B: {encoded_message}")
    except KeyboardInterrupt:
        queue_a.put(None)

    proc_a.join()
    proc_b.join()
