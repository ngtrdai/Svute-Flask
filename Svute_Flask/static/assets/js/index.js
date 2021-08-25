function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({
            noteId: noteId
        })
    }).then((_res) => {
        window.location.href = "/"
    });
}

function copyToClip(e, t="") {
    function n(t) {
        t.clipboardData.setData("text/html", e),
        t.clipboardData.setData("text/plain", e),
        t.preventDefault()
    }
    document.addEventListener("copy", n),
    document.execCommand("copy"),
    document.removeEventListener("copy", n),
    t.length > 0 && $("#" + t).html(txt_copied)
}

function printDiv(e) {
    var t = document.getElementById(e).innerHTML
      , n = document.body.innerHTML;
    document.body.innerHTML = t,
    window.print(),
    document.body.innerHTML = n
}