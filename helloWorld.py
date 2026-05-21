def greeting( messages ):

   mainMessage = "Hello World"

   messageCount = 1
   messageCount += len( messages )

   print( mainMessage )

   for message in messages:
      print( message )

   print( f"That was {messageCount} message(s)" )

def getGreetings():
   return [
      "This is my first Python programm",
      "It shows variables, loops and functions",
      "Have a nice day"
   ]
   
def main():
   greeting( getGreetings() )

if __name__ == "__main__":
   main()

