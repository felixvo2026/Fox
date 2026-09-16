def calculate_mul_div( tokens):
        expression = []
        i = 0

        while i < len(tokens):

            if tokens[i] == "*":
                result = expression.pop() * tokens[i + 1]
                expression.append(result)
                i += 2

            elif tokens[i] == "/":
                result = expression.pop() / tokens[i + 1]
                expression.append(result)
                i += 2

            else:
                expression.append(tokens[i])
                i += 1

        return expression

def calculate_add_sub( tokens):
    result = tokens[0]

    i = 1

    while i < len(tokens):

        if tokens[i] == "+":
            result += tokens[i + 1]

        elif tokens[i] == "-":
            result -= tokens[i + 1]

        i += 2

    return [result]

def compare( tokens):
    operatoren = {"==", "!=", "<", ">", "<=", ">="}

    for i, token in enumerate(tokens):
        if token in operatoren:

            links = calculate(tokens[:i])
            rechts = calculate(tokens[i + 1:])

            if token == "==":
                return links == rechts

            elif token == "!=":
                return links != rechts

            elif token == "<":
                return links < rechts

            elif token == ">":
                return links > rechts

            elif token == "<=":
                return links <= rechts

            elif token == ">=":
                return links >= rechts

    return tokens





def calculate(tokens):
    tokens = calculate_mul_div(tokens)
    tokens = calculate_add_sub(tokens)
    return tokens[0]
