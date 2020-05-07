from block import Block


class Room:
    """Класс хранит информацию о комнате"""
    def __init__(self, size):
        self.size = size
        self.blocks = []
        self.bonuses = []
        self.triggers = []

    def convert_blocks_to_json(self):
        for block in self.blocks:
            block.convert_to_json()




    
    


    