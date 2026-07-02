function getCSRFToken() {
    const tokenElement = document.querySelector('[name=csrfmiddlewaretoken]');
    return tokenElement ? tokenElement.value : '';
}

const fetchHeaders = {
    'Content-Type': 'application/json',
    'X-CSRFToken': getCSRFToken()
};

async function startDictation(btn) {
    const originalHtml = btn.innerHTML;
    btn.innerHTML = '<i class="material-icons left">hourglass_empty</i>Слушаю...';
    btn.classList.add('disabled');

    try {
        const response = await fetch('/api/recognize/', {
            method: 'POST',
            headers: fetchHeaders
        });
        const data = await response.json();

        if (data.text) {
            const sourceTextArea = document.getElementById('sourceText');
            sourceTextArea.value = data.text;
            M.textareaAutoResize(sourceTextArea);
            showToast('Речь распознана', 'green');
        } else {
            showToast(data.error || "Ошибка распознавания", 'red');
        }
    } catch (e) {
        showToast("Сбой сети при обращении к серверу", 'red');
    } finally {
        btn.innerHTML = originalHtml;
        btn.classList.remove('disabled');
    }
}

async function translateText() {
    const text = document.getElementById('sourceText').value;
    const targetLang = document.getElementById('targetLang').value;

    if (!text.trim()) {
        showToast('Введите текст для перевода', 'orange');
        return;
    }

    try {
        const response = await fetch('/api/translate/', {
            method: 'POST',
            headers: fetchHeaders,
            body: JSON.stringify({ text: text, target_lang: targetLang })
        });

        const data = await response.json();
        if (data.translated_text) {
            const translatedTextArea = document.getElementById('translatedText');
            translatedTextArea.value = data.translated_text;
            M.textareaAutoResize(translatedTextArea);
        } else {
            showToast(data.error || "Ошибка перевода", 'red');
        }
    } catch (e) {
        showToast("Ошибка при подключении к серверу", 'red');
    }
}

async function speakText(elementId, defaultLang) {
    let text = document.getElementById(elementId).value;
    let lang = defaultLang;

    if (elementId === 'translatedText') {
        const target = document.getElementById('targetLang').value;
        lang = target === 'en' ? 'en-US' : target === 'fr' ? 'fr-FR' : 'de-DE';
    }

    if (!text.trim()) {
        showToast("Нет текста для озвучки", 'orange');
        return;
    }

    try {
        const response = await fetch('/api/synthesize/', {
            method: 'POST',
            headers: fetchHeaders,
            body: JSON.stringify({ text: text, lang: lang })
        });
        const data = await response.json();

        if (data.error) {
            showToast(data.error, 'red');
        }
    } catch (e) {
        showToast("Ошибка запроса на озвучку", 'red');
    }
}
