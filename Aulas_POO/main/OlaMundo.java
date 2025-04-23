import java.util.Scanner;
public class OlaMundo {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int idade;
            String nome;
            
            System.out.println("Digite seu nome: ");
            nome = sc.next();
            System.out.println("Digite sua idade: ");
            idade = sc.nextInt();
            System.out.printf("Olá, %s! Você tem %d anos%n.", nome, idade);
        }
    }
}