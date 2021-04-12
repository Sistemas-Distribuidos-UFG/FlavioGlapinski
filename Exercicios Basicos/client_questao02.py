import socket, json

HOST = '192.168.1.200'
PORT = 50000

while True:
	lista = []

	print ("Digite o nome do funcionário:")
	nome = input()
	print ("Digite o sexo do funcionário:")
	sexo = input()
	print ("Digite o idade do funcionário:")
	idade = input()

	lista = json.dumps({"nome": nome, "sexo": sexo,"idade": idade})


	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	s.sendall(lista.encode())

	data = s.recv(1024)
	recebido = json.loads(data.decode())

	nomer = recebido.get("nome")
	maioridade = recebido.get("maioridade")

	print("Nome da pessoa e estado de maioridade legal:")
	print(nomer)
	print(maioridade)
	s.close()

