import socket, json

HOST = '192.168.1.200'
PORT = 50000

while True:
	lista = []

	print ("Digite o nome do funcionário:")
	nome = input()
	print ("Digite o nível do funcionário:")
	nivel = input()
	print ("Digite o salario bruto do funcionário:")
	salariobruto = input()
	print ("Digite o número de dependentes do funcionário:")
	dependentes = input()

	lista = json.dumps({"nome": nome, "nivel": nivel,"salariobruto": salariobruto, "dependentes": dependentes})


	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	s.sendall(lista.encode())

	data = s.recv(1024)
	recebido = json.loads(data.decode())

	salarioLiquido = recebido.get("salarioLiquido")


	print("O nome do funcionário, nível e salário liquido é:")
	print(nome)
	print(nivel)
	print(salarioLiquido)
	s.close()

