import pygame
import math
import random
from roomfactory import RoomFactory
from roomgenerator import RoomGenerator
from roomgenerator2 import RoomGenerator2
from emptyroomgenerator import EmptyRoomGenerator



class ExampleRoomFactory:
    def __init__(self, room_size, block_width, block_height):
        self.width = block_width
        self.height = block_height
        self.room_size = room_size

    def create_room(self, x, y):
        block_width = self.width
        block_height = self.height

        blocks = []


        for i in range(self.room_size):
            blocks.append({
                'x': (x * self.room_size + i) * block_width,
                'y': (y * self.room_size + 0) * block_height,
                'width': block_width,
                'height': block_height
            })
            blocks.append({
                'x': (x * self.room_size + i) * block_width,
                'y': (y * self.room_size + self.room_size) * block_height,
                'width': block_width,
                'height': block_height
            })
            blocks.append({
                'x': (768 - round(random.gauss(0, 5))),
                'y': (768 - round(random.gauss(0, 5))),
                'width': self.width,
                'height': self.height
            })

        return {
            'blocks': blocks
        }





class BlocksView:
    def __init__(self, room_factory):
        self.screen = None
        self.offset_x = 0
        self.offset_y = 0
        self.dx = 0
        self.dy = 0
        self.rooms = []
        self.rooms_pos = []
        self.room_factory = room_factory
        self.width = 800
        self.height = 600


    def load_room(self, room_x, room_y):
        if (room_x, room_y) not in self.rooms_pos :
            r = self.room_factory.create_room(room_x, room_y)
            self.rooms.append(r)
            self.rooms_pos.append((room_x, room_y))


    def draw(self):
        self.offset_x += self.dx
        self.offset_y += self.dy

        room_x = (self.offset_x + self.width // 2) // self.room_factory.width // self.room_factory.room_size
        room_y = (self.offset_y + self.height // 2) // self.room_factory.height // self.room_factory.room_size
        self.load_room(room_x, room_y)
        #self.load_room(room_x - 1, room_y)
        #self.load_room(room_x + 1, room_y)
        #self.load_room(room_x, room_y - 1)
        #self.load_room(room_x, room_y + 1)



        for room in self.rooms:
            for block in room["blocks"]:
                x = block["x"] - self.offset_x
                y = block["y"] - self.offset_y
                rct = self.screen.blit(pygame.image.load(block["image"]), (x,y))
                pygame.draw.rect(self.screen, (255, 255, 255), rct, 1)



        pos = (self.width // 2, self.height // 2)
        pygame.draw.circle(self.screen, (255, 255, 255), pos, 15)
 
    def keydown(self, key):
        if key == pygame.K_DOWN:
            self.dy = 5
        if key == pygame.K_UP:
            self.dy = -5
        if key == pygame.K_LEFT:
            self.dx = -5
        if key == pygame.K_RIGHT:
            self.dx = 5
    
    def keyup(self, key):
        if key == pygame.K_DOWN:
            self.dy = 0
        if key == pygame.K_UP:
            self.dy = 0
        if key == pygame.K_LEFT:
            self.dx = 0
        if key == pygame.K_RIGHT:
            self.dx = 0

    def run(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
                if event.type == pygame.KEYDOWN:
                    self.keydown(event.key)
                if event.type == pygame.KEYUP:
                    self.keyup(event.key)
        
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()


factory = RoomFactory()
generator1 = RoomGenerator(8, 32, 32)
generator2 = RoomGenerator2(16, 32, 32)
empty = EmptyRoomGenerator(16, 32, 32)

if __name__ == "__main__":
   BlocksView(empty).run()

