class Scratch {
    public static void main(String[] args) {

        // 1 2 3 4 5 6 7 8 9 10, saida um abaixo do outro.

        for (int i = 1; i <= 10; i++) {
            System.out.println(i);
        }

        // para ir de dois em dois,  i+=2     ex:
//        for (int i = 1; i <= 10; i+=2) {
//            System.out.println(i);
       //}

        // para tabuada, (laços for, aninhados, um dentro do outro) ex:
        for (int i = 1; i <= 10; i++) {
            for (int j =  1; j <= 10; j++){
                System.out.println(j + "x" + i + " = " + j * i);
                //ex: 1x1 = 1
                //1x2 = 2
            }
        }

    }
}
