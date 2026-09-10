# 🦊 Fox

Eine deutsche Programmiersprache für den Browser.

## 📖 Übersicht

Fox ist ein innovatives Projekt, das es ermöglicht, Code in einer deutschen Programmiersprache direkt im Browser auszuführen. Das Projekt kombiniert einen Tokenizer, Parser und Interpreter, um eine benutzerfreundliche Programmierumgebung zu schaffen.

## ✨ Funktionen

- **Deutsche Syntax**: Schreibe Code in deutscher Sprache
- **Browser-basiert**: Nutze die Anwendung direkt im Web-Browser
- **Tokenizer**: Intelligente Zerlegung von Quellcode in Token
- **Parser & Executor**: Robuste Verarbeitung und Ausführung von Programmen
- **REST API**: FastAPI-basierte Schnittstelle für Code-Verarbeitung

## 🏗️ Projektstruktur

```
Fox/
├── main.py          # Hauptklasse für Code-Verarbeitung und Parsing
├── api.py           # FastAPI REST-API Server
├── tokenizer.py     # Token-Generierung aus Quellcode
├── execute.py       # Code-Ausführungs-Engine
├── calculate.py     # Mathematische Operationen
├── variables.py     # Variablen-Management
├── commands.py      # Befehlsdefinitionen
├── index.htm        # HTML Frontend
├── script.js        # JavaScript Frontend-Logik
├── style.css        # Frontend-Styling
└── .gitignore       # Git-Ignorare-Datei
```

## 🚀 Erste Schritte

### Voraussetzungen

- Python 3.8+
- pip (Python-Paketmanager)

### Installation

1. Repository klonen:
```bash
git clone https://github.com/felixvo2026/Fox.git
cd Fox
```

2. Abhängigkeiten installieren:
```bash
pip install fastapi uvicorn
```

### Verwendung

**API-Server starten:**
```bash
python api.py
```
Der Server läuft dann unter `http://127.0.0.1:8000`

**Frontend öffnen:**
Öffne `index.htm` in deinem Browser

## 🔌 API-Endpunkte

### POST /verarbeitung
Verarbeitet Fox-Code und gibt das Ergebnis zurück.

**Request:**
```json
{
    "nachricht": "dein_code_hier"
}
```

**Response:**
```json
{
    "nachricht": ["Ausgabe1", "Ausgabe2"]
}
```

## 💻 Technologie-Stack

- **Backend**: Python mit FastAPI
- **Frontend**: HTML5, CSS3, JavaScript
- **Kommunikation**: REST API mit CORS-Support

## 📝 Lizenz

Dieses Projekt ist lizenziert unter der MIT-Lizenz.

## 👨‍💻 Autor

Erstellt von [@felixvo2026](https://github.com/felixvo2026)

## 🤝 Beitragen

Beiträge sind willkommen! Bitte erstelle einen Pull Request oder ein Issue für Verbesserungsvorschläge.

## 📞 Support

Hast du Fragen oder Probleme? Öffne ein [Issue](https://github.com/felixvo2026/Fox/issues) auf GitHub.
