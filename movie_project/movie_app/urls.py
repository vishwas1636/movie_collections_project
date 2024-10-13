from django.urls import path
from .views import Register, GetToken, get_my_collections, get_movie_list, collections_get_or_add, Collectionedit, get_request_count, reset_request_count

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('token/', GetToken.as_view(), name='token_obtain_pair'),
    path('movies/', get_movie_list),
    path('collection/', collections_get_or_add, name='collections-get-or-add'),  # we can use GET and POST
    path('collection/<uuid>/', Collectionedit.as_view(), name='collection-detail'),
    path('my-collections/', get_my_collections, name='get-my-collections'),
    path('request-count/', get_request_count),
    path('request-count/reset/', reset_request_count),
]
