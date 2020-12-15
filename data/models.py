from django.db import models

from django.utils import timezone

import os

from urllib import request

class Apod(models.Model):
    pub_date = models.CharField('дата публикации',max_length = 15)
    explanation = models.TextField('описание')
    title = models.CharField('заголовок',max_length = 50)
    image_url = models.CharField('изображение',max_length = 100)
    image_hd_url = models.CharField('изображение в hd',max_length = 100,null=True)
    media_type = models.CharField('тип медиа',max_length = 20)
    service_version = models.CharField('сервисаная версия',max_length = 5)

    received_date = models.DateTimeField('дата получения данных',default = timezone.now())

    def __str__(self):
        return self.title

    # def get_remote_image(self,data):
    #     result = request.urlretrieve(data)
    #     self.image_url.save( os.path.basename(self.image_url),
    #             File(open(result[0], 'rb'))
    #             )
    #
    # def get_remote_image_hd(self,data):
    #     result = request.urlretrieve(data)
    #     self.image_hd_url.save( os.path.basename(self.image_hd_url),
    #             File(open(result[0], 'rb'))
    #             )

    class Meta():
        verbose_name = 'единица информации'
        verbose_name_plural = 'единицы информации'
