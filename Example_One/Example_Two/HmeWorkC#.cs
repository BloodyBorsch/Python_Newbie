using System.Diagnostics;
using System.Diagnostics.CodeAnalysis;
using System.Runtime.CompilerServices;


int xa = 40;
int ya = 1;
int xb = 1;
int yb = 30;
int xc = 80;
int yc = 30;

int x = 0;
int y = 0;

Console.SetCursorPosition(xa, ya);
Console.WriteLine("+");

Console.SetCursorPosition(xb, yb);
Console.WriteLine("+");

Console.SetCursorPosition(xc, yc);
Console.WriteLine("+");

for (int count = 0; count < 10000; count++)
{
    int what = new Random().Next(0, 3);

    Switcher(what);

    Console.SetCursorPosition(x, y);
    Console.WriteLine("+");

    void Switcher(int number)
    {
        switch (number)
        {
            case 0:
                x = (x + xa) / 2;
                y = (y + ya) / 2;
                break;
            case 1:
                x = (x + xb) / 2;
                y = (y + yb) / 2;
                break;
            case 2:
                x = (x + xc) / 2;
                y = (y + yc) / 2;
                break;
            default:
                Console.WriteLine("Свитчер вышел за пределы значений");
                break;
        }
    }
}