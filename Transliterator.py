#Das Programm wurde in Python entworfen, hier seht ihr die aktuellste Version
#In den grünen Kommentaren findet ihr jeweils eine Erklärung, was die Zeile Code darüber macht und in Klammern den jeweiligen Fachbegriff (falls ich ihn kenne)
from curses.ascii import islower
import re
#Importieren von Regex, siehe unten


Austauschliste = {"ch":"tsch","kh":"ch","ks":"x","zh":"sch","sh":"sch","tz":"z","ts":"z","v":"w","z":"s","shch":"schtsch" }
#Aus der Tabelle zur Umschrift aus dem Englischen ins Deutsche (https://docs.google.com/document/d/1jCjfOibMW0nGcjV0kygoX7GssWtOuYB2G8m1jYDED-Y/edit#)
#Diesen Buchstaben oder Silben (Substrings) werden Gegenstücke zugewiesen (in der Form Schlüssel/Key:Wert/Value), durch die sie ersetzt werden -> zB "ch" wird zu "tsch"

def transliterator():
    transliterat = input("Was soll transliteriert werden? ")
    #Speichert die Eingabe in der Variable transliterat
    res = []
    #Generiert eine leere Liste, siehe unten
    transliteriert = transliterat.lower()
    #Zur Vereinfachung werden alle Eigennamen kleingeschrieben und die Variable umbenannt
    for x in Austauschliste.keys():
        if x in transliteriert:
            res.append(x)
    #durchläuft die Eingabe und sucht nach Schlüsseln, die sich in der Austauschliste befinden und fügt sie in eine Liste (namens res für result) ein
    for key in res:
        transliteriert = transliteriert.replace(key,Austauschliste[key])
    #Für jeden gefundenen Schlüssel in der Liste res wird der Schlüssel/Key durch sein Gegenstück (Value) ersetzt
    
    #Ab hier werden Sonderfälle (edge cases) abgearbeitet
    if transliteriert.endswith("ey"):
            transliteriert = transliteriert.replace("ey","ej")
    #wird ein "ey" am Ende gefunden, wird es durch "ej" ersetzt
    #Um komplexere Muster in der Eingabe zu erkennen (Pattern Matching), wird das Konzept der regulären Ausdrücke (English Regular Expressions oder Regex) angewandt
    #Die Bibliothek zur Benutzung in Python heißt re und folgt diesen Mustern (https://www.dataquest.io/blog/regex-cheatsheet/)
    pattern = "y$"
    finalresult = re.sub(pattern, r"i",transliteriert)
    #Befindet sich am Ende der Eingabe ein y (hier angegeben durch das $ nach dem y), wird es durch ein i ersetzt
    pattern1 = "y([aeiou])"
    final_result1 = re.sub(pattern1,r'j\1',finalresult)
    #Befindet sich ein y vor einem Vokal, wird es durch ein j ersetzt
    pattern2 = "([aeiou])s([aeiou])"
    final_result2 = re.sub(pattern2,r"\1ss\2",final_result1)
    #Befindet sich ein s zwischen zwei Vokalen, wird es durch ss ersetzt
    pattern3 = "(i)(i)"
    final_result3 = re.sub(pattern3,r"\1j\2",final_result2)
    #Zwischen zwei i's wird ein j eingefügt
    pattern4 = "i([aeiou])"
    final_result4 = re.sub(pattern4,r"j\1",final_result3)
    #Befindet sich ein i vor einem Vokal, wird es durch ein j ersetzt.
    print(final_result4.capitalize())
    #Zuletzt wird das fertige Wort noch großgeschrieben und ausgegeben
    
while True:
    transliterator()
    #Dauerschleife, um weiter nach einer Eingabe zu fragen
