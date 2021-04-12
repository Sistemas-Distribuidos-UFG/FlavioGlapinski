import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")

while True:
	print ("Digite a saldo médio:")
	saldo = int(input())
	
	credito = float(proxy.calculaCredito(saldo))
	credito = credito*saldo

	print("o valor do saldo médio é:")
	print(saldo)
	print("o valor do crédito disponível é:")
	print(credito)	





