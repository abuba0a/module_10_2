# -*- coding: utf8 -*-
from threading import Thread
from time import sleep


class Knight(Thread):
    enemy = 100
    days = 0

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, íà íàñ íàïàëè!')
        while self.enemy > 0:
            self.enemy -= self.power
            self.days += 1
            sleep(1.0)
            print(f'{self.name} ñðàæàåòñÿ {self.days} äíåé(äíÿ), îñòàëîñü {self.enemy} âîèíîâ. \n')
        print(f'{self.name} îäåðæàë ïîáåäó ñïóñòÿ {self.days} äíåé(äíÿ)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
