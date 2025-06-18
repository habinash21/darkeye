function setKeywords() {
    const keywords = document.getElementById('keywords').value.split(',');
    fetch('http://127.0.0.1:5000/set_keywords', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ keywords }),
    })
    

        .then((response) => response.json())
        .then((data) => {
            alert(data.message);
        });
}

function monitorDarkWeb() {
    fetch('http://127.0.0.1:5000/monitor')
        .then((response) => response.json())
        .then((data) => {
            const alertsDiv = document.getElementById('alerts');
            alertsDiv.innerHTML = '';
            data.alerts.forEach((alert) => {
                const alertElem = document.createElement('p');
                alertElem.textContent = `Keyword: ${alert.keyword}, Content: ${alert.content}`;
                alertsDiv.appendChild(alertElem);
            });
        });
}