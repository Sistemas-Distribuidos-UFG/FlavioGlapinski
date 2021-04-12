import socket, json

HOST = '192.168.1.200'
PORT = 50000

while True:
	lista = []

	print ("Digite a idade do nadador:")
	idade = input()

	lista = json.dumps({"idade": idade})


	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	s.sendall(lista.encode())

	data = s.recv(1024)
	recebido = json.loads(data.decode())

	classificacao = recebido.get("classificacao")


	print("A classificacao do nadador é:")
	print(classificacao)
	s.close()

