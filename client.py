import socket               # Import socket module
import threading
import Queue
import application

def recieve_messages(sock, root):
  print 'Recieving messages.'
  global app
  while True:
    try:
      message = sock.recv(1024)
      app.get_text(message)
    except:
      print 'Server disconnected.'
      break

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))
root, app = application.create_app(s)

reciever = threading.Thread(target=recieve_messages, args=(s, root))
reciever.daemon = True
reciever.start()
application.start_app(root, app)