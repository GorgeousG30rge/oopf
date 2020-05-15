from roomgenerator import RoomGenerator
from roomgenerator2 import RoomGenerator2

class RoomFactory:
    """ Класс хранит созданные комнаты
    """
    def __init__(self):

        self._generators = [RoomGenerator(16,32,32), RoomGenerator2(16,32,32)]
        self._rooms = []
    
    def add_generator(self, generator):
        return self._generators.append(generator)


    def transfer_room(self):
        if self.counter() % 2 == 0:
            self._rooms.append(self._generators[0].create_room())
            return self._generators[0].create_room()
        else:
            self._rooms.append(self._generators[0].create_room())
            return self._generators[1].create_room()
    
    
    def counter(self):
        return len(self._rooms)
        




        

