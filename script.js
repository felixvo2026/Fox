class ProjectStorage {
    constructor() {
        this.isLoggedIn = false; // Wird nach dem Login auf true gesetzt
    }

    async saveProject(projectId, code) {
        if (this.isLoggedIn) {
            // 1. In der Cloud speichern (z.B. per API)
            //await fetch(`/api/projects/${projectId}`, { method: 'POST', body: JSON.stringify({ code }) });
            return
        } else {
            // 2. Lokal im Browser speichern
            localStorage.setItem(`project_${projectId}`, code);
        }
    }
}

storage = new ProjectStorage();

function send() {

    let text = document.getElementById("editor").value;
    fetch("http://127.0.0.1:8000/verarbeitung", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            nachricht: text
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        console.log("Verarbeitung erfolgreich abgeschlossen.");

        const liste = data.nachricht;
        
        const terminal = document.getElementById("terminal");
        const terminal_div = document.getElementById("terminal_div");
        if (terminal_div.hidden = true) {
            terminal_div.hidden = false;
            terminal.style.height = "30vh";
            document.getElementById("").style.height = "59vh";
        }
        if (terminal.value.length == 0) {
            terminal.value = liste.join("\n");
        } else {
            terminal.value += "\n" + liste.join("\n");
        }
    });
}

function openTerminal() {
    const terminal_div = document.getElementById("terminal_div");
    const terminal = document.getElementById("terminal");
    terminal_div.hidden = false;
    terminal.style.height = "30vh";
    document.getElementById("editor").style.height = "59vh";
}

function closeTerminal() {
    const terminal_div = document.getElementById("terminal_div");
    const terminal = document.getElementById("terminal");
    terminal_div.hidden = true;
    terminal.style.height = "0";
    document.getElementById("editor").style.height = "89vh";
}

function clearTerminal() {
    const terminal = document.getElementById("terminal");
    terminal.value = "";
}

// Den Code-Editor aus dem HTML holen (z. B. eine Textarea)
const codeEditor = document.getElementById('editor');

// 1. Beim Laden der Seite: Gespeicherten Code auslesen
window.addEventListener('DOMContentLoaded', () => {
    const savedCode = localStorage.getItem('user_project_code');
    if (savedCode) {
        codeEditor.value = savedCode; // Code wiederherstellen
    }
});

// 2. Beim Tippen: Code sofort automatisch speichern (Debouncing empfohlen für Performance)
codeEditor.addEventListener('input', (event) => {
    const currentCode = event.target.value;
    localStorage.setItem('user_project_code', currentCode);
});



function KontoErstellen (event) {
    
    event.preventDefault();
    const Username = document.getElementById("Username");
    const Password = document.getElementById("Password");
    // if (localStorage.getItem(Username) === Username) {
    //     const Info = document.getElementById("info-register");
    //     Info.value = "Benutzername bereits verwendet";
    //     Info.hidden = false;
    //     return
    // }
    
    // localStorage.setItem(Username, Password);
    storage.isLoggedIn = true;
    window.location.href = '../index.htm';
    console.log("Ausgeführt");
}

function Einloggen(event) {
    event.preventDefault();
    const Username = document.getElementById("Username");
    const Password = document.getElementById("Password");
    storage.isLoggedIn = true;
    window.location.href = '../index.htm';
}
