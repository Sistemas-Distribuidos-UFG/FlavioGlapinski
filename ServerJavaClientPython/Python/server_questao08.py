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
		saldo = int(recebido.get("saldo"))
		
		if saldo <= 200:
			credito = 0
		elif saldo >= 201 and saldo <=400:
			credito = 0.2
		elif saldo >= 401 and saldo <=600:
			credito = 0.3
		elif saldo >= 601:
			credito = 0.4
		break


	retorno = json.dumps({"credito": credito})
					
	conn.sendall(retorno.encode())
