
import java.io.BufferedInputStream;
import java.io.OutputStreamWriter;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;
import org.apache.commons.io.IOUtils;
import org.json.JSONObject;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author sye
 */
public class ChatServer extends Thread{
    //Declarando porta do Socket
    public static final int PORT = 50000;
    public double credito = -1;
    public int saldoMedio = -1;
    //
    private ServerSocket serverSocket;
    
    public void start(){
        try {
                    serverSocket = new ServerSocket(PORT);
        System.out.println("Servidor iniciado na porta " + PORT);
        clientConnectionLoop();
            
        } catch (Exception e) {
        }
        

        
                
    }
    
    private void clientConnectionLoop() throws IOException{

            

        while(true){
            //recebe conexão
            System.out.println("Aguardando conexão...");
            Socket clientSocket = serverSocket.accept();
            
            //adicionar a thread
            System.out.println("Cliente " + clientSocket.getRemoteSocketAddress() + " está conectado.");

            //lê entrada de dados
            OutputStreamWriter writer = new OutputStreamWriter(clientSocket.getOutputStream(), "UTF-8");
            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            String msg = in.readLine();
            //InputStream in = new BufferedInputStream(clientSocket.getInputStream());
            //String msg = IOUtils.toString(in, "UTF-8");
            System.out.println("Mensagem recebida do cliente " + clientSocket.getRemoteSocketAddress() + ": " + msg);
            
            //recebe entrada e converte para json
            JSONObject myResponse = new JSONObject(msg);
            System.out.println("Saldo médio - " + myResponse.getString("saldo"));
            saldoMedio = Integer.parseInt(myResponse.getString("saldo"));
            
            if (saldoMedio<=200){
                credito=0;
                System.out.println("Valor menor que 200");                
            }else if (saldoMedio>201 && saldoMedio<=400){
                credito=0.2;
                System.out.println("Valor maior igual que 201 e menor que 400");                
            }else if (saldoMedio>401 && saldoMedio<=600){
                credito=0.3;
                System.out.println("Valor maior igual que 401 e menor que 600");                
            }else if (saldoMedio>601){
                credito=0.4;
                System.out.println("Valor maior que 600");                
            }
            
            //criando json de resposta
            JSONObject resposta = new JSONObject();
            resposta.put("credito", credito);
            
            //enviando o json como resposta para o client
            writer.write(resposta.toString() + "\n");
            writer.flush();
            
            clientSocket.close();
            
            
        }
    }
    
    public void chamathread(){
        ChatServer serv = new ChatServer();
        Thread ts = new Thread(serv);
        
    }
    
    public static void main(String[] args) {
        
        try {
            ChatServer server = new ChatServer();
            server.start();
        } catch (Exception e) {
            //Atalho "sout" ctl + espaço
            System.out.println("Erro ao inicializar servidor" + e.getMessage());
                    
        }
        
        System.out.println("Servidor finalizado!");
        
    }
    
}
