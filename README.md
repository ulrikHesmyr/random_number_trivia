# Random number trivia

## Description
This web application is for people to input a number on their phone/PC and then there will 
be a random trivia related to this number, displayed on a monitor connected to a Raspberry 
Pi which will be located in the future be located in my collective university housing.

I will use the [Numbers API](http://numbersapi.com/#random/trivia) to retrieve the random 
trivia. 

To do this we will create an HTTP server

That will use `SocketIO` to enable real-time bi-directional communication between the server 
and clients. In other words, allow the client on the monitor to display the trivia after the 
input from another client is sent to the server with an HTTP request.

## Setup
### Installation
### Usage
