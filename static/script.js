let chartInstance;  // Declare a global variable to hold the chart instance

document.getElementById('search-btn').addEventListener('click', function () {
    const query = document.getElementById('query').value;

    // Clear previous results
    document.getElementById('document-list').innerHTML = '';

    fetch('/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `query=${query}`
    })
    .then(response => response.json())
    .then(data => {
        const documentList = document.getElementById('document-list');

        // Display the top 5 documents
        data.results.forEach((doc, i) => {
            const docElement = document.createElement('div');
            docElement.classList.add('document');
            docElement.innerHTML = `<h3>Document ${i + 1} (Similarity: ${data.similarities[i].toFixed(4)})</h3><p>${doc}</p>`;
            documentList.appendChild(docElement);
        });

        // Update the bar chart for cosine similarities
        const ctx = document.getElementById('similarity-chart').getContext('2d');

        // If a chart instance already exists, destroy it before creating a new one
        if (chartInstance) {
            chartInstance.destroy();
        }

        // Create a new chart with the updated similarity data
        chartInstance = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Document 1', 'Document 2', 'Document 3', 'Document 4', 'Document 5'],
                datasets: [{
                    label: 'Cosine Similarity',
                    data: data.similarities,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    });
});
