from flask import Flask
from roomfactory import RoomFactory
from roomgenerator import RoomGenerator


factory = RoomFactory(RoomGenerator(32,32,32))



app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return factory.transfer_room()

   
