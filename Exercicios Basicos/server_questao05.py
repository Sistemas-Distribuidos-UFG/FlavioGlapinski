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

	

		if idade >= 5 and idade <= 7:
			classificacao = "infantil A"
					
		elif idade >= 8 and idade <= 10:
			classificacao = "infantil B"
		elif idade >= 11 and idade <= 13:
			classificacao = "juvenil A"
		elif idade >= 14 and idade <= 17:
			classificacao = "juvenil B"
		elif idade >= 18:
			classificacao = "adulto"
		else:
			classificacao = "Sem Classificação"

		break


	retorno = json.dumps({"classificacao": classificacao})
					
	conn.sendall(retorno.encode())
