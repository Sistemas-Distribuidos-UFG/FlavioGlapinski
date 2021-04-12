import socket, json

HOST = '192.168.1.200'
PORT = 50000

while True:
	lista = []

	print ("Digite o sexo:")
	sexo = input()
	print ("Digite a altura:")
	altura = input()


	lista = json.dumps({"sexo": sexo, "altura": altura})


	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	s.sendall(lista.encode())

	data = s.recv(1024)
	recebido = json.loads(data.decode())

	pesoIdeal = recebido.get("pesoIdeal")


	print("O peso ideal do(a) ", sexo,"é:")
	print(round(pesoIdeal,1))
	s.close()

