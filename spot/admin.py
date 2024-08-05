from django.contrib import admin

# Register your models here.


from spot.models import Genre, Album, Music, PlayList, History

admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Music)
admin.site.register(PlayList)
admin.site.register(History)
