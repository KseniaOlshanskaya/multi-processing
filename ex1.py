from declarative_part import *
from multiprocessing import Process, freeze_support
import time

def main():
    p = ProcessRunner()
    time1 = time.time()
    process1 = Process(target=p.first_process())
    process1.start()
    process1.join()
    time2 = time.time()
    print(time2 - time1)

if __name__ == "__main__":
    main()
