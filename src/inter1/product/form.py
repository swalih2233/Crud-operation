from django import forms

from product.models import  Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =["name","image","description","price"]

        widgets = {
            "name":forms.widgets.TextInput(attrs={"placeholder":"Category Name","class":"form-control"}),
            "image":forms.widgets.FileInput(attrs={"class":"form-control"}),
            "description":forms.widgets.Textarea(attrs={"placeholder":"Product Description","class":"form-control"}),
            "price":forms.widgets.NumberInput(attrs={"placeholder":"Product Price","class":"form-control"}),


            
            }

