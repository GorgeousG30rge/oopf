from roomgenerator import RoomGenerator

class RoomFactory:
    """ Класс хранит созданные комнаты
    """
    def __init__(self, room_generator):

        self._generators = []
        self.room_generator = room_generator

    def transfer_room(self):
                room_generator = RoomGenerator(16,32,32)
                self._generators.append(room_generator)
                return room_generator.create_room()
        




        

