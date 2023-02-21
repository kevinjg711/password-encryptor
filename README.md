# password-encryptor

This microservice python file will enable user to send a password as data to this program to hash and salt the password before sending it back to the user

This microservice would constantly be requesting data once it has been run. Instead of using break which would terminate the program after sending the data back to the user once, I used continue so that it would continue to return values back to the user once up and running.

To request data from user's side of program, here is the code they could include in their program.

import socket

HOST = "127.0.0.1"
PORT = 65432


def password_encrypt(password):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect((HOST, PORT))
      password_byte = password.encode("utf-8")
      s.sendall(password_byte)
      data = s.recv(1024)
      data_dc = data.decode("utf-8")
  print(data_dc)
  
password_encrypt(string)

Once microservice is up and running, they can continously request data by calling the password_encrypt function with the original password as the parameter.

The print statement of data_dc is there to make it clear that they are receiving the data, but they can choose to do anything they need to (upload to the database) with the data_dc variable.
