from sqlalchemy import desc
import db

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

for nomi in diz["f"]:
  post = Post(nome= nomi , genere=True) 
  db.session.add(post)
  db.session.commit()

for nomi in diz["m"]:
  post = Post(nome= nomi , genere=False) 
  db.session.add(post)
  db.session.commit()







