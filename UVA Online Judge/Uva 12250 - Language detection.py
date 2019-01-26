i = 1
while True:
    try:
        n = str(input())
        if n=='#':
            break
        elif n=='HELLO':
            print("Case %d: ENGLISH" %i)
        elif n=='HOLA':
            print("Case %d: SPANISH" %i)
        elif n=='HALLO':
            print("Case %d: GERMAN" %i)
        elif n=='BONJOUR':
            print("Case %d: FRENCH" %i)
        elif n=='CIAO':
            print("Case %d: ITALIAN" %i)
        elif n=='ZDRAVSTVUJTE':
            print("Case %d: RUSSIAN" %i) 
        else:
            print("Case %d: UNKNOWN" %i)
        i+=1
    except EOFError:
            break

                  
    
