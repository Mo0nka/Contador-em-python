#Unidades de tempo para fazer a contagem.
milesimos = 0
segundos = 0
minutos = 0
horas = 0
dias = 0

#Começa a contar
while True:
    milesimos += 1
    #print (str(milesimos) + ' milésimos.')
    
    #Se 'milesimos' for igual a 9_000_000, ele adiciona mais um em 'segundos'.
    if milesimos == 9_000_000:
        milesimos = 0
        segundos += 1
        print (str(segundos) + ' segundos.')

        #Se 'segundos' for igual a 60, ele adiciona mais um a 'minutos'.
        if segundos == 60:
            segundos = 0
            minutos += 1
            print ('\n\t' + str(minutos) + ' minutos\n')
            
            #Se 'minutos' for igual a 60, ele adiciona mais um a 'horas'.
            if minutos == 60:
                minutos = 0
                horas += 1
                print ('\n\t' + str(horas) + ' horas\n')
                
                #Se 'horas' for igual a 24, ele adiciona mais um a 'dias'.
                #Provavelmente niguém vai passar um dia com isso funcionando para ver se funciona realmente.
                if horas == 24:
                    horas = 0
                    dias += 1
                    print ('\n\t' + str(dias) + ' dias\n')
            
