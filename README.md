# Seriennummergenerator
Das folgende Programm erstellt Seriennummern und sichert diese in eine .json Datei.\


### Anleitung
Das Programm lässt sich über eine Kommandozeile (PowerShell o. bsh/zsh) ausführen.  
Benötigt wird hierbei ein Python Interpreter. Zum Ausführen Python in die Kommandozeile (Python3 für macOS) eingeben und die unten spezifizierten Parameter eingeben.

### Parameter
-h oder --help um alle verfügbaren befehle anzeigen zu lassen.\
-dg oder --digitalgenerator mit der Anzahl als Wert für nummerbasierte Schlüssel.\
-lg oder --lettergenerator mit der Anzahl als nummerischer Wert für buchstabenbasierte Schlüssel.\
-v oder --validate um erstellte Schlüssel zu validieren.

### Optionale Parameter
-kr oder --keyrows um die Anzahl der erstellen Blöcke zu manipulieren. (Standardmäßg auf 4)\
-rl oder --rowlength für die Anzahl der Charaktere, die für jede Reihe erzeugt werden.\
-p oder --path um den Speicherort zu ändern.\
-fn oder --filename um den Namen der Datei zu bearbeiten.
