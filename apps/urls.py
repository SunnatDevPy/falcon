from django.urls import path

from apps.views import MainTemplateView, Products, Profile, Settings, LogoutView, CustomLoginView, ProductDetailView, \
    OrderCreateView, OrderListView, LoveProductView, MarketView, OperatorView, DeliveryIsReady, RegisterView, \
    ClikLikeView

urlpatterns = [
    path('', MainTemplateView.as_view(), name='main_page'),
    path('product', Products.as_view(), name='category_to_product'),


    path('detail-product/<int:pk>', ProductDetailView.as_view(), name='detail_product'),
    path('profile', Profile.as_view(), name='profile'),
    path('settings', Settings.as_view(), name='settings'),


    path('logout', LogoutView.as_view(), name='logout'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('love-product', LoveProductView.as_view(), name='love-product'),


    path('create-order', OrderCreateView.as_view(), name='order_create'),
    path('order-list', OrderListView.as_view(), name='order_list'),


    path('market', MarketView.as_view(), name='market'),

    path('operator', OperatorView.as_view(), name='operator'),
    path('delivery-is-ready', DeliveryIsReady.as_view(), name='delivery-is-ready'),
    path('product/click/like/<int:pk>', ClikLikeView.as_view(), name='click_like'),



]
