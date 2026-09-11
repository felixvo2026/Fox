from tokenizer import *
from execute import execute



class Main:
    def __init__(self):
        #self.variables = variablen
        #self.eingabe = None
        self.ausgabe = []
        #self.commands = commands

    def main(self, text):
        try:
            tokens = tokenize(text)


            statements, _ = self.split_code(tokens)

            for statement in statements:
                if len(statement) == 0:
                    continue
                #print(statement)
                #print(self.commands)
                try:
                    execute(statement)
                except Exception as e:
                    self.ausgabe.append(str(e))

        except Exception as e:
            self.ausgabe.append(str(e))
            print(f"Fehler: {str(e)}")
            

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
        self.main(text)
        return self.ausgabe
