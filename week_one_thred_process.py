import threading
from multiprocessing import Process
import os
 
def foo():
    print('thread id', threading.get_native_id())
    print('process id', os.getpid())
 
def bar():
     print('This is bar')

def baz():
    print('This is baz')
   
if __name__ == '__main__':
    child1 = Process(target=foo).start()
    child2 = Process(target=bar).start()
    child3 = Process(target=baz).start()
 
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=foo).start()
    thread3 = threading.Thread(target=foo).start()

# thread id 14176
# process id 3104
# thread id 6696
# process id 3104
# thread id 3424
# process id 3104
# thread id 9024
# process id 8604
# This is bar
# This is baz

