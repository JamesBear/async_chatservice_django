
import threading
import queue
import time

bot_started = False
thread = None
SLEEP_INTERVAL = 1.0
BATCH_SIZE = 20

def naive_process_messages(msg_list):
    for item in msg_list:
        sender, msg, reply = item
        reply = 'Hi {}. Did you just say "{}"?'.format(sender, msg)
        item[2] = reply

def process_messages(msg_list):
    naive_process_messages(msg_list)

def run_chatbot():
    global msg_queue, terminate_signal
    print('thread: run_chatbot started')
    while True:
        qsize = msg_queue.qsize()
        if qsize > 0:
            n_batch = min(BATCH_SIZE, qsize)
            msgs = []
            for i in range(n_batch):
                item = msg_queue.get(block=False)
                msgs.append(item)
            process_messages(msgs)
        else:
            time.sleep(SLEEP_INTERVAL)

def try_start_bot():
    global bot_started, thread, msg_queue, terminate_signal
    if bot_started:
        return
    bot_started = True
    terminate_signal = False
    msg_queue = queue.Queue()
    thread = threading.Thread(target=run_chatbot, daemon=True)
    thread.start()

def push_message(message_obj):
    global msg_queue
    msg_queue.put(message_obj)