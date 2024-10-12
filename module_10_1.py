import threading
from time import sleep


def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(word_count):
            f.write('Какое-то слово № %d\n' % (i + 1))
            sleep(0.1)
    print("Завершилась запись в файл", file_name)


def main():
    import time

    # Без потоков
    t1 = time.time()
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')
    t2 = time.time()
    print("Без потоков:", t2 - t1)

    # С потоками
    threads = []
    t3 = time.time()
    for i in range(4):
        filename = f'example{i + 5}.txt'
        word_count = {0: 10, 1: 30, 2: 200, 3: 100}[i]
        thread = threading.Thread(target=write_words, args=(word_count, filename))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    t4 = time.time()
    print("С потоками:", t4 - t3)
import threading
from time import sleep


def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(word_count):
            f.write('Какое-то слово № %d\n' % (i + 1))
            sleep(0.1)
    print("Завершилась запись в файл", file_name)


def main():
    import time

    # Без потоков
    t1 = time.time()
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')
    t2 = time.time()
    print("Без потоков:", t2 - t1)

    # С потоками
    threads = []
    t3 = time.time()
    for i in range(4):
        filename = f'example{i + 5}.txt'
        word_count = {0: 10, 1: 30, 2: 200, 3: 100}[i]
        thread = threading.Thread(target=write_words, args=(word_count, filename))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    t4 = time.time()
    print("С потоками:", t4 - t3)


if __name__ == "__main__":
    main()

