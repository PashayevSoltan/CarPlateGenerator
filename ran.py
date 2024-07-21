import random
import time 
istisna_seriyalar = [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98]
bolge_kodu = random.randint(1,99)
herf_seryasi1 = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "R", "S", "T", "U", "V", "Y", "Z"]
herf_seryasi2 = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "R", "S", "T", "U", "V", "Y", "Z"]
nomre_kodu_son_uc_reqem = random.randint(100, 999)
if bolge_kodu < 10:
  bolge_kodu = f"0{bolge_kodu}"

if nomre_kodu_son_uc_reqem < 100:
  nomre_kodu_son_uc_reqem = f"0{nomre_kodu_son_uc_reqem}"

nomre = f"{bolge_kodu}-{random.choice(herf_seryasi1)}{random.choice(herf_seryasi2)}-{nomre_kodu_son_uc_reqem}"
if bolge_kodu not in istisna_seriyalar:
  print(nomre)


