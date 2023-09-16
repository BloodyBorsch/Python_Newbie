namespace HomeWork
{
    public class Example1
    {
        private static int _numberOne = 0;
        private static int _numberTwo = 10;        

        private static void Main(string[] args)
        {           
            Randomizer(_numberOne, _numberTwo);
        }

        private static void Randomizer(int min, int max)
        {
            Console.WriteLine(new Random().Next(min, max));            
        }
    }
}