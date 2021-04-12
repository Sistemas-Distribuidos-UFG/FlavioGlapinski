import socket, json

HOST = '192.168.1.200'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind ((HOST, PORT))
s.listen()
while True:
	print('Aguardando Conexão')
	conn, ender = s.accept()
	print("Conectado em", ender)
	while True:
		data = conn.recv(1024)
		if not data:
			print('Fechando a conexão')
			conn.close()
			break
		
		recebido = json.loads(data.decode())
		idade = int(recebido.get("idade"))
		tempo = int(recebido.get("tempo"))


		if idade >= 65 and tempo >= 30 :
			estado = "Liberado para aposentadoria"
		else:
			estado = "Não liberado para aposentadoria"	
		break


	retorno = json.dumps({"estado": estado})
					
	conn.sendall(retorno.encode())
