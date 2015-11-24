# Python HTTP Clients by Federico De Faveri

These are very simple Python clients that send an HTTP GET request and print the server's response.

## USAGE:

###  ClientHTTP.py

To run execute in your terminal window `python3 ClientHTTP.py`

This program will ask the user for three inputs:

1. The host we want to connect to (for example localhost)

2. The port we wanto to connect to (for example 80)

3. The page we want to retrieve (for example /index.php)


After these three inputs from the user, the program will send the GET request and then print out the response from the webserver.

### socketclient.py

To run execute in your terminal window `python3 socketclient.py`

This program will simply send and HTTP GET request for the index page. The difference between this program and the previous one is that this one uses a socket library, not an HTTP library.

----

Nothing too fancy at all but a great learning experience on how the web works!

Thank you!
