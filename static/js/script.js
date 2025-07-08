document.addEventListener('DOMContentLoaded', function () {
    const pdfUpload = document.getElementById('pdf-upload');
    const fileNameDisplay = document.getElementById('file-name');
    const summarizeBtn = document.getElementById('summarize-btn');
    const resultsSection = document.getElementById('results-section');
    const extractedText = document.getElementById('extracted-text');
    const aiSummary = document.getElementById('ai-summary');
    const loadingSpinner = document.getElementById('loading-spinner');
    const copySummaryBtn = document.getElementById('copy-summary');

    // File selected
    pdfUpload.addEventListener('change', function (e) {
        if (e.target.files.length > 0) {
            const fileName = e.target.files[0].name;
            fileNameDisplay.textContent = `Selected: ${fileName}`;
            fileNameDisplay.classList.remove('hidden');
            summarizeBtn.disabled = false;
        } else {
            fileNameDisplay.classList.add('hidden');
            summarizeBtn.disabled = true;
        }
    });

    // Summarize button clicked
    summarizeBtn.addEventListener('click', function () {
        summarizeBtn.disabled = true;
        loadingSpinner.classList.remove('hidden');

        const file = pdfUpload.files[0];
        const language = document.getElementById('language').value;
        const limit = document.getElementById('word-limit').value;
        const apiKey = document.getElementById('api-key').value;

        const formData = new FormData();
        formData.append('file', file);
        formData.append('language', language);
        formData.append('limit', limit);
        formData.append('api_key', apiKey);

        fetch('/summarize', {
            method: 'POST',
            body: formData
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                extractedText.innerHTML = `<pre>${data.text}</pre>`;
                aiSummary.innerHTML = marked.parse(data.summary);
                resultsSection.classList.remove('hidden');
                resultsSection.scrollIntoView({ behavior: 'smooth' });
            })
            .catch(error => {
                alert(`Failed to summarize: ${error.message}`);
            })
            .finally(() => {
                loadingSpinner.classList.add('hidden');
                summarizeBtn.disabled = false;
            });
    });

    // Copy button
    copySummaryBtn.addEventListener('click', function () {
        const range = document.createRange();
        range.selectNode(aiSummary);
        window.getSelection().removeAllRanges();
        window.getSelection().addRange(range);
        document.execCommand('copy');
        window.getSelection().removeAllRanges();

        const original = copySummaryBtn.innerHTML;
        copySummaryBtn.innerHTML = `
            <svg class="-ml-0.5 mr-2 h-4 w-4 text-green-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
            </svg>
            Copied!
        `;
        setTimeout(() => {
            copySummaryBtn.innerHTML = original;
        }, 2000);
    });

    // Drag & Drop
    const uploadDiv = document.querySelector('.file-upload');
    uploadDiv.addEventListener('dragover', function (e) {
        e.preventDefault();
        uploadDiv.classList.add('border-indigo-500', 'bg-indigo-50');
        uploadDiv.classList.remove('border-gray-300');
    });
    uploadDiv.addEventListener('dragleave', function () {
        uploadDiv.classList.remove('border-indigo-500', 'bg-indigo-50');
        uploadDiv.classList.add('border-gray-300');
    });
    uploadDiv.addEventListener('drop', function (e) {
        e.preventDefault();
        uploadDiv.classList.remove('border-indigo-500', 'bg-indigo-50');
        uploadDiv.classList.add('border-gray-300');
        if (e.dataTransfer.files.length) {
            pdfUpload.files = e.dataTransfer.files;
            const event = new Event('change');
            pdfUpload.dispatchEvent(event);
        }
    });
});
