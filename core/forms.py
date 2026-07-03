from django import forms

class TranslationForm(forms.Form):
    LANG_CHOICES = [
        ('en-US', 'Английский'),
        ('uk-UA', 'Украинский'),
        ('ru-RU', 'Русский'),
        ('fr-FR', 'Французский'),
        ('de-DE', 'Немецкий'),
    ]
    
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
        initial='en'
    )