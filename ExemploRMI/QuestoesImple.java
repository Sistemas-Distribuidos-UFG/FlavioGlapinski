/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author sye
 */
import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;

public class QuestoesImple extends UnicastRemoteObject implements Questoes {
        protected QuestoesImple() throws RemoteException{
        super();
    }


        
 public double Credito(double saldoMedio) throws RemoteException {
                double credito = 0;
               if (saldoMedio<=200){
                credito=0;
                System.out.println("Valor menor que 200");                
            }else if (saldoMedio>201 && saldoMedio<=400){
                credito=(float) 0.2;
                System.out.println("Valor maior igual que 201 e menor que 400");                
            }else if (saldoMedio>401 && saldoMedio<=600){
                credito=(float) 0.3;
                System.out.println("Valor maior igual que 401 e menor que 600");                
            }else if (saldoMedio>601){
                credito=(float) 0.4;
                System.out.println("Valor maior que 600");                
            }
        return  credito;

    }
   


}
