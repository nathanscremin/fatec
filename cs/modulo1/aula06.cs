// ARRAYS
int[] numeros = { 1, 2, 3, 4 };
Console.WriteLine(numeros[0]); // 1

// Percorrendo com for
for (int i = 0; i < numeros.Length; i++)
    Console.WriteLine(numeros[i]);

// ou com foreach
foreach (int num in numeros)
    Console.WriteLine(num);
