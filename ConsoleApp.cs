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
            
                console.WrileLine("Address is not valid");
             AlgodApi AlgodApiInstance = new AlgodApi("https://testnet-algorand.api.purestake.io/ps1", "YSXJSJHNDXZNSME&Y*EJWSJ67UEUEJUEHDE");
             var accountInfo = AlgodApiInstance.AccountInformation(a.ToString());   
             console.WrileLine($"Account Balance of {a} is {accountInfo.Amount}");
        }
    }
}