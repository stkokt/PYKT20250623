# Es soll eine zufällig ausgewählte Zahl von 1 - 100 geraten werden.
# Bei jedem Rateversuch wird ausgewertet, ob die geratene Zahl 
# größer oder kleiner als die Zufallszahl ist.
# Wir simulieren das Ratespiel mit einer Binärsuche (Zeitkomplexität O(log n) = superschnell)
# Immer wenn die geratene Zahl kleiner als die Zufallszahl ist,
# wird die untere Intervallgrenze des Suchbereichs auf die 
# geratene Zahl verschoben und vice versa
# wenn die geratene Zahl größer als die Zufallszahl ist,
# wird die obere Intervallgrenze des Suchbereichs auf die 
# geratene Zahl verschoben.
# Die neue geratene Zahl liegt immer in der Mitte des Suchbereichs.

from random import randint
# Zum Nachweis, wie effizient der Suchalgorithmus ist,
# spielen wir das ganze 10 Mal durch.
for n,runs in enumerate(range(10)):
    zufallszahl = randint(1,10000)
    geraten = 0
    untere_intervallgrenze = 1
    obere_intervallgrenze = 10001
    versuche = 0
    print(f"Run {n+1}\nDie Zufallszahl lautet: {zufallszahl}")
    # Wetten, dass wir es immer innerhalb von 10 Versuchen schaffen?
    for x in range(10):
        versuche += 1
        if geraten < zufallszahl:
            untere_intervallgrenze = geraten
            geraten += (obere_intervallgrenze - untere_intervallgrenze)//2
        if geraten > zufallszahl:
            obere_intervallgrenze = geraten
            geraten -= (obere_intervallgrenze - untere_intervallgrenze)//2
        if geraten == zufallszahl:
            print(f"Treffer bei Versuch Nr.{versuche}\n")
            break


"""
Es gibt viele ausgezeichnete Bücher und Ressourcen zum Thema effiziente Algorithmen in der Programmierung. Hier sind einige Empfehlungen:

ENGLISCHSPRACHIG

1. **"Introduction to Algorithms"** von Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest und Clifford Stein.
   - Dieses Buch ist auch als "CLRS" bekannt und gilt als Standardwerk für das Studium von Algorithmen. Es bietet eine umfassende Einführung in eine Vielzahl von Algorithmen und deckt auch deren Komplexität und Effizienz ab.

2. **"Algorithms"** von Robert Sedgewick und Kevin Wayne.
   - Dieses Buch ist sehr zugänglich und bietet eine gute Einführung in grundlegende Datenstrukturen und Algorithmen. Es enthält auch viele Beispiele in Java.

3. **"The Algorithm Design Manual"** von Steven S. Skiena.
   - Dieses Buch bietet eine praktische Herangehensweise an das Design und die Analyse von Algorithmen und enthält viele Beispiele und Übungen.

4. **"Algorithmics: The Spirit of Computing"** von David Harel mit Yishai Feldman.
   - Dieses Buch bietet eine Einführung in die Welt der Algorithmen und deren Bedeutung für die Informatik.

5. **"Algorithms Unlocked"** von Thomas H. Cormen.
   - Ein weiteres Buch von Cormen, das sich an Leser richtet, die eine weniger formale und mathematische Einführung in Algorithmen suchen.

Diese Bücher sind weit verbreitet und werden oft in Universitätskursen verwendet. Sie bieten eine solide Grundlage für das Verständnis und die Anwendung effizienter Algorithmen.

DEUTSCHSPRACHIG:

Hier sind einige deutschsprachige Bücher über Algorithmen und Programmierung:

1. **"Algorithmen und Datenstrukturen"** von Thomas Ottmann und Peter Widmayer.
   - Ein umfassendes Lehrbuch, das sich mit den Grundlagen von Algorithmen und Datenstrukturen beschäftigt.

2. **"Algorithmen - Eine Einführung"** von Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest und Clifford Stein, übersetzt von Paul Molitor.
   - Die deutsche Übersetzung des bekannten "Introduction to Algorithms", das oft als "CLRS" bezeichnet wird.

3. **"Programmieren lernen mit Python"** von Michael Weigend.
   - Dieses Buch bietet eine Einführung in das Programmieren mit Python und behandelt auch grundlegende Algorithmen und Datenstrukturen.

4. **"Der Algorithmen-Knacker: Moderne Algorithmen im Praxis-Check"** von Julian Hein.
   - Dieses Buch bietet eine praxisnahe Einführung in moderne Algorithmen und deren Anwendung.

"""