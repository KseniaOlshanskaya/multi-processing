from multiprocessing import Process
from declarative_part import *


def main():
    p = ProcessRunner()
    process1 = Process(target=p.read(1, p))
    process1.start()

    p2 = ProcessRunner()
    process2 = Process(target=p2.read(2, p2))
    process2.start()

    p3 = ProcessRunner()
    process3 = Process(target=p3.third_process(p3))
    process3.start()

    process1.join()
    process2.join()
    process3.join()


if __name__ == "__main__":
    main()

