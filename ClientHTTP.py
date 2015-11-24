# Python HTTP Client by Federico De Faveri

import http.client

print("--Fede's simple HTTP client-- \n-Will Send a GET request and output the response-\n\n")

host = input("please input host: ")
port = input("\nplease input port number: ")
pagerequested = input("\nplease input the page that you want to retrieve (ex. /index.php): ");

print("\n\nconnecting to " + host + " at port " + port)


def connection(host, port):

    print("\nready to connect")
    
    instance = http.client.HTTPConnection(host, port)
    
    print("\nconnected to " + host)

    instance.request('GET', pagerequested)
    
    print("\n\nGET request sent");    

    risp = instance.getresponse()

    print("Server Answer: ")
    print(risp.read())

    print("bye bye")
    instance.close()

    
    
connection(host, port)
    
    
