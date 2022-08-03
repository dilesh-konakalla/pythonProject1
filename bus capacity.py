class vehicle(object):
    def __init__(self, capacity):
        self.capacity = capacity

    def getcapacity(self):
        return self.capacity
class bus(vehicle):
    pass
emp = vehicle(50)
print(emp.getcapacity())

