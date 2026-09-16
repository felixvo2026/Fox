class Ausgabe:
    def __init__(self):
        self.ausgabe = []

    def add(self, item):
        self.ausgabe.append(item)
    
    def get(self):
        """Gibt alle Ausgaben als Liste zurück"""
        return self.ausgabe
    
    def get_string(self):
        """Gibt alle Ausgaben als String zurück"""
        return "\n".join(str(item) for item in self.ausgabe)
    
    def clear(self):
        """Leert die Ausgabenliste"""
        self.ausgabe = []