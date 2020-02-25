from rest_framework.permissions import BasePermission
from datetime import datetime , date
from .models import Booking
from flights import views

class OwnerOrAdminBooker(BasePermission):

    def has_object_permission(self,request,view,obj):
        if request.user.is_staff or request.user == obj.user:
            return True
        return False

class CannotCancelOrUpdate(BasePermission):

    def has_object_permission(self , request , view , obj):
        bookingdate = obj.date - date.today()
        bookingdateindays = bookingdate.days

        if bookingdateindays > 3:
            return True
        return False
