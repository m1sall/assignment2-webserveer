# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serverSocket.bind(("", port))
  #Fill in start
  serverSocket.listen(1)

  #Fill in end

  while True:
    #Establish the connection
    #print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start      #Fill in end
    try:
      try:
        message = connectionSocket.recv(1024)#Fill in start    #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        #Fill in start
        outputdata = f.read      
        #Fill in end
        f.close()
        #Send one HTTP header line into socket.
        #Fill in start
        connectionSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n","UTF-8"))
        connectionSocket.send(bytes("<html><head></head><body><h1>200 OK</h1></body></html>\r\n","UTF-8"))


        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          if len(outputdata) > 0:
            print(output)
          else:
            print("Not Found")
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        # Send response message for file not found (404)
        #Fill in start
        connectionSocket.send(bytes("HTTP/1.1 200 OK\r\n","UTF-8"))
        connectionSocket.send(bytes("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n","UTF-8"))

        #Fill in end
        connectionSocket.close()


        #Close client socket
        #Fill in start

        #Fill in end
        serverSocket.close()

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
