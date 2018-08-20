from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic
from django.http import HttpResponse
from .models import VpnInfo
from .utils import login_check_in, register


# Create your views here.

class IndexView(generic.ListView):
    model = VpnInfo


# 'nydjck04839@chacuo.net',
# 'aymgzi63459@chacuo.net',
# 'bwkhfz83467@chacuo.net',
# 'dyswjo58041@chacuo.net',
# 'xleiow26403@chacuo.net',
# 'pimhdc26419@chacuo.net',
# 'dxmpqt46380@chacuo.net',
# 'rfpoxt78026@chacuo.net',
# 'godmnc62473@chacuo.net',

# 由于之前注册没加入数据库,写个路由加入
def vpn_add(request):
    vpn_list = [

    ]
    for email in vpn_list:
        vpn_model = VpnInfo(email=email)
        vpn_model.check_in()
    return HttpResponse('added')
