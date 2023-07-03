inter = gremio = empates = 0

while (True):
    gols_inter, gols_gremio = input().split()
    gols_inter, gols_gremio = int(gols_inter), int(gols_gremio)
    
    if (gols_inter > gols_gremio):
        inter = inter + 1
    elif (gols_gremio > gols_inter):
        gremio = gremio + 1
    else:
        empates = empates + 1
        
    print("Novo grenal (1-sim 2-nao)")
    res = int(input())
    if (res == 2):
        break
    
grenais = inter + gremio + empates

print(grenais, "grenais")
print("Inter:", inter, sep="")
print("Gremio:", gremio, sep="")
print("Empates:", empates, sep="")

if (inter > gremio):
    print("Inter venceu mais")
elif (gremio > inter):
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")

    
    
        
        
