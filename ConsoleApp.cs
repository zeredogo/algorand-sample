using system;
namespace DApp
{
    -reference
    class Program
    {
        -references
        static void Main(string[] args)
        {
            Account account - new Account();
            var a = "YSXJSJHNDXZNSME&Y*EJWSJ67UEUEJUEHDE";
            if (Address.IsVAlid(a))
            {
                console.WrileLine("Address is  Valid")
            }
            else
            {
                console.WrileLine("Address is not valid");
            }
            console.WrileLine(account.Address.ToString());
        }
    }
}