import socket, json

HOST = '192.168.1.200'
PORT = 50000

while True:
	lista = []

	print ("Digite o nome do funcionário:")
	n1 = input()
	print ("Digite o sexo do funcionário:")
	n2 = input()
	print ("Digite o idade do funcionário:")
	n3 = input()

	lista = json.dumps({"n1": n1, "n2": n2,"n3": n3})


	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	s.sendall(lista.encode())

	data = s.recv(1024)
	recebido = json.loads(data.decode())

	estado = recebido.get("estado")


	print("A situação do aluno é:")
	print(estado)
	s.close()

