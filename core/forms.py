from django import forms

LANG_CHOICES = [
    ('en-US', 'Английский'),
    ('uk-UA', 'Украинский'),
    ('ru-RU', 'Русский'),
]

class TranslationForm(forms.Form):
    source_lang = forms.ChoiceField(
        choices=LANG_CHOICES,
        widget=forms.Select(attrs={'id': 'sourceLang'}),
        initial='ru-RU'
    )
    
    source_text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'materialize-textarea', 
            'id': 'sourceText',
            'placeholder': "Нажмите 'Слушать' или введите текст..."
        }),
        required=False
    )
    
    target_lang = forms.ChoiceField(
        choices=LANG_CHOICES,
        widget=forms.Select(attrs={'id': 'targetLang'}),
        initial='en-US'
    )