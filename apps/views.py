from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView

from apps.forms import CustomUserCreationForm, CustomAuthenticationForm
from apps.models import Category, Product, Order, User, LoveProduct


# Create your views here.
class MainTemplateView(LoginRequiredMixin, ListView):
    queryset = Product.objects.all()
    template_name = 'apps/main/index.html'
    context_object_name = 'products'
    success_url = reverse_lazy('main_page')
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        request = self.request
        user_id = request.user.id
        product_id = request.POST.get('product_id')
        LoveProduct.objects.create(user_id=user_id, product_id=product_id)
        return super().get(request, *args, **kwargs)


class Products(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'apps/shopping/product.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        if slug := self.request.GET.get('slug'):
            return qs.filter(category__slug=slug)
        return qs


class ProductDetailView(LoginRequiredMixin, DetailView):
    queryset = Product.objects.all()
    template_name = 'apps/shopping/product_detail.html'
    context_object_name = 'product'

    # def post(self, request, pk):
    #     user_id = request.POST.get('user_id')
    #     product_id = request.POST.get('product_id')
    #     count = request.POST.get('count')
    #     phone = request.POST.get('phone')
    #     Order.objects.create(user_id=user_id, product_id=product_id, count=count, phone=phone)
    #     return redirect('main_page')


class OrderListView(LoginRequiredMixin, ListView):
    queryset = Order.objects.all()
    template_name = 'apps/shopping/order-list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class OrderCreateView(LoginRequiredMixin, CreateView):
    queryset = Order.objects.all()
    fields = 'user', 'product', 'phone', 'count'
    template_name = 'apps/shopping/product_detail.html'
    success_url = reverse_lazy('main_page')


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'apps/auth/profile.html'


class Settings(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    fields = 'first_name', 'last_name', 'description', 'phone', 'image'
    template_name = 'apps/auth/settings.html'
    success_url = reverse_lazy('main_page')

    def get_object(self, queryset=None):
        return self.request.user


class RegisterView(CreateView):
    template_name = 'apps/auth/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_invalid(self, form):
        return super().form_invalid(form)


class CustomLoginView(LoginView):
    template_name = 'apps/auth/login.html'
    form_class = CustomAuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('main_page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class LoveProductView(LoginRequiredMixin, ListView):
    queryset = LoveProduct.objects.all()
    template_name = 'apps/other/love-products.html'
    context_object_name = 'love_products'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user__pk=self.request.user.pk)


class MarketView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/other/market.html'


class OperatorView(TemplateView):
    template_name = 'apps/operator/operators.html'


class DeliveryIsReady(TemplateView):
    template_name = 'apps/operator/delivery_is_ready.html'


class ClikLikeView(View):
    def get(self, request, pk):
        obj, created = LoveProduct.objects.get_or_create(user=self.request.user, product_id=pk)
        if not created:
            obj.delete()
            return redirect('main_page')
        return redirect('main_page')
