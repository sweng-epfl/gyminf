class PeopleCounter:

    def __init__(self, maximum=10):
        self.count = 0
        self.maximum = maximum

    def increment(self):
        if self.count < self.maximum:
            self.count += 1

    def reset(self):
        self.count = 0
