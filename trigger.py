import random
from baseblock import BaseBlock
from room import Room
from settings import *

class Trigger(BaseBlock):
    def __init__(self, x, y, width, height, type_, x_random = TELEPORT_X, y_random = TELEPORT_Y):
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


    