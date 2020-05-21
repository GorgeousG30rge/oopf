from room import Room
from block import Block
from bonus import Bonus
from trigger import Trigger
import random
import math
from settings import MID_POINT

class RoomGenerator:
    """ Класс создает игровую комнату"""
    def __init__(self, room_size, block_width, block_height, room_x=1, room_y=1):
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


            block_x = (x * self.room_size + i * i) * block_width
            block_y = round((i * math.sin(y * self.room_size + i) * block_width) + (y * self.room_size + 0) * block_height)

            room.blocks.append(Block(block_x, block_y, block_width, block_height, '/images/ground.png').convert_to_json())

            block_x = (x * self.room_size + i) * block_width
            block_y = round((random.randint(0, self.room_size) * math.sin(y * self.room_size + i) * block_width) + (y * self.room_size + 0) * block_height)

            room.blocks.append(Block(block_x, block_y, block_width, block_height, '/images/ground.png').convert_to_json())


        block_x = random.randint(x * block_width, x * self.room_size  * block_width)
        block_y = random.randint(y * block_width, y * self.room_size  * block_width)

        room.blocks.append(Bonus(block_x, block_y, block_width, block_height).convert_to_json())

        block_x = random.randint(x * block_width, x * self.room_size  * block_width)
        block_y = random.randint(y * block_width, y * self.room_size  * block_width)

        teleport = Trigger(block_x, block_y, block_width, block_height, "teleport")
        room.blocks.append(teleport.convert_to_json())

        return {'blocks': room.blocks}



        


