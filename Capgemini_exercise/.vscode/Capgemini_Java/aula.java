class Scratch {
    public static void main(String[] args) {

        int nota = 100;
        String graduacao;
        // A 80  B 70  C60  D0

        if (nota >= 80){
            System.out.println("Nota A");
            graduacao = "A";

        }else if (nota < 80 && nota >= 70){
            System.out.println("Nota B");
            graduacao = "B";

        }else if (nota < 70 && nota >= 60){
            System.out.println("Nota C");
            graduacao = "C";

        }else if (nota < 60 && nota >= 0){
            System.out.println("Nota D");
            graduacao = "D";

        }else {
            System.out.println("Nota Invalida");
            graduacao = "";
        }

        switch (graduacao){
            case "A":
            case "B":
                System.out.println("Aluno aprovado");
                break;
            case"C":
            case"D":
                System.out.println("Aluno não aprovado");
                break;
            default:
                System.out.println("Nota Invalida");
        }
    }
}
