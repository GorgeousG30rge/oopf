import random
from baseblock import BaseBlock
from room import Room

class Trigger(BaseBlock):
    def __init__(self, x, y, width, height):
        BaseBlock.__init__(self, x, y, width, height)
        self.type = "Teleport"
        self.coords = {}

    def create_teleport(self):
        teleport_x = random.randint(0, 512)
        teleport_y = random.randint(0, 512)
        self.coords = {'x': teleport_x,
                       'y': teleport_y
                       }

    def convert_to_json(self):
        return {"x": self.x,
                "y": self.y,
                "width": self.width,
                "height": self.height,
                "type" : self.type,
                "coords": self.coords}





    