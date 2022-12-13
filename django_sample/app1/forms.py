from django import forms
from .models import TestData


class TestDataModelForm(forms.ModelForm):

    class Meta:
        model = TestData
        fields = ("number", "name", "price")


# class TestDataForm(forms.Form):
#     # https://www.javadrive.jp/regex-basic/sample/index11.html
#     # https://www.javadrive.jp/regex-basic/sample/index5.html
#     # https://prorautatie.net/tell/

#     campany_mame = forms.CharField(
#         label="貴社名(必須)",
#         max_length=128,
#         required=True,
#         error_messages={'required': '会社名が入力されていません'},
#         widget=forms.TextInput(attrs={'placeholder': '株式会社ネオセルコ'}),
#         help_text="例: 株式会社ネオセルコ",
#     )
