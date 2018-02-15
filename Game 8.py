print("Please Enter Number of Coins to Start The Game")
while True :
    try :
      coins=int(input("Enter Number of Coins: "))
    except Exception as e :
        print("Not Valid")
        continue
    break
while coins<=1 :
    print("Not Valid")
    while True :
        try :
          coins=int(input("Enter Number of Coins: "))
        except Exception as e :
          print("Not Valid")
          continue
        break
while True :
    try :  
      player1=int(input("Player1: "))
    except Exception as e :
        print("Not Valid")
        continue
    break
while player1>=coins or player1<=0 :
    print("Not Valid")
    while True :
       try :  
          player1=int(input("Player1: "))
       except Exception as e :
          print("Not Valid")
          continue
       break
newcoins=coins-player1
print("The New Coins is: ",newcoins)
for i in range (newcoins) :
    while True :
        try :
           player2=int(input("Player2: "))
        except Exception as e :
            print("Not Valid")
            continue
        break
    while player2<=0 or player2>newcoins or player2>2*player1 :
        print("Not Valid")
        while True :
            try :
                player2=int(input("Player2: "))
            except Exception as e :
                print("Not Valid")
                continue
            break    
    ncoins=newcoins-player2
    print("The New Coins is: ",ncoins)
    if ncoins==0 :
        print("Player2 won")
        print("End Game")
        break
    while True :
        try :  
          player1=int(input("Player1: "))
        except Exception as e :
            print("Not Valid")
            continue
        break
    while player1<=0 or player1>ncoins or player1>2*player2  :
        print("Not Valid")
        while True :
            try :
               player1=int(input("Player1: "))
            except Exception as e :
               print("Not Valid")
               continue
            break  
    coins=ncoins-player1
    print("The New Coins is: ",coins)
    if coins==0 :
       print("Player1 won")
       print("End Game")
       break
    newcoins=coins
