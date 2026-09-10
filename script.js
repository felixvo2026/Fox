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
    });
}
