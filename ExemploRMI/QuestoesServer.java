/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author sye
 */
import java.rmi.registry.LocateRegistry;
import java.rmi.Naming;
import java.rmi.Remote;

public class QuestoesServer {
    QuestoesServer(){
        try{
            System.setProperty("java.rmi.server.hostname", "192.168.1.200");
            LocateRegistry.createRegistry(1099);
            Questoes c = new QuestoesImple();
            Naming.bind("QuestoesService", (Remote) c);
        } catch (Exception e){
            e.printStackTrace();
        }               
    }
    
    public static void main(String[] args){
        new QuestoesServer();
    }
    
    
}
