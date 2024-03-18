// string curso = "ADS";
// string discplina = "LP";

// Console.WriteLine(curso);
// Console.WriteLine(discplina);

//object

// object nota = 10;
// object valor1 = 8.55m;
// object nome1 = "maria";
// object ativa = true;
// object letra = 'A';

// Console.WriteLine(nota);
// Console.WriteLine(valor1);
// Console.WriteLine(nome1);
// Console.WriteLine(ativa);
// Console.WriteLine(letra);


//dynamic

// dynamic nota = 10;
// dynamic valor1 = 8.55m;
// dynamic nome1 = "maria";
// dynamic ativa = true;
// dynamic letra = 'A';

// Console.WriteLine(nota);
// Console.WriteLine(valor1);
// Console.WriteLine(nome1);
// Console.WriteLine(ativa);
// Console.WriteLine(letra);

//tipos nulos
Nullable<int> x = null;
int? y = null;

if(y.HasValue)
{
    Console.WriteLine("y possui valor");
}

else{
    Console.WriteLine("y n possui valor");
}

