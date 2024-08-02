from abc import ABC, abstractmethod


class Worker(ABC):
    @abstractmethod
    def work(self):
        pass


class EatableWorker(ABC):
    @abstractmethod
    def eat(self):
        pass


class Human(Worker, EatableWorker):
    def eat(self):
        print('Eating')

    def work(self):
        print('Working')


class Robot(Worker):  # Robot didn't eat

    def work(self):
        print('Working')
