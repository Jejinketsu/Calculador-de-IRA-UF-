def media (lista):
    return sum(lista)/len(lista)

mediaNotas = []
cHorariaTotal = []

quantMaterias = int(input("Quantas matérias você tem? "))

for i in range (0, quantMaterias):
    notas = []
    
    print("\nMatéria %d"% (i+1))
    cHoraria = float(input("Qual a Carga Horária dessa matéria? "))
    cHorariaTotal.append(cHoraria)
    quantNotas = 0
    if cHoraria == 15:
        quantNotas = 1
    elif cHoraria == 30:
        quantNotas = 2
    elif cHoraria == 60:
        quantNotas = 3
    elif cHoraria == 90:
        quantNotas = 4
    
    for j in range(0, quantNotas):
        while(1):
            try:
                notas.append(float(input("nota %d: "% (j+1))))
                break
            except (ValueError):
                print("Valor incorreto. Obs: use . para números decimais.")

    mediaNotas.append(media(notas)*cHoraria)

IRA = sum(mediaNotas)/sum(cHorariaTotal)
print("IRA: %f"% IRA)  