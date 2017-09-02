import socket               # Import socket module
import Queue
import threading

clients = []
messages = Queue.Queue()

def recieve_messages(client, queue):
  print 'Server recieving messages'
  global clients
  name = 'default-user'
  try:
      message = client.recv(1024)
      name = message
  except:
    print 'Lost connection with', client
    clients.remove(client)
    return
  while True:
    try:
      message = client.recv(1024)
      queue.put(name + ": " + message)
    except:
      print 'Lost connection with', client
      clients.remove(client)
      break

def send_messages(queue):
  print 'Server sending messages'
  global clients
  while True:
    message = queue.get()
    for client in clients:
      client.send(message)

sender = threading.Thread(target=send_messages, args=(messages,))
sender.daemon = True
sender.start()

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
try:
  s.bind((host, port))        # Bind to the port
except:
  print 'Another server is already active on this port.'
  exit()

s.listen(5)  
              # Now wait for client connection.

while True:
   c, addr = s.accept()     # Establish connection with client.
   clients.append(c)
   print 'Got connection from', addr
   client = threading.Thread(target=recieve_messages, args=(c, messages))
   client.daemon = True
   client.start()