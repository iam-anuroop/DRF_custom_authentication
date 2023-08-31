from rest_framework.authentication import BasicAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed



class Myauth(BasicAuthentication):
    def authenticate(self, request):
        uname = request.GET.get('username')
        if uname is None:
            return None
        try:
            user = User.objects.get(username=uname)
        except User.DoesNotExist:
            return AuthenticationFailed('No user in this user name')
        return(user,None)