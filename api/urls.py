from django.urls import path
from .views import NewRegisterView, create_product, get_product, get_product_by_id, update_product, delete_product, partial_update_product,\
      BlogList, BlogCreate, BlogDetail, BlogUpdate, BlogDelete, BlogListCreateView, BlogRetrieveUpdateDestroyView, \
      RegisterView, LoginView, LogoutView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
 
# from . import views
# from rest_framework import routers

# router = routers.DefaultRouter()

# router.register(r'products',views.ProductViewSet)



# urlpatterns = router.urls


urlpatterns = [
    #function based views
#     path('create_product/', create_product, name='create-product'),
#     path('get_product/', get_product, name='get-product'),
#     path('get_product/<int:id>/', get_product_by_id, name='get-product-by-id'),
#     path('update_product/<int:id>/', update_product, name='update-product'),
#     path('delete_product/<int:id>/', delete_product, name='delete-product'),
#     path('update/<int:id>/', partial_update_product, name='partial-update-product'),


    # class based views
#     path('blogs/', BlogList.as_view(), name='blog-list'),
#     path('blogs/create/', BlogCreate.as_view(), name='blog-create'),
#     path('blogs/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
#     path('blogs/<int:pk>/update/', BlogUpdate.as_view(), name='blog-update'),
#     path('blogs/<int:pk>/delete/', BlogDelete.as_view(), name='blog-delete'),
    path('blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogRetrieveUpdateDestroyView.as_view(), name='blog-retrieve-update-destroy'),

    path('newregister', NewRegisterView.as_view(), name='register-view'),
    path('login/token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('refresh/token/', TokenRefreshView.as_view(), name='token-refresh'),

    
    #authentication
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),




] 
