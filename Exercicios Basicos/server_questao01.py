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
		
		data = json.loads(data.decode())
		nome = data.get("nome")
		cargo = data.get("cargo")
		salario = data.get("salario")
		print("Antes if cargo: ", cargo)
		print("Antes if salario: ", salario)
		
		if cargo == 'operador':
			salario = float(salario)*1.2
			print ("operador s:", salario)
			break
		if cargo.upper() == 'PROGRAMADOR':
			salario = float(salario)*1.18
			print ("programador s:", salario)
			break	

	retorno = json.dumps({"nome": nome, "cargo": cargo,"salario": salario})
					
	conn.sendall(retorno.encode())
