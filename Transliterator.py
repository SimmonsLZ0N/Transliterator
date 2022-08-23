from curses.ascii import islower
import re

Austauschliste = {"ch":"tsch","kh":"ch","ks":"x","zh":"sch","sh":"sch","tz":"z","ts":"z","v":"w","z":"s","shch":"schtsch" }
#Aus der Tabelle zur Umschrift aus dem Englischen ins Deutsche (https://docs.google.com/document/d/1jCjfOibMW0nGcjV0kygoX7GssWtOuYB2G8m1jYDED-Y/edit#)
#Diesen Buchstaben oder Silben (Substrings) werden Gegenstücke zugewiesen (Key:Value), durch die sie ersetzt werden -> zB "ch" wird zu "tsch"




def transliterator():
    transliterat = input("Was soll transliteriert werden? ")
    res = []
    transliteriert = transliterat.lower()
    #Zur Vereinfachung werden alle Eigennamen kleingeschrieben
    for x in Austauschliste.keys():
        if x in transliteriert:
            res.append(x)
    #durchläuft die Eingabe und sucht nach Keys, die sich in der Austauschliste befinden und fügt sie in eine Liste (namens res für result) ein
    for key in res:
        transliteriert = transliteriert.replace(key,Austauschliste[key])
    #Für jeden gefundenen Key in der Liste res wird der Key durch sein Gegenstück ersetzt
    #Ab hier werden Sonderfälle (edge cases) abgearbeitet
    if transliteriert.endswith("ey"):
            transliteriert = transliteriert.replace("ey","ej")
    #wird ein "ey" am Ende gefunden, wird es durch "ej" ersetzt
    pattern = "y$"
    finalresult = re.sub(pattern, r"i",transliteriert)
    #Befindet sich am Ende der Eingabe ein y, wird es durch ein i ersetzt
    pattern1 = "y([aeiou])"
    final_result1 = re.sub(pattern1,r'j\1',finalresult)
    #Befindet sich ein y vor einem Vokal, wird es durch einen j ersetzt
    pattern2 = "([aeiou])s([aeiou])"
    final_result2 = re.sub(pattern2,r"\1ss\2",final_result1)
    #Befindet sich ein s zwischen zwei Vokalen, wird es durch ss ersetzt
    pattern3 = "(i)(i)"
    finalresult3 = re.sub(pattern3,r"\1j\2",final_result2)
    #Zwischen zwei i's wird ein j eingefügt
    print(finalresult3.capitalize())
    #Zuletzt wird das fertige Wort noch großgeschrieben und ausgegeben
    
while True:
    transliterator()
    #Dauerschleife, um weiter nach einer Eingabe zu fragen