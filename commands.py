#from main import ausgabe

def schreibe(text):
    if type(text) in uenterstuetzte_datentypen or text is None:
        raise ValueError(text)
    else:
        raise ValueError("Fehler: Rechenausdruck konnte nicht ausgewertet werden")

commands = {
    "schreibe": schreibe,
}

uenterstuetzte_datentypen = [ str, bool]

