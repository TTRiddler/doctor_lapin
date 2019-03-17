from django import forms


class ReviewForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField(required=True, widget=forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'Ваша электронная почта'}))
        self.fields['name'] = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}))
        self.fields['image'] = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'custom-file-input', 'lang': 'ru'}))
        self.fields['text'] = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Текст отзыва'}))