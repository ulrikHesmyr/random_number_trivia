# Random number trivia

## Description
This web application is for people to input a number on their phone/PC and then there will 
be a random trivia related to this number, displayed on a monitor connected to a Raspberry 
Pi which will be located in the future be located in my collective university housing.

## Approach
To do this we will create an HTTP server

That will use `SocketIO` to enable real-time bi-directional communication between the server 
and clients. In other words, allow the client on the monitor to display the trivia after the 
input from another client is sent to the server with an HTTP request.

## History
First I used the [Numbers API](http://numbersapi.com/#random/trivia) to retrieve the random 
trivia. Then I thought it would be better to not create alot of traffic to this API by prociding the data myself, and so I went to ChatGPT to generate trivia data for the numbers from 1-80. 

## Roadmap
I have realized that it is not so efficient to manually ask ChatGPT for data, and then capture the request which are sent to the ChatGPT server (I will use an interceptor for this), and my plan is to automate the requests by creating a dockerized microservice (using either `rust` or `go`) which does the following:

1. Send request to ChatGPT server (probably use ChatGPT API if it exists). 
2. Retrieve the JSON data and concatinate it to the current data and write it to a file.
3. The data will be returned on all requests to the microservice. The `.json` file will be used as persistent storage. I could also used a document-based NoSQL database, but I find more efficient by creating a custom made DBMS as part of this microservice.

The microservice will make requests to ChatGPT for a variable time interval. I.e every minute.




## Setup
### Installation
### Usage
