import threading
from threading import Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            amount_to_add = randint(50, 500)
            self.balance += amount_to_add
            print(f"Пополнение: {amount_to_add}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for i in range(100):
            amount_to_remove = randint(50, 500)
            print(f'Запрос на {amount_to_remove}.')

            if amount_to_remove <= self.balance:
                with self.lock:
                    if not self.lock.locked():
                        self.lock.acquire()
                    self.balance -= amount_to_remove
                    print(f"Снятие: {amount_to_remove}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                sleep(0.001)



bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f"Итоговый баланс: {bk.balance}")
