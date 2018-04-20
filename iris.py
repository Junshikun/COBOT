import abc



class Person(metaclass=abc.ABCMeta):
    def __init__(self,age=1):
        self.age=age
    @abc.abstractmethod
    def drive(self):
        pass
class Adult(Person):
    def __init__(self,age=1):
        if age<18:
            super().__init__(age)
        else:
            raise ValueError
    def drive(self):
        print('ok')

class Car(object):
    def __init__(self,model=None):
        self.model=model
    def ride(self,person):
        person.drive()
class TeslaCar(Car):
    def __init__(self,model='Model S',enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run=enable_auto_run
    @property
    def enable_auto_run(self):
        return self._enable_auto_run
    @enable_auto_run.setter
    def enable_auto_run(self,is_enable):
        self._enable_auto_run=is_enable


Jun=Adult()
Car=TeslaCar()
Car.ride(Jun)