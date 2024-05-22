from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit
import requests
from utils.data import random_number_trivias
import random

app = Flask(__name__)
socketio = SocketIO(app)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the input page
@app.route('/input')
def input_page():
    return render_template('input.html')

# WebSocket event for receiving messages
@socketio.on('message')
def handle_message(data):

    #Validating if we have data for this number
    number = int(data)
    if number > len(random_number_trivias) and number > 0:
        emit('display', 'Number out of range', broadcast=True)
        return
    
    # Get the random number trivia based on the input, accessing a dictionary, not a list
    number_data = random_number_trivias[number]
    number_trivia = number_data[random.randint(0, len(number_data)-1)]

    # Broadcast the message to all connected clients
    emit('display', number_trivia, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
