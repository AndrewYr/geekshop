from mainApp.models import Product
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ShopProductRegisterForm(CreateView):
    class Meta:
        model = Product
        template_name = 'adminapp/products_update.html'
        success_url = reverse_lazy('admin_custom:products')
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ShopProductRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
