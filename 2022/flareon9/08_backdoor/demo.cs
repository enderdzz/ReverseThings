using System;
using System.Reflection;
using System.Reflection.Emit;

public class Demo
{
    public static void Main()
    {
        DynamicMethod dm = new DynamicMethod("HelloWorld", typeof(void), Type.EmptyTypes, typeof(Demo), false);
        DynamicILInfo il = dm.GetDynamicILInfo();

        SignatureHelper sigHelper = SignatureHelper.GetLocalVarSigHelper();
        il.SetLocalSignature(sigHelper.GetSignature());

        byte[] code = { 0x00, 0x72, 0x01, 0x00, 0x00, 0x70, 0x27, 0x04, 0x00, 0x00, 0x0a, 0x00, 0x2a };
        int token0 = il.GetTokenFor("Hello world");
        int token1 = il.GetTokenFor(typeof(Console).GetMethod("WriteLine", new Type[] { typeof(string) }).MethodHandle);
        PutInteger4(token0, 0x0002, code);
        PutInteger4(token1, 0x0007, code);
        il.SetCode(code, 8);

        dm.Invoke(null, null);
　　     Console.Read();
    }

    static void PutInteger4(int value, int startPos, byte[] array)
    {
        array[startPos++] = (byte)value;
        array[startPos++] = (byte)(value >> 8);
        array[startPos++] = (byte)(value >> 16);
        array[startPos++] = (byte)(value >> 24);
    }
}