public class TaskNew
{
    public static string[] coorditanes = { "x1: ", "y1: ", "z1: ", "x2: ", "y2: ", "z2: " }; // [] <- массив!
    public static int[] variables = new int[coorditanes.Length];
    public static Tools testTwo;

    static void Main(string[] args)
    {        
        testTwo = new TaskTwo();
        testTwo.Start();

        //for (int i = 0; i < coorditanes.Length; i++)
        //{
        //    Console.Write(coorditanes[i]);
        //    variables[i] = Convert.ToInt32(Console.ReadLine());
        //}

        //int A = DistanceCheck(DigitalNumbers.X2, variables) - DistanceCheck(DigitalNumbers.X1, variables); //int A = x2 - x1;
        //int B = DistanceCheck(DigitalNumbers.Y2, variables) - DistanceCheck(DigitalNumbers.Y1, variables); //int B = y2 - y1;
        //int C = DistanceCheck(DigitalNumbers.Z1, variables) - DistanceCheck(DigitalNumbers.Z2, variables); //int C = z1 - z2;

        //double length = Math.Sqrt(A * A + B * B + C * C);
        //Console.WriteLine($"расстояние между точками в 3D пространстве -> {Math.Round(length, 2)}");
    }

    static int DistanceCheck(DigitalNumbers coord, int[] array)
    {
        switch (coord)
        {
            case DigitalNumbers.X1:
                return array[(int)DigitalNumbers.X1];
            case DigitalNumbers.Y1:
                return array[(int)DigitalNumbers.Y1];
            case DigitalNumbers.Z1:
                return array[(int)DigitalNumbers.Z1];
            case DigitalNumbers.X2:
                return array[(int)DigitalNumbers.X2];
            case DigitalNumbers.Y2:
                return array[(int)DigitalNumbers.Y2];
            case DigitalNumbers.Z2:
                return array[(int)DigitalNumbers.Z2];
            default:
                Console.WriteLine("Нет такой координаты!");
                return 0;
        }
    }
}

public enum DigitalNumbers
{
    X1,
    Y1,
    Z1,
    X2,
    Y2,
    Z2
}

public class TestOne : HomeWorks
{
    public void Start()
    {
        Console.WriteLine($"Тестовый класс запущен");
    }

    public void WrongMethod()
    {

    }
}

public interface HomeWorks
{
    void Start();
}