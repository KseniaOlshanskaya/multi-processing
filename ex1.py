from concurrent.futures import ThreadPoolExecutor, as_completed
from declarative_part import *
from multiprocessing import Process
from threading import Thread
from queue import Queue

import time

def main():
    p = ProcessRunner()
    time1 = time.time()
    process1 = Process(target=p.read(1, p))
    process1.start()
    process1.join()
    time2 = time.time()
    print("Первый процесс (последовательно):" + str(time2 - time1))

    p2 = ProcessRunner()
    time1 = time.time()
    process2 = Process(target=p2.read(2, p2))
    process2.start()
    process2.join()
    time2 = time.time()
    print("Второй процесс (многопоточно c очередью): " + str(time2 - time1))

    p3 = ProcessRunner()
    time1 = time.time()
    process3 = Process(target=p3.read(3, p3))
    process3.start()
    process3.join()
    time2 = time.time()
    print("Третий процесс (многопоточно c блокировками): " + str(time2 - time1))

if __name__ == "__main__":
    main()
