# Description and status

### P1 is sample node .... P2 P3 are just copies of P1 with just different ports, So please refer P1 and try because P2 and P3 may not be updated



EACH NODE HAS DEDICATED PORT (except Pn)
here 10001 10002 10003

1)So,Pn sends using TCP to all ports (DONE and WORKING)

2)P1 recvs msg and generates it hash (DONE and WORKING)
  and shares its hash TO ALL NODES AT ONE. (DONE something and NOT WORKING) --- check shareMyHash() in P1

>The above step requires Multicast

>THIS MULTICASTING CODE IS COMPLEX AS FUCK AND I COULDN'T GET ONE WORKING

>FURTHUR, EVEN IF MULTICAST WORKS, WHEN A NODE MULTICASTS OTHER NODES SHOULDN'T. (SYNC PROBLEM)


>AN ALTERNATIVE FOR ABOVE STEP IS IT SENDS TO ALL NODES ONE BY ONE

>IT'S WON'T BE PROPER THIS WAY

>FOR EXAMPLE, IN CASE OF BLOCKCHAIN which is one of the applications of our protocol, ALL NODES WILL MULTICAST THEIR VALUES NOT ONE-BY-ONE.

3)Verify hash and print respective msg. (WILL BE DONE EASILY and WILL BE WORKING)


## YOU CAN
          COMPLETE THIS PIECE OF CODE
          FIND AND TRY AN ALTERNATIVE FOR ANY STEP OF THIS CODE
          WRITE A WHOLE NEW CODE
          ANYTHING YOU THINK WHICH MAKES SENSE :)
          
          
          
          
          
          
          
          
          
________________________________________________________________________
**I WONT BE AVAILABLE TODAY AND MAY NOT BE TOMORROW because of a ceremony in my house.
CAN CALL ME BUT NOT AT ODD TIMES FOR A FAMILY**
