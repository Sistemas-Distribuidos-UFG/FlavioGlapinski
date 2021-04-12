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
		nivel = recebido.get("nivel")
		dependentes = int(recebido.get("dependentes"))
		salario = float(recebido.get("salariobruto"))


		if nivel.upper() == 'A':
			if dependentes == 0:
				salarioLiquido = salario*0.97
			else:
				salarioLiquido = salario*0.92
		elif nivel.upper() == 'B':
			if dependentes == 0:
				salarioLiquido = salario*0.95
			else:
				salarioLiquido = salario*0.90
		elif nivel.upper() == 'C':
			if dependentes == 0:
				salarioLiquido = salario*0.92
			else:
				salarioLiquido = salario*0.85			
		elif nivel.upper() == 'D':
			if dependentes == 0:
				salarioLiquido = salario*0.90
			else:
				salarioLiquido = salario*0.83	
		break


	retorno = json.dumps({"salarioLiquido": salarioLiquido})
					
	conn.sendall(retorno.encode())
