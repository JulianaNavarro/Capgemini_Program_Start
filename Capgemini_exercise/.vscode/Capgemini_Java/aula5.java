/*  tipos primitivos

public class Main {
    
    public static void main(String[] args) {
       int idade = 10;
       float cotacaoDolar = 5.0f;
       double cotacaoEuro = 6.0d;
       char genero = 'M';
       byte pontos = 0;
       boolean palmeirasTemMundial = false;
       
       String nome = "Esse é uma texto da variável String";
    }
}*/

// COMO LER DADOS:

import java.util.Scanner;
public class Main {

    public static void main (String[]args){
        
       Scanner leitor = new Scanner(System.in);
       
       int idade = leitor.nextInt();
       float cotacaoDolar = leitor.nextFloat();
       double cotacaoEuro = leitor.nextDouble();
       String nome = leitor.nextLine();
       String codigoRua = leitor.next ();
       
       
       System.out.println("Texto que será exibido o console");
       System.out.print("Texto que será exibido o console 2");
       
    }

}
