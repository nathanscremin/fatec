using System;
class Program {
    static void Main() {
        Random rnd = new Random(); // cria uma instância da classe Random
        int nrandom = rnd.Next(1, 101); // número entre 1 e 100

        bool cond = true;

        while (cond == true) {
            Console.WriteLine("Insira um numero de 1 a 100:");
            int n1 = int.Parse(Console.ReadLine());
    
            if (nrandom == n1) {
                Console.WriteLine("Numero correto!");
                cond = false;
            } else if (nrandom > n1) {
                Console.WriteLine("Muito baixo.");
            } else if (nrandom < n1) {
                Console.WriteLine("Muito alto.");
            }
        }
    }
}