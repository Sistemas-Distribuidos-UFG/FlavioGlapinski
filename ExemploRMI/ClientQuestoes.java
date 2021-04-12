import java.rmi.*;
import java.text.DecimalFormat;
import java.util.Scanner;


public class ClientQuestoes {
    public static void main(String [] args){
        try{
            while(true){
            Scanner scanner = new Scanner(System.in);
            double creditoFinal;
            Questoes c = (Questoes) Naming.lookup("rmi://192.168.1.200:1099/QuestoesService");
            
            double salarioMedio;
            DecimalFormat df = new DecimalFormat("#.##");            
            System.out.println("Digite o salário Médio:");
            salarioMedio = scanner.nextDouble();
            System.out.println("Salario médio digitado é :" + df.format(salarioMedio));
            creditoFinal = salarioMedio*c.Credito(salarioMedio);
            
            System.out.println("O crédito disponível é : "+ df.format(creditoFinal) );           
            System.out.println();
            }

           

            
        }catch (Exception e){
            e.printStackTrace();
        }
    }
    
}