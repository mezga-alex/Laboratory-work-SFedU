using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Percents
{
    class Program
    {
        public static double Calculate(string userInput)
        {
            // Split string by spaces
            string[] splitInput = userInput.Split(' ');

            // Convert types
            double P = double.Parse(splitInput[0], System.Globalization.CultureInfo.InvariantCulture); // Initial deposit amount
            double I = double.Parse(splitInput[1], System.Globalization.CultureInfo.InvariantCulture); // Annual percentage rate
            int t = int.Parse(splitInput[2]); // Term of deposit in months

            // In case of monthly capitalization:
            // P * ((1 + I / (12 * 100))^t
            // P - initial deposit amount
            // I - Annual percentage rate
            // t - term of deposit in months
            return P * Math.Pow((1 + I / (12 * 100)), t);
        }
        static void Main(string[] args)
        {
            string input =  Console.ReadLine();
            double res = Calculate(input);
            Console.WriteLine(res);
            Console.ReadKey();
        }
    }
}
