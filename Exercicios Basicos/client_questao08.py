import socket, json

HOST = '192.168.1.200'
PORT = 50000

while True:
	lista = []

	print ("Digite a saldo médio:")
	saldo = input()


	lista = json.dumps({"saldo": saldo})
	lista = lista + '\n'



	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	s.sendall(lista.encode('utf-8'))





	data = s.recv(1024)
	recebido = json.loads(data.decode())

	credito = float(recebido.get("credito"))
	credito = credito*float(saldo)

	print("o valor do saldo médio é:")
	print(saldo)
	print("o valor do crédito disponível é:")
	print(credito)	
	s.close()

