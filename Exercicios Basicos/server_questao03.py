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
		n1 = float(recebido.get("n1"))
		n2 = float(recebido.get("n1"))
		n3 = float(recebido.get("n1"))
		
		mediaprevia = (n1+n2)/2
	

		if mediaprevia >= 7.0:
			estado = "Aprovado"
					
		elif (mediaprevia > 3.0 and mediaprevia < 7.0):
			media = (mediaprevia+n3)/2
			if media >= 5.0:
				estado = "Aprovado"
		else:
			estado = "Reprovado"
		break


	retorno = json.dumps({"estado": estado})
					
	conn.sendall(retorno.encode())
