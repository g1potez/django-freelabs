from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
import main.views
import footer.views
import mynewuser.views
import userprofile.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.index, name='index'),
    path('sign_in/', mynewuser.views.sign_in, name='sign_in'),
    path('sign_up/', mynewuser.views.sign_up, name='sign_up'),
    path('sign_out/', mynewuser.views.sign_out, name='sign_out'),
    path('profile/', userprofile.views.profile, name='profile'),
    path('support/', footer.views.support, name='support'),
    path('profile/edit/', userprofile.views.edit, name='edit'),
    path('recommends/', main.views.recommends, name='recommends'),
    path('charts/', main.views.charts, name='charts'),
    path('addlisten/', main.views.addlisten, name='addlisten')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
