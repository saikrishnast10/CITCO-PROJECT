from django import forms
from mainpage.models import candidatemodel

class candidateform(forms.ModelForm):
    class Meta:
        model=candidatemodel
        fields=["Name","Email","Password","Gender","Qualification","Upload_Image","Upload_Resume"]
        widgets={
            "Name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Name"}),
            "Email":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Name","type":"Email"}),
            "Password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Name"}),
            "Gender":forms.Select(attrs={"class":"form-control"}),
            "Qualification":forms.Select(attrs={"class":"form-control"}),
            "Upload_Image":forms.FileInput(attrs={"class":"form-control","accept":"Image/*","title":"Upload_Image"}),
            "Upload_Resume":forms.FileInput(attrs={"class":"form-control","accept":".pdf","title":"Upload_Resume"}),

        }


def clean_upload_Resume(self):
    resume=self.cleaned_data.get("upload_Resume")
    if not resume.Name.endswith('.pdf'):
        raise forms.ValidationError("only pdf files are Allowed")
    return resume