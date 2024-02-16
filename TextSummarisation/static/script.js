function clearTextAreas() {
    document.getElementById("inputText").value = ""; // Clear inputText textarea
    document.getElementById("summary").value = ""; // Clear summary textarea
}



function summarizeText() {
    var inputText = document.getElementById('inputText').value.trim();
    var numSentences = document.getElementById('numSentences').value;

    if (!inputText) {
        alert('Please enter some text to summarize.');
        return;
    }

    // Make an AJAX request to Flask server
    fetch('/summarize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: inputText, numSentences: numSentences })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('summary').value = data.summary;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

