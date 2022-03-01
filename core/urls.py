from django.contrib import admin
from django.urls import path

from quote.views import KanyeWestTenQuotesView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "kanye-sayings/",
        KanyeWestTenQuotesView.as_view(),
        name="kanye-sayings",
    ),
]
