from calculate import *
from variables import variablen
from commands import commands
from variables import Variable


def execute(tokens):
    if is_variable(tokens):
            create_variable(tokens)

    elif is_command(tokens):
        execute_command(tokens)

    elif is_if(tokens):
        execute_if(tokens)

    else:
        pass


def is_if( tokens):
    return len(tokens) > 0 and tokens[0] == "wenn"

def execute_if( tokens):
    condition = tokens[1:-1]
    block = tokens[-1]

    result = eval_expressions(condition)

    if result:
        for statement in block:
            execute(statement)

def is_command( tokens):
    return len(tokens) > 0 and tokens[0] in commands

def execute_command( tokens):
    command = commands[tokens[0]]

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
        arg = parse_value(argument_tokens[0])

        # Variable?
        if isinstance(arg, str):
            # String-Literal
            if argument_tokens[0].startswith('"') and argument_tokens[0].endswith('"'):
                pass

            # Variable vorhanden
            elif arg in variablen:
                arg = variablen[arg].value

            else:
                raise ValueError("Fehler: Unbekannte Variable")
                return

    # Ausdruck (z.B. 1+2 oder a*5)
    else:
        arg = eval_expressions(argument_tokens)

        if arg == "Fehler":
            raise ValueError("Fehler in der Berechnung des Arguments")
            return
    command(arg)

def parse_value(value):

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

def is_variable(tokens):
        return len(tokens) >= 3 and tokens[1] == "="

def create_variable( tokens):
    var_name = tokens[0]

    var_value = eval_expressions(tokens[2:])

    if var_value == "Fehler":
        raise ValueError("Fehler in der Berechnung des Wertes")
        return

    if var_name in variablen:
        try:
            variablen[var_name].value = var_value
        except TypeError as ex:
            raise ValueError(str(ex))
            return
    else:
        variablen[var_name] = Variable(var_value)

def eval_expressions(tokens):
    expression = []

    # Variablen ersetzen und Werte parsen
    for token in tokens:
        if token in variablen:
            expression.append(variablen[token].value)
        else:
            expression.append(parse_value(token))

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
            raise ValueError("Fehler: Ungültige Klammern")
            

        wert = eval_expressions(expression[start + 1:ende])

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
