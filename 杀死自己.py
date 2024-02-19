import threading
import multiprocessing
import tkinter as tk
import time
def process():
    # window = tk.Tk()  # 创建一个窗口，因为后面还要用到所以用window这个变量来赋值，可以自行更改
    #
    # window.title('你关不掉的我~~')
    # window.mainloop()  # 必须一直更新窗口，不然会未响应，如果要自行更新，可以用window.update()
    print('hello,world')

#控制发送数量
def scapy_ping_10k():
    while True:
        process()

#控制并发数量
def scapy_ping_dos(count):
    pool=multiprocessing.Pool(processes=count)
    while True:
        pool.apply_async(scapy_ping_10k,(count,))
        dos()
def dos():
    while True:
        pro=threading.Thread(target=scapy_ping_10k)
        pro.start()
if __name__ == '__main__':
    scapy_ping_dos(20000)