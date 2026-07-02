document.addEventListener('DOMContentLoaded', function () {
    var selects = document.querySelectorAll('select');
    if (typeof M !== 'undefined') {
        M.FormSelect.init(selects);

        const sourceText = document.getElementById('sourceText');
        const translatedText = document.getElementById('translatedText');

        if (sourceText) M.textareaAutoResize(sourceText);
        if (translatedText) M.textareaAutoResize(translatedText);
    }
});


function showToast(message, colorClass) {
    if (typeof M !== 'undefined') {
        M.toast({ html: message, classes: colorClass });
    } else {
        alert(message);
    }
}