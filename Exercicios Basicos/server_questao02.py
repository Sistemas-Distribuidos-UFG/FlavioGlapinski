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
		nome = recebido.get("nome")
		sexo = recebido.get("sexo")
		idade = recebido.get("idade")

		if sexo.upper() == 'MASCULINO':
			if int(idade) < 18:
				maioridade = "Não atingiu maioridade legal"
			elif int(idade) >= 18:
				maioridade = "Atingiu maioridade legal"		
		if sexo.upper() == 'FEMININO':
			if int(idade) < 21:
				maioridade = "Não atingiu maioridade legal"
			if int(idade) >= 21:
				maioridade = "Atingiu maioridade legal"
		break


	retorno = json.dumps({"nome": nome, "maioridade": maioridade})
					
	conn.sendall(retorno.encode())
