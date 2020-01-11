import re

diz={"m":[],"f":[]}
file_m = open("NOMI_MASCHILI.txt","r")
nome_m = ""
listam=file_m.read()
file_m.close()
for i in listam:
  if i == ",":
    diz["m"] = diz["m"] + [nome_m]
    nome_m = ""
  elif i == " ":
    continue
  else:
    nome_m = nome_m + i

file_f = open("NOMI_FEMMINILI.txt","r")
nome_f = ""
listaf=file_f.read()

for i in listaf:
  if i == ",":
    diz["f"] = diz["f"] + [nome_f]
    nome_f = ""
  elif i == " ":
    continue
  else:
    nome_f = nome_f + i

while True:
  print("(digita 'fine' per uscire)\n")
  nome=input("Inserisci un nome proprio italiano:\n")
  if nome.lower().capitalize() in diz["m"]:
    print("\nIl nome è maschile\n")
  elif nome.lower().capitalize() in diz["f"]:
    print("\nIl nome è femminile\n")
  elif not bool(re.fullmatch(r'[a-zA-Z]+', nome)):
    print("Non hai inserito un nome proprio\n")
  elif nome == "fine":
    break
  else:
    print("Il nome non è presente nel mio dizionario.\n")
    if nome.lower().endswith("o"):
      try:
        flag = int(input("Provo ad indovinare. E un nome maschile?(SI = 1, NO = 0)\n"))
        if flag == 0:
          print("Peccato. Ora inserisco questo nuovo nome femminile nel dizionario\n")
          diz["f"] = diz["f"] + [nome.lower().capitalize()]
          print("Nome inserito\n")
          continue
        elif flag == "fine":
          break
        else:
          print("Bene. Ora inserisco questo nuovo nome maschile nel dizionario\n")
          diz["m"] = diz["m"] + [nome.lower().capitalize()]
          print("Nome inserito\n")
          continue
      except:
        print("Hai inserito un valore inatteso\n")
        continue
    elif nome.lower().endswith("a"):
      try:
        flag = int(input("Provo ad indovinare. E un nome femminile?(SI = 1, NO = 0)\n"))
        if flag == 0:
          print("\nPeccato. Ora inserisco questo nuovo nome maschile nel dizionario\n")
          diz["m"] = diz["m"] + [nome.lower().capitalize()]
          print("Nome inserito\n")
          continue
        elif flag == "fine":
          break
        else:
          print("Bene. Ora inserisco questo nuovo nome femminile nel dizionario\n")
          diz["f"] = diz["f"] + [nome.lower().capitalize()]
          print("Nome inserito")
          continue
      except:
        print("Hai inserito un valore inatteso\n")
        continue
    else:
        gen = input("Non riesco ad indovinare. Dimmi te se è un nome maschile o femminile. f/F = femminile - m/M = maschile:\n")
        try:
          if gen.lower() in diz.keys():
            if gen.lower() == "m":
              diz["m"] = diz["m"] + [nome.lower().capitalize()]
              print("\nNome inserito\n")
              continue
            else:
              diz["f"] = diz["f"] + [nome.lower().capitalize()]
              print("Nome inserito\n")
              continue
          elif gen == "fine":
              break
        except:
          print("Hai inserito un valore inatteso!\n")
          continue





