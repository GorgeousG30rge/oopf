from flask import Flask
from roomfactory import RoomFactory
from roomgenerator import RoomGenerator
from roomgenerator2 import RoomGenerator2
from emptyroomgenerator import EmptyRoomGenerator
from settings import ROOM_SIZE, BLOCK_WIDTH, BLOCK_HEIGHT



factory = RoomFactory()
emptyroom = EmptyRoomGenerator(ROOM_SIZE, BLOCK_WIDTH, BLOCK_HEIGHT)
generator1 = RoomGenerator(ROOM_SIZE, BLOCK_WIDTH, BLOCK_HEIGHT)
generator2 = RoomGenerator2(ROOM_SIZE, BLOCK_WIDTH, BLOCK_HEIGHT)

factory.add_generator(emptyroom)
factory.add_generator(generator1)
factory.add_generator(generator2)

app = Flask(__name__)


@app.route('/index', methods = ['GET'])
@app.route('/', methods = ['GET'])
def index():
    room = factory.transfer_room()
    response = app.make_response(room) 
    response.headers["Room status"] = "Room created"
    response.headers["Room counter"] = len(factory._rooms)
    return response
  
