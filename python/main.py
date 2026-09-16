from python.tokenizer import *


class Main:
    def __init__(self):
        #self.variables = variablen
        #self.eingabe = None
        self.ausgabe_main = []
        #self.commands = commands

    def main(self, text):
        from python.execute import Execute
        try:
            execute = Execute()
            tokens = tokenize(text)

            if tokens == "Fehler":
                return

            statements, _ = self.split_code(tokens)

            for statement in statements:
                if len(statement) == 0:
                    continue
                #print(statement)
                #print(self.commands)
                try:
                    
                    execute.execute(statement)
                except Exception as e:
                    self.ausgabe_main.append(str(e))

        except Exception as e:
            self.ausgabe_main.append(str(e))
            

    def split_code(self, tokens, pos=0):
        statements = []
        statement = []

        while pos < len(tokens):
            token = tokens[pos]

            # Ende des aktuellen Blocks
            if token == "}":
                if statement:
                    statements.append(statement)
                return statements, pos

            # Neuer Block beginnt
            elif token == "{":
                block, pos = self.split_code(tokens, pos + 1)
                statement.append(block)

                # Das aktuelle Statement (z.B. wenn) ist jetzt komplett
                statements.append(statement)
                statement = []

            # Statement beendet
            elif token == ";":
                if statement:
                    statements.append(statement)
                    statement = []

            # Normales Token
            else:
                statement.append(token)

            pos += 1

        # Falls am Dateiende noch ein Statement übrig ist
        if statement:
            statements.append(statement)

        return statements, pos

    def verarbeitung(self, text):
        from python.execute import ausgabe
        
        self.ausgabe_main = []  # ✅ self.ausgabe_main ZUERST leeren
        ausgabe.clear()   # ✅ dann ausgabe leeren
        
        self.main(text)
        
        self.ausgabe_main += ausgabe.get()  # ✅ Jetzt können beide kombiniert werden
        ausgabe.clear()   # ✅ Nach der Ausgabe clearen
        
        return self.ausgabe_main