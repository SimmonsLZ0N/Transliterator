
from curses.ascii import islower
import re



Austauschliste = {"ch":"tsch","kh":"ch","ks":"x","zh":"sch","sh":"sch","tz":"z","ts":"z","v":"w","z":"s","shch":"schtsch" }

def transliterator():
    transliterat = input("Was soll transliteriert werden? ")
 
    res = []

    transliteriert = transliterat.lower()
    for x in Austauschliste.keys():
        if x in transliteriert:
            res.append(x)
    
    for key in res:
        transliteriert = transliteriert.replace(key,Austauschliste[key])
  
    
  
    if transliteriert.endswith("ey"):
            transliteriert = transliteriert.replace("ey","ej")
    
    pattern = "y$"
    finalresult = re.sub(pattern, r"i",transliteriert)
 
    pattern1 = "y([aeiou])"
    final_result1 = re.sub(pattern1,r'j\1',finalresult)
   
    pattern2 = "([aeiou])s([aeiou])"
    final_result2 = re.sub(pattern2,r"\1ss\2",final_result1)
  
    pattern3 = "(i)(i)"
    final_result3 = re.sub(pattern3,r"\1j\2",final_result2)
   
    pattern4 = "i([aeiou])"
    final_result4 = re.sub(pattern4,r"j\1",final_result3)
   
    print(final_result4.capitalize())
   
    
while True:
    transliterator()
    
