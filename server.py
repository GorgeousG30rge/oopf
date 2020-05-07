from flask import Flask
from roomfactory import RoomFactory
from roomgenerator import RoomGenerator


factory = RoomFactory(RoomGenerator(32,32,32))



app = Flask(__name__)


@app.route('/index', methods = ['GET'])
@app.route('/', methods = ['GET'])
def index():
    room = factory.transfer_room()
    response = app.make_response(room) 
    response.headers["Room status"] = "Room created"
    response.headers["Room counter"] = factory.counter()
    return response
  
