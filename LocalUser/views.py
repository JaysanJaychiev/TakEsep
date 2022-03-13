from allauth.account.decorators import login_required
from django.http import HttpResponse



@login_required
def home(request):
    html = "<html><body>you are logged in, welcome!</body></html>"
    return HttpResponse(html)


