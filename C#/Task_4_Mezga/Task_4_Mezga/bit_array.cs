using System;
using System.Collections.Generic;

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

            this.arr = new byte[size];
        }

        public void Print()
        {
            foreach (var cur_byte in this.arr)
                Console.Write(Convert.ToString(cur_byte, 2).PadLeft(8, '0') + " ");
            Console.WriteLine();
        }
        public int this[int pos]
        {
            get
            {
                if (pos < 1 || pos > arr.Length * 8)
                {
                    Console.WriteLine("Incorrect position");
                    return -1;
                }

                pos--;
                int byte_pos = pos / 8;
                int bit_pos = pos % 8;

                bool pos_val = (arr[byte_pos] & (1 << bit_pos)) != 0;

                return Convert.ToInt32(pos_val);
            }

            set
            {
                if (pos < 1 || pos > arr.Length * 8)
                {
                    Console.WriteLine("Incorrect position");
                    return;
                }

                if (value > 1)
                {
                    Console.WriteLine("Only 0 and 1 available");
                    return;
                }

                pos--;
                int byte_pos = arr.Length - pos / 8 - 1;
                int bit_pos = pos % 8;

                bool is_complement = false;
                if (value == 0)
                {
                    is_complement = true;

                    value = 1;
                    arr[byte_pos] = (byte)~arr[byte_pos];
                }

                arr[byte_pos] |= (byte)(value << bit_pos);

                if (is_complement)
                {
                    arr[byte_pos] = (byte)~arr[byte_pos];
                }

            }
        }
    }

    public class BitArrayDict
    {
        private Dictionary<string, int> a;

        public BitArrayDict()
        {
            a = new Dictionary<string, int>();

        }
        public int this[string s]
        {
            get
            {
                return a[s];
            }

            set
            { 
                a[s] = value;
            }
        }
    }
}