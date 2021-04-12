import socket, json

HOST = '192.168.1.200'
PORT = 50000

while True:
	lista = []

	print ("Digite a idade do funcionário:")
	idade = input()
	print ("Digite o tempo de contribuição do funcionário:")
	tempo = input()

	lista = json.dumps({"idade": idade, "tempo": tempo})


	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	s.sendall(lista.encode())

	data = s.recv(1024)
	recebido = json.loads(data.decode())

	estado = recebido.get("estado")


	print("O estado de liberação de aposentadoria é:")
	print(estado)
	s.close()

