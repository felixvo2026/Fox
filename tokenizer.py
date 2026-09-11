def tokenize(code):
    tokens = []
    klammern = []
    current_token = ""
    in_string = False
    string_delimiter = ""

    oeffnende_klammern = "([{"
    schliessende_klammern = ")]}"
    klammerpaare = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    sonderzeichen = ".,:+-*/=%<>!;"

    i = 0

    while i < len(code):
        char = code[i]

        # Strings
        if char in ('"', "'"):
            if in_string:
                current_token += char
                if char == string_delimiter:
                    tokens.append(current_token)
                    current_token = ""
                    in_string = False
            else:
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
                in_string = True
                string_delimiter = char
                current_token += char

            i += 1
            continue

        if in_string:
            current_token += char
            i += 1
            continue

        # Leerzeichen
        if char.isspace():
            if current_token:
                tokens.append(current_token)
                current_token = ""
            i += 1
            continue

        # Öffnende Klammern
        if char in oeffnende_klammern:
            if current_token:
                tokens.append(current_token)
                current_token = ""
            klammern.append(char)
            tokens.append(char)
            i += 1
            continue

        # Schließende Klammern
        if char in schliessende_klammern:
            if current_token:
                tokens.append(current_token)
                current_token = ""

            if not klammern or klammern[-1] != klammerpaare[char]:
                raise ValueError(f"Ungültige schließende Klammer: {char}")

            klammern.pop()
            tokens.append(char)
            i += 1
            continue

        # Zweistellige Operatoren
        if char in "=<>!":
            if current_token:
                tokens.append(current_token)
                current_token = ""

            if i + 1 < len(code) and code[i + 1] == "=":
                tokens.append(char + "=")
                i += 2
            else:
                tokens.append(char)
                i += 1

            continue

        # Einfache Sonderzeichen
        if char in ".,:+-*/%;":
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
            i += 1
            continue

        # Normale Zeichen
        current_token += char
        i += 1

    if current_token:
        tokens.append(current_token)

    if klammern:
        raise ValueError(f"Offene Klammer bleibt übrig: {''.join(klammern)}")
        

    return tokens
