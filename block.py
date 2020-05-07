from baseblock import BaseBlock

class Block(BaseBlock):
    def __init__(self, x, y, width, height):
        BaseBlock.__init__(self, x, y, width, height)
        self.image = '/images/block.png'


    def convert_to_json(self):
        return {"x": self.x,
                "y": self.y,
                "image": self.image,
                "width": self.width,
                "height": self.height}





        