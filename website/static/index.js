function deleteNote(noteID) {
    console.log("cliiiiiick");
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteID: noteID }),
    }).then((_res) => {
        window.location.href = "/";
    });
}
