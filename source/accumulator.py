class Accumulator:

    def __init__(self, count=0):
        self.__count = count

    def add_accumulators(self, amount=1):
        self.__count += amount

    @property
    def count(self):
        return self.__count
