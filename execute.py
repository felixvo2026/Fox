from calculate import *
from variables import *
from tokenizer import tokenize
from ausgabe import Ausgabe

ausgabe = Ausgabe()

class Execute:
    def __init__(self):
        self.commands = {
            "schreibe": self.schreibe,
        }
        self.last_if_result = None
        self.waiting_for_else = False
        


    def execute(self, tokens, inside_block=False):
        if self.is_variable(tokens):
                self.create_variable(tokens)

        elif self.is_command(tokens):
            self.execute_command(tokens)

        elif self.is_if(tokens):
            self.execute_if(tokens)

        elif self.is_else(tokens):
            self.execute_else(tokens)

        else:
            pass


    def is_if(self, tokens):
        return len(tokens) > 0 and tokens[0] == "wenn"

    def execute_if(self, tokens):

        
        condition = tokens[1:-1]
        block = tokens[-1]
        self.last_if_result = self.eval_expressions(condition)

        self.waiting_for_else = True

        if self.last_if_result:
            for statement in block:
                self.execute(statement, inside_block=True)
        


    def is_else(self, tokens):
        return len(tokens) > 0 and tokens[0] == "sonst"

    def execute_else(self, tokens):
        # print(self.waiting_for_else)
        if not self.waiting_for_else:
            ausgabe.add("Fehler: 'sonst' ohne vorheriges 'wenn'")
            return

        if self.last_if_result:
            self.waiting_for_else = False
            self.last_if_result = None
            return

        block = tokens[-1]

        for statement in block:
            self.execute(statement, inside_block=True)

        self.waiting_for_else = False
        self.last_if_result = None

    def is_command(self, tokens):
        return len(tokens) > 0 and tokens[0] in self.commands

    def execute_command(self, tokens):
        command = self.commands[tokens[0]]

        # Kein Argument
        if len(tokens) == 1:
            command()
            return

        # Klammern entfernen
        if tokens[1] == "(" and tokens[-1] == ")":
            argument_tokens = tokens[2:-1]
        else:
            argument_tokens = tokens[1:]

        # Nur ein einzelnes Argument?
        if len(argument_tokens) == 1:
            arg = self.parse_value(argument_tokens[0])

            # Variable?
            if isinstance(arg, str):
                # String-Literal
                if argument_tokens[0].startswith('"') and argument_tokens[0].endswith('"'):
                    pass

                # Variable vorhanden
                elif arg in variablen:
                    arg = variablen[arg].value

                else:
                    ausgabe.add("Fehler: Unbekannte Variable")
                    return

        # Ausdruck (z.B. 1+2 oder a*5)
        else:
            arg = self.eval_expressions(argument_tokens)

            if arg == "Fehler":
                ausgabe.add("Fehler in der Berechnung des Arguments")
                return
        command(arg)


    def parse_value(self, value):

        if not isinstance(value, str):
            return value

        if value.startswith('"') and value.endswith('"'):
            return value[1:-1]

        try:
            return int(value)
        except ValueError:
            pass

        try:
            return float(value)
        except ValueError:
            pass

        return value

    def is_variable(self, tokens):
            return len(tokens) >= 3 and tokens[1] == "="

    def create_variable(self, tokens):
        var_name = tokens[0]

        var_value = self.eval_expressions(tokens[2:])

        if var_value == "Fehler":
            ausgabe.add("Fehler in der Berechnung des Wertes")
            return

        if var_name in variablen:
            try:
                variablen[var_name].value = var_value
            except TypeError as ex:
                ausgabe.add(str(ex))
                return
        else:
            variablen[var_name] = Variable(var_value)
            #print(f"Variable {var_name} erstellt mit Wert {var_value} und Typ {type(var_value).__name__}")

    def eval_expressions(self, tokens):
        expression = []

        # Variablen ersetzen und Werte parsen
        for token in tokens:
            if token in variablen:
                expression.append(variablen[token].value)
                #print(f"Variable {token} ersetzt durch Wert {variablen[token].value}")
            else:
                expression.append(self.parse_value(token))

        # Klammern auswerten
        while "(" in expression:
            start = None
            ende = None

            for i, token in enumerate(expression):
                if token == "(":
                    start = i
                elif token == ")" and start is not None:
                    ende = i
                    break

            if start is None or ende is None:
                ausgabe.add("Fehler: Ungültige Klammern")
                return "Fehler"

            wert = self.eval_expressions(expression[start + 1:ende])

            expression = (
                expression[:start]
                + [wert]
                + expression[ende + 1:]
            )

        vergleichs_operatoren = {"==", "!=", "<", ">", "<=", ">="}

        if any(token in vergleichs_operatoren for token in expression):

            return compare(expression)

        expression = calculate_mul_div(expression)
        expression = calculate_add_sub(expression)

        return expression[0]

    def schreibe(self, text):
        if isinstance(text, (str, bool)):
            ausgabe.add(text)
        else:
            text = tokenize(str(text))
            text = self.eval_expressions(text)
            ausgabe.add(text)
