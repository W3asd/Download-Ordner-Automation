# Libaries die benötigt werden
from os import listdir
from os.path import isfile, join
import os
import shutil

# Funktion welche die Extension aus von einer Datei filtert
def getExtension(file):
    extension = os.path.splitext(file)[1]
    extension = extension.lstrip(".")
    return extension

# Ordner der sotiert werden soll
file_path = "D:/Downloads"

# Datein welche im Ordner sind
"""
List Comprehension
Die soll den Array von der listdir() Funktion mit hilfe der isfile() Funktion nach Datein filtern
"""
files = [ f for f in listdir(file_path) if isfile(join(file_path, f)) ]


# Deklarierung von einem leeren Array & Dict
"""
Array soll für die unterschiedlichen Extension sein
Dict soll die Extension beinhalten und diese an dessen Verzeichnisse mappen
"""
extension_list = []
extension_dict = {}

# Loop um die Verzeichnisse der spez Extension zu erstellen
for file in files:

    extension = getExtension(file)                                      # Nutze definierte Funktion getExtension() um die Extension der Datei zu erhalten

    if extension not in extension_list:

        extension_list.append(extension)                                # sollte die Extension nicht in der Liste sein, soll die in die extension_list hinzugefügt werden 


        new_folder_name = file_path + "/" + extension + "_folder"       # Name des neuen Verzeichnisses wird generiert


        extension_dict[str(extension)] = str(new_folder_name)           # Extension und dessen neuer Pfad wird ins dict hinzugefügt


        if os.path.isdir(new_folder_name) == True:                      # Exestiert das Verzeichnis schon im Download Ordner?

            continue

        else:
            os.mkdir(new_folder_name)                                   # neues Verzeichnis wird erstellt 

# Schleife um die Datein in passende Verzeichnis zu bewegen
for file in files:
        
    src_path = file_path + "/" + file                                   # Erzeugung des Source Path 

    extension = getExtension(file)

    if extension in extension_dict.keys():                              # Im Dict wird nachgeschaut wohin die Datei bewegt werden soll
        
        dest_path = extension_dict[str(extension)]                      # Erzeugung des Destination Path

        shutil.move(src_path, dest_path)                                # Datei wird ins passende Verzeichnis bewegt