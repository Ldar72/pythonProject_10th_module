from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        self.enemies = 100
        days = 0
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            self.enemies -= self.power
            days += 1
            print(f'{self.name} сражается {days} день(дня)..., осталось {self.enemies} воинов.')
            sleep(1)
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


def main():
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    first_knight.start()
    second_knight.start()
    for knight in (first_knight, second_knight):
        knight.join()
    print('Все битвы закончились!')


if __name__ == '__main__':
    main()