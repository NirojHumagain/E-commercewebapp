from django.shortcuts import render

# Create your views here.

#def homeview(request):
#
#    return render(request,'shop-index.html')
from django.views.generic.base import View

from home.models import Item, Brand, Ad, Slider


class BaseNavView(View):
    template_context = {}

class HomeBaseView(BaseNavView):
    def get(self,request):
        self.template_context['brands'] = Brand.objects.all()
        self.template_context['indexsale'] = Item.objects.filter(status = 'sale')
        self.template_context['indexhot'] = Item.objects.filter(status = 'hot')
        self.template_context['indexnew'] = Item.objects.filter(status = 'new')
        self.template_context['indexdefault'] = Item.objects.filter(status = 'default')
        self.template_context['ads']= Ad.objects.all()
        self.template_context['sliders'] = Slider.objects.all()
        return render(self.request,'shop-index.html',self.template_context)
