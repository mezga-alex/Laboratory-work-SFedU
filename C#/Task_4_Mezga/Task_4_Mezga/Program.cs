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
            //bit_array.set_byte(, 1);
            //Console.WriteLine(bit_array.get_byte(0));

            //bool f = 0;
            bit_array.set_bit(1, 1);
            bit_array.set_bit(1, 5);
            bit_array.set_bit(1, 8);
            bit_array.set_bit(1, 9);
            bit_array.set_bit(1, 12);
            bit_array.set_bit(1, 16);
            Console.ReadLine();
        }
    }
}
