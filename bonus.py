from baseblock import BaseBlock


class Bonus(BaseBlock):
    def __init__(self, x, y, width, height):
        BaseBlock.__init__(self, x, y, width, height)
        self.type = 'score bonus'
        self.image = 'images/block.png'  
        self.effect = 500

    def convert_to_json(self):
        return  {"x": self.x,
                 "y": self.y,
                 "width": self.width,
                 "height": self.height,
                 "type": self.type,
                 "effect": self.effect,
                 "image": self.image
                 } 
                

        

