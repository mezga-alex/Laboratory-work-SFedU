using System;

namespace bit_array
{
    public class BitArraySimple
    {
        private byte[] arr;
        public BitArraySimple(int n)
        {
            int size = n / 8;
            if (n % 8 != 0)
            {
                size++;
            } 

            //Console.WriteLine(size);
            this.arr = new byte[size];
        }

        public void set_byte(byte cur_byte, int pos)
        {
            this.arr[pos] = cur_byte;
        }

        public int get_byte(int pos)
        {
            return this.arr[pos];
        }

        public void set_bit(byte val, int pos)
        {
            if (pos < 1 || pos > this.arr.Length * 8)
            {
                Console.WriteLine("Ti daun");
                return;
            }
            
            if (val > 1)
            {
                Console.WriteLine("Only 0 and 1 available");
                return;
            }
            Console.WriteLine($"Set {val} on position {pos}");
            pos--;
            int byte_pos = pos / 8;
            int bit_pos = pos % 8;

            bit_pos = 7 - bit_pos;
            val <<= bit_pos;
            //Console.WriteLine($"Shifted byte: {Convert.ToString(val, toBase: 2)}");
            this.arr[byte_pos] |= val;
            
            Console.WriteLine($"This is {byte_pos} byte with {bit_pos} bit pos(0..7, start from right)");
            Console.WriteLine($"Mask: {Convert.ToString(val, toBase: 2)}");
            Console.WriteLine($"Shifted byte: {Convert.ToString(this.arr[byte_pos], toBase: 2)}");
            Console.WriteLine();
        }
    }
}