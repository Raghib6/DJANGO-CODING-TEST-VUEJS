import django_filters
from .models import Product, ProductVariant
from django import forms


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr="icontains",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Search Product"}
        ),
    )
    productvariant = django_filters.ModelMultipleChoiceFilter(
        queryset=ProductVariant.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control",
            }
        ),
    )

    created_at = django_filters.DateFilter(
        "created_at",
        label=("Date"),
        lookup_expr="contains",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
    )
    productvariantprice = django_filters.NumberFilter()
    min_price = django_filters.NumberFilter(
        field_name="productvariantprice",
        lookup_expr="gte",
        widget=forms.NumberInput(
            attrs={"type": "text", "class": "form-control", "placeholder": "From"}
        ),
    )
    max_price = django_filters.NumberFilter(
        field_name="productvariantprice",
        lookup_expr="lte",
        widget=forms.NumberInput(
            attrs={"type": "text", "class": "form-control", "placeholder": "To"}
        ),
    )

    class Meta:
        model = Product
        exclude = ["id"]
