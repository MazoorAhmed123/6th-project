import socket

s = socket.socket()
print("Socket created")
s.bind(('localhost', 9999))
s.listen(3)
print('Waiting for connections')

while True:
    c, addr = s.accept()
    print("Connected with", addr)

    # Sending a welcome message (encoded as bytes)
    welcome_message = 'Welcome to MUET'.encode('utf-8')
    c.send(welcome_message)

    # Close the connection
    c.close()
