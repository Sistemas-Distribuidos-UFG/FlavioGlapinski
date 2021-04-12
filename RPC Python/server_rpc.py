from xmlrpc.server import SimpleXMLRPCServer

def calculaCredito(saldo):

	saldo = int(saldo)
	if saldo <= 200:
		credito = 0
	elif saldo >= 201 and saldo <=400:
		credito = 0.2
	elif saldo >= 401 and saldo <=600:
		credito = 0.3
	elif saldo >= 601:
		credito = 0.4
	return credito

server = SimpleXMLRPCServer(("localhost",6789))
server.register_function(calculaCredito, "calculaCredito")
server.serve_forever()

