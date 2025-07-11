// File Upload and Drag & Drop
const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const uploadBtn = document.getElementById('uploadBtn');
const processBtn = document.getElementById('processBtn');
const extractedContent = document.getElementById('extractedContent');
const extractedContainer = document.getElementById('extracted-container');

uploadBtn.addEventListener('click', () => fileInput.click());

fileInput.addEventListener('change', (e) => {
    if (e.target.files.length) {
        handleFile(e.target.files[0]);
    }
});

['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropZone.addEventListener(eventName, preventDefaults, false);
});

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

['dragenter', 'dragover'].forEach(eventName => {
    dropZone.addEventListener(eventName, highlight, false);
});

['dragleave', 'drop'].forEach(eventName => {
    dropZone.addEventListener(eventName, unhighlight, false);
});

function highlight() {
    dropZone.classList.add('drag-active');
}

function unhighlight() {
    dropZone.classList.remove('drag-active');
}

dropZone.addEventListener('drop', (e) => {
    const dt = e.dataTransfer;
    const file = dt.files[0];
    handleFile(file);
});

async function handleFile(file) {
    if (file.type !== 'application/pdf') {
        alert('Please upload a PDF file');
        return;
    }
    if (file.size > 10 * 1024 * 1024) {
        alert('File is too large. Maximum size is 10MB');
        return;
    }

    processBtn.disabled = false;

    const formData = new FormData();
    formData.append('pdf_file', file);

    try {
        const res = await fetch('/api/extract', {
            method: 'POST',
            body: formData
        });
        const data = await res.json();
        const markdown = data.text || ''; // đây là nội dung CV
        const htmlContent = marked.parse(markdown);

        extractedContent.innerHTML = `
            <div class="flex items-start gap-4 mb-4">
                <i class="fas fa-file-pdf text-red-500 mt-1"></i>
                <div>
                    <h4 class="font-medium">${file.name}</h4>
                    <p class="text-xs text-gray-500">${(file.size / (1024 * 1024)).toFixed(2)} MB</p>
                </div>
            </div>
            <div class="prose prose-sm leading-loose max-w-none overflow-y-auto max-h-[300px] p-2 border border-gray-100 bg-white rounded">
                ${htmlContent}
            </div>
        `;

        setTimeout(() => {
            document.querySelectorAll('#extractedContent pre code').forEach((el) => {
                hljs.highlightElement(el);
            });
        }, 0);

    } catch (err) {
        extractedContent.innerHTML = `<p class="text-red-500">Error extracting PDF content.</p>`;
    }
}


// Process Button Handler
processBtn.addEventListener('click', async () => {
    const formData = new FormData();
    if (!textSection.classList.contains('hidden')) {
        formData.append('cv_text', cvTextInput.value);
    } else {
        formData.append('pdf_file', fileInput.files[0]);
    }
    formData.append('jd_text', jdTextInput.value);

    const lang = document.querySelector('select').value;
    const length = document.querySelector('input[name="summaryLength"]:checked').nextElementSibling.innerText;

    formData.append('language', lang);
    formData.append('summary_length', length);

    const aiSummary = document.getElementById('aiSummary');
    aiSummary.innerHTML = `<div class="text-center py-8"><i class="fas fa-spinner fa-spin text-4xl mb-3 text-indigo-500"></i><p class="text-gray-600">Generating your summary...</p></div>`;

    try {
        const res = await fetch('/api/summarize', {
            method: 'POST',
            body: formData
        });
        const data = await res.json();
        const markdown = data.summary;
        const htmlContent = marked.parse(markdown);
        aiSummary.innerHTML = `<div class="prose prose-sm max-w-none">${htmlContent}</div>`;

        setTimeout(() => {
            document.querySelectorAll('#aiSummary pre code').forEach((el) => {
                hljs.highlightElement(el);
            });
        }, 0);

        document.getElementById('matchAnalysis').innerHTML = `<div class="prose max-w-none">${data.match_analysis}</div>`;
    } catch (err) {
        aiSummary.innerHTML = `<p class="text-red-500">Something went wrong.</p>`;
    }
});

// Tab switching between PDF and Text input
const tabPdf = document.getElementById('tabPdf');
const tabText = document.getElementById('tabText');
const pdfSection = document.getElementById('pdfSection');
const textSection = document.getElementById('textSection');
const cvTextInput = document.getElementById('cvTextInput');

tabPdf.addEventListener('click', () => {
    pdfSection.classList.remove('hidden');
    extractedContainer.classList.remove('hidden')
    textSection.classList.add('hidden');
    tabPdf.classList.add('border-indigo-500', 'text-indigo-500', 'bg-indigo-50');
    tabPdf.classList.remove('border-gray-300', 'text-gray-500');
    tabText.classList.add('border-gray-300', 'text-gray-500');
    tabText.classList.remove('border-indigo-500', 'text-indigo-500', 'bg-indigo-50');
});

tabText.addEventListener('click', () => {
    pdfSection.classList.add('hidden');
    extractedContainer.classList.add('hidden')
    textSection.classList.remove('hidden');
    tabText.classList.add('border-indigo-500', 'text-indigo-500', 'bg-indigo-50');
    tabText.classList.remove('border-gray-300', 'text-gray-500');
    tabPdf.classList.add('border-gray-300', 'text-gray-500');
    tabPdf.classList.remove('border-indigo-500', 'text-indigo-500', 'bg-indigo-50');
});

// JD text input handler
const jdTextInput = document.getElementById('jdTextInput');
const jdContent = document.getElementById('jdContent');

jdTextInput.addEventListener('input', () => {
    if (jdTextInput.value.trim()) {
        jdContent.innerHTML = `
                    <div class="prose max-w-none">
                        <pre class="whitespace-pre-wrap">${jdTextInput.value}</pre>
                    </div>
                `;
    } else {
        jdContent.innerHTML = `
                    <div class="text-center py-12 text-gray-400">
                        <i class="fas fa-align-left text-4xl mb-3"></i>
                        <p>Enter job description on the left to see it here</p>
                    </div>
                `;
    }
});
function checkEnableButton() {
    const hasTextCV = !textSection.classList.contains('hidden') && cvTextInput.value.trim().length > 0;
    const hasPDF = !pdfSection.classList.contains('hidden') && fileInput.files.length > 0;
    processBtn.disabled = !(hasTextCV || hasPDF);
}

cvTextInput.addEventListener('input', checkEnableButton);
fileInput.addEventListener('change', checkEnableButton);

setTimeout(() => {
    document.querySelectorAll('#aiSummary pre code').forEach((el) => {
        hljs.highlightElement(el);
    });
}, 0);
