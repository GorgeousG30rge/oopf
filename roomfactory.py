

class RoomFactory:
    """ Класс хранит созданные комнаты """
    def __init__(self):

        self._generators = []
        self._rooms = []
    
    def add_generator(self, generator):
        return self._generators.append(generator)

    def get_generator_name(self):
        return self._generators


    def transfer_room(self):
        if len(self._rooms) == 0:
            self._rooms.append(self._generators[0].create_room())
            return self._generators[0].create_room()
        elif len(self._rooms) % 2 != 0:
            self._rooms.append(self._generators[1].create_room())
            return self._generators[1].create_room()
        else:
            self._rooms.append(self._generators[2].create_room())
            return self._generators[2].create_room()
        




        

