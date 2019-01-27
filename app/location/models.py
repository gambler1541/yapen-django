from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    location_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Sub_location(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey('Location',
                                 on_delete=models.CASCADE,
                                 related_name='sub_location',)
    sub_location_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Pensions(models.Model):
    name = models.CharField(max_length=100)
    sub_location = models.ForeignKey('Sub_location',
                                     on_delete=models.CASCADE,
                                     related_name='pension',)
    ypidx = models.CharField(max_length=100)
    pension_img = models.URLField(blank=True,)
    address = models.TextField(max_length=100, blank=True,)
    check_in = models.CharField(max_length=10, blank=True,)
    check_out = models.CharField(max_length=10, blank=True,)
    pick_up = models.TextField(max_length=100, blank=True,)
    number_of_room = models.TextField(max_length=10, blank=True,)
    notice = models.TextField(max_length=100, blank=True,)
    theme = models.TextField(max_length=100, blank=True,)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.TextField(max_length=100)
    pension = models.ForeignKey('Pensions',
                                on_delete=models.CASCADE,
                                related_name='room',)
    # 방 이미지
    room_img = models.URLField(blank=True,)
    # 방 구조
    room_structure = models.TextField(max_length=100, blank=True,)
    # 방 크기
    size = models.TextField(max_length=100, blank=True,)
    # 기준/최대 인원
    max_people = models.TextField(max_length=100, blank=True,)
    # 구비시설
    facilities = models.TextField(max_length=100, blank=True,)
    # 객실 설명
    room_info = models.TextField(max_length=300, blank=True,)







