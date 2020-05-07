import random
from baseblock import BaseBlock
from room import Room

class Trigger(BaseBlock):
    def __init__(self, x, y, width, height, type_, x_random = random.randint(0,512), y_random = random.randint(0, 512)):
        BaseBlock.__init__(self, x, y, width, height)
        self.type = type_
        self.coords = {"x": x_random,
                       "y": y_random
                       }

    def convert_to_json(self):
        return {
                "x": self.x,
                "y": self.y,
                "width": self.width,
                "height": self.height,
                "type" : self.type,
                "coords": self.coords
                }


    