import java.util.Arrays;

class Scratch {
    public static void main(String[] args) {

//        //arrays
//        int [] numeros = new int [5];
//        //[0] [1] [2] [3] [4]
//        numeros [0] = 1;
//        numeros [1] = 2;
//        numeros [2] = 3;
//        numeros [3] = 4;
//        numeros [4] = 5;
//
//        for (int i=0; i < numeros.length; i++){
//            System.out.println(numeros[i]);
//        }
//
//        String [] letras = new String[5];
//        letras[0] = "A";
//        letras[1] = "B";
//        letras[2] = "C";
//        letras[3] = "D";
//        letras[4] = "J";
//
//        for (int i=0; i < letras.length; i++){
//            System.out.println(letras[i]);
//
//        }

        String [] letras = {"A", "B", "C", "D", "J"};
        for (int i=0; i < letras.length; i++){
           System.out.println(letras[i]);
        }

        // outro exemplo:
        System.out.println(Arrays.toString(letras));

//--------------------------------------------------------------------------------
        int[] numeros = { 9, 10, 12, 25, 2};
        int maior = numeros [0];
        int menor = numeros [0];
        int media = 0;

        for (int i=0; i< numeros.length; i++){
            if (numeros [i] > maior){
                maior = numeros[i];
            }if (numeros[i] < menor){
                menor = numeros[i];
            } media += numeros[i];
        }
        System.out.println("Maior " + maior);
        System.out.println("Menor " + menor);
        System.out.println("Média " + media/numeros.length);
    }
}
