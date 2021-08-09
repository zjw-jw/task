#coding=utf-8
import threading
import time
def apple_1():
    print("苹果1")
    time.sleep(2)
    print(time.strftime("%Y-%m-%d %H-%M-%S",time.localtime()))
def apple_2():
    print("苹果2")
    time.sleep(2)
    print(time.strftime("%Y-%m-%d %H-%M-%S",time.localtime()))
def main():

    thread2=threading.Thread(target=apple_2())

    thread2.start()    #让线程开始
    thread2.join()
    thread = threading.Thread(target=apple_1())
    thread.start()
    thread.join()   #让其他线程等待自己执行完成再往下执行
    print("苹果3")
    print(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()))
    print("有多少个小丑？",threading.active_count())
    print("这些小丑是谁呢？",threading.enumerate())

if __name__ =="__main__":
    main()