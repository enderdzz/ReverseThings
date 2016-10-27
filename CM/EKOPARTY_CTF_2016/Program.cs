using System;
using System.Globalization;

namespace FlagGen
{
    public static class Program
    {
        public static string get_flag(string str)
        {
            int[] array = StringInfo.ParseCombiningCharacters(str);

            int num = array.Length;

            string[] array2 = new string[num];
            int num2 = 0;
            int num3 = num - 1;
            if (num3 >= num2)
            {
                do
                {
                    if (num2 == array.Length - 1)
                    {
                        array2[num2] = str.Substring(num2);
                    }
                    else
                    {
                        int num4 = array[num2];
                        array2[num2] = str.Substring(num4, array[num2 + 1] - num4);
                    }
                        num2++;
                }
                while (num2 != num3 + 1);
            }
            string[] array3 = array2;
            Array.Reverse(array3);
            return string.Join("", array3);
        }
        public static int Main(string[] argv)
        {
            string text = Program.get_flag("t#hs_siht_kc#f");
            Console.WriteLine(text);
            return 0;
        }
    }
}
