from room import Room
from block import Block
from bonus import Bonus
from trigger import Trigger
import random
from settings import MID_POINT

class RoomGenerator:
    """ Класс создает игровую комнату"""
    def __init__(self, room_size, block_width, block_height, room_x=0, room_y=0):
        self.name = "Generator1"
        self.width = block_width
        self.height = block_height
        self.room_size = room_size
        self.room_x = room_x
        self.room_y = room_y


    def create_room(self, x=1, y=1):

        room = Room(self.room_size)
        for i in range(self.room_size):
            block_width = self.width
            block_height = self.height
            block_x = (x * self.room_size + i) * block_width
            block_y = (y * self.room_size + 0) * block_height

            room.blocks.append(Block(block_x, block_y, block_width, block_height).convert_to_json())

            block_x = (x * self.room_size + i) * block_width
            block_y = (y * self.room_size + self.room_size) * block_height

            room.blocks.append(Block(block_x, block_y, block_width, block_height).convert_to_json())


            block_x = x * (MID_POINT - round(random.gauss(0, 2 * self.room_size)))
            block_y = y * (MID_POINT - round(random.gauss(0, 2 * self.room_size)))

            room.blocks.append(Bonus(block_x, block_y, block_width, block_height).convert_to_json())

            block_x = x * (MID_POINT - round(random.gauss(0, 2 * self.room_size)))
            block_y = y * (MID_POINT - round(random.gauss(0, 2 * self.room_size)))
            teleport = Trigger(block_x, block_y, block_width, block_height, "teleport")


            room.blocks.append(teleport.convert_to_json())

        return {'blocks': room.blocks}




        


