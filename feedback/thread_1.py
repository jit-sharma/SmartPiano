import _thread as t

mu = t.allocate_lock()
n = 0

def hello():
    print("Hello Jit")
    mu.release()
    t.exit()
    

for i in range(20):
    t.start_new_thread(hello,())
