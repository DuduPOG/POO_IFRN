import java.util.Scanner;
public class OlaMundo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int idade;
        String nome;
        
        nome = sc.next();
        System.out.printf("Digite seu nome: %s%n", nome);
        idade = sc.nextInt();
        System.out.printf("Digite sua idade: %d%n", idade);
        sc.next();
        System.out.printf("Olá, %s! Você tem %d anos%n.", nome, idade);
        sc.close();
    }
}