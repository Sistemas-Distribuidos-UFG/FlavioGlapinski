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
		sexo = recebido.get("sexo")
		altura = float(recebido.get("altura"))


		if sexo.upper() == 'MASCULINO':
			pesoIdeal = (72.7*altura)-58
					
		elif sexo.upper() == 'FEMININO':
			pesoIdeal = (62.1*altura)-44.7
	
		break


	retorno = json.dumps({"pesoIdeal": pesoIdeal})
					
	conn.sendall(retorno.encode())
