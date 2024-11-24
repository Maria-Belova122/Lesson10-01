# ЗАДАНИЕ ПО ТЕМЕ "Введение в потоки"

import threading
from time import sleep, time


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start_time1 = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
finish_time1 = time()
print(f'Работа потоков: {round((finish_time1 - start_time1), 6)} сек.')

start_time2 = time()
# Создаём потоки для 4 вызовов функции
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
# Запускаем потоки
thread1.start()
thread2.start()
thread3.start()
thread4.start()
# Ждём завершения потоков
thread1.join()
thread2.join()
thread3.join()
thread4.join()
finish_time2 = time()
print(f'Работа потоков: {round((finish_time2 - start_time2), 6)} сек.')