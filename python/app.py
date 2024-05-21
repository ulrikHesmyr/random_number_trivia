from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

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
    # Broadcast the message to all connected clients
    emit('display', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
