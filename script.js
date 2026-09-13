function send() {

    let text = document.getElementById("code_eingabe").value;
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
            document.getElementById("code_eingabe").style.height = "59vh";
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
    document.getElementById("code_eingabe").style.height = "59vh";
}

function closeTerminal() {
    const terminal_div = document.getElementById("terminal_div");
    const terminal = document.getElementById("terminal");
    terminal_div.hidden = true;
    terminal.style.height = "0";
    document.getElementById("code_eingabe").style.height = "89vh";
}

function clearTerminal() {
    const terminal = document.getElementById("terminal");
    terminal.value = "";
}