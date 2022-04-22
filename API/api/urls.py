from urllib.parse import urlparse
from django.urls import path, re_path
from . import views
#setting some urls
urlpatterns = [
        path('charachters/compare/<int:first_id>/<int:second_id>', views.getCompare, name='Ids'), #getting by /
        re_path(r'^charachters/compare/(?P<characters_ids>[\d,]+)', views.getCompare, name='Ids'),# getting multiple with ,
        path('charachters/compare_to_csv/<int:first_id>/<int:second_id>', views.getCompareCsv, name='Ids'),
        re_path(r'^charachters/compare_to_csv/(?P<characters_ids>[\d,]+)', views.getCompareCsv, name='Ids'),
]
