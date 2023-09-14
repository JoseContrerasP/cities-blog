from django import forms

from .models import Comment, Like_comment, City

from django_countries.fields import CountryField


from django_countries import countries

# from django import newforms


class Comment_form(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ("text",)

        widgets = {
            "text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Comment",
                    "style": "max-width: 300px",
                    "id": "formComment",
                }
            )
        }


class Like_comment_form(forms.ModelForm):
    class Meta:
        model = Like_comment

        fields = ("comment",)


class City_form(forms.ModelForm):
    class Meta:
        model = City

        fields = ("name", "country", "description", "population", "image")

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write the name of the city",
                }
            ),
            "contry": CountryField().formfield(),
        }
