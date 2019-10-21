using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace bit_array
{

    class Program
    {
        static void Main(string[] args)
        {
            BitArraySimple bit_array = new BitArraySimple(19);

            bit_array[1] = 1;
            bit_array[4] = 1;
            bit_array[17] = 1;
            bit_array[9] = 1;
            bit_array[24] = 1;
            bit_array[16] = 1;
            bit_array.Print();

            bit_array[1] = 0;
            bit_array[9] = 0;
            bit_array.Print();

            BitArrayDict bit_dict = new BitArrayDict();

            //Console.WriteLine(bit_array[9]);
            Console.ReadLine();
        }
    }
}
