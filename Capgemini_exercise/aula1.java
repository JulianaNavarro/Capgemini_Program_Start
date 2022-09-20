
import java.time.LocalDate;
import java.time.format.TextStyle;
import java.util.Locale;
import java.time.LocalDateTime;
class Scratch {
    public static void main(String[] args) {
        // Olá, {nome}. Hoje é {dia-da-semana}, BOM DIA.


          String nome = "Juliana";
//        System.out.println(nome.toUpperCase());
//        System.out.println(nome.toLowerCase());
//        System.out.println(nome.length());
//
//        String nomeOutro = "juliana";
//        System.out.println(nome.equals(nomeOutro));
//        System.out.println(nome.equalsIgnoreCase(nomeOutro));

        // ISO 8601 - Padrão Mundial de Data
        LocalDate hoje = LocalDate.now();
        Locale brasil = new Locale("pt","BR");
        //Locale brasil = new Locale("pt","BR");

        System.out.println(hoje.getDayOfWeek().getDisplayName(TextStyle.FULL,brasil));
        String diaSemana = (hoje.getDayOfWeek().getDisplayName(TextStyle.FULL,brasil));
        String saudacao;
        LocalDateTime agora = LocalDateTime.now();

        if (agora.getHour() >= 0 && agora.getHour()<12){
            saudacao = "BOM DIA";
        }else if (agora.getHour() >=12 && agora.getHour() < 18){
            saudacao = "BOA TARDE";
        }else if (agora.getHour() >=18 && agora.getHour() < 24) {
            saudacao = "BOA NOITE";
        }else {
            saudacao = "OLÁ";
        }

        System.out.printf("Olá, %s. Hoje é %s, %s. %n", nome, diaSemana, saudacao.toUpperCase());

    }
}