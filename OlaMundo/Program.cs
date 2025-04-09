namespace OlaMundo;
class Program
{
    static void Main(string[] args)
    {
        Console.Write("Digite seu nome: ");
        string nome = Console.ReadLine(); // Lê a linha inteira, incluindo espaços

        Console.Write("Digite sua idade: ");
        int idade = int.Parse(Console.ReadLine()); // Lê a linha e converte para inteiro

        Console.WriteLine($"Olá, {nome}! Você tem {idade} anos.");
    }
}