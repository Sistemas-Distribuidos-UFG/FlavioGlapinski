import socket, json

HOST = '192.168.1.200'
PORT = 50000

while True:
	lista = []

	print ("Digite o nome do funcionário:")
	nome = input()
	print ("Digite o Cargo do funcionário:")
	cargo = input()
	print ("Digite o Salario do funcionário:")
	salario = input()

	lista = json.dumps({"nome": nome, "cargo": cargo,"salario": salario})


	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	s.sendall(lista.encode())

	data = s.recv(1024)
	recebido = json.loads(data.decode())

	nomer = recebido.get("nome")
	cargor = recebido.get("cargo")
	salarior = recebido.get("salario")

	print("O nome do funcionário, cargo e salário reajustado:")
	print(nomer)
	print(cargor)
	print(salarior)
	s.close()

