#coding:utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator
from haystack.generic_views import SearchView
# Create your views here.
def index(request) :
    goodsinfo = []  #-->{'typeofgoods':,'new_list':,'click_list':}
    #查询分类对象
    #查询分类对象中最火，以及最新的四个对象
    typeofgoods = TypeofGoods.objects.all()
    for t1 in typeofgoods:
        nlist = t1.goodsinfo_set.order_by('-id')[0:4]
        clist = t1.goodsinfo_set.order_by('-gclick')[0:4]
        goodsinfo.append({'t1':t1,'nlist':nlist,'clist':clist})
    context = {'glist':goodsinfo,'title':'主页','chart_show':'2'}
    return render(request,'goodsinfo/index.html',context)

def detail(request,gid):
    goods = GoodsInfo.objects.filter(pk=gid)[0]
    # print goods
    goods.gclick += 1
    goods.save()
    new_list = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context={'title':'商品详情','chart_show':'2','nlist':new_list,'goods':goods}
    response = render(request,'goodsinfo/detail.html',context)
    #用cookie保存最近浏览的商品的id信息-->字符串recent_goodlist
    recent_goodlist = request.COOKIES.get('goods_ids','').split(',')
    #如果浏览的商品在原来的浏览列表中,则删除原来的，并把最新的浏览信息保存在列表最前面
    if gid in recent_goodlist:
        recent_goodlist.remove(gid)
    recent_goodlist.insert(0,gid)
    #如果保存的浏览列表大于5个，则清除最前面浏览的一个，（注意第一次为空的时候需要维护，故+1）
    if len(recent_goodlist)>6:
        recent_goodlist.pop()
    #得到列表后存入cookie中
    response.set_cookie('goods_ids',','.join(recent_goodlist),max_age=60*60*24*7)
    return response

def list(request,tid,pindex,means):
    pindex = int(pindex)
    #得到商品分类对象
    typegoods = TypeofGoods.objects.filter(pk=int(tid))[0]
    #最新的4件商品
    new_list = typegoods.goodsinfo_set.order_by('-id')[0:3]
    #按价格排序
    # price_list = typegoods.goodsinfo_set.order_by('-gprice')
    #按点击量排序
    # pclick_list = typegoods.goodsinfo_set.order_by('-gclick')
    #属于此类的所有的商品(默认按id)
    desct = 1
    if means == '1':
        all_list = typegoods.goodsinfo_set.order_by('-id')
    elif means == '2':
        desct = request.GET.get('desct','1')
        if desct == '0':
            all_list = typegoods.goodsinfo_set.order_by('-gprice')
        else:
            all_list = typegoods.goodsinfo_set.order_by('gprice')
    elif means == '3':
        all_list = typegoods.goodsinfo_set.order_by('-gclick')
    paginator = Paginator(all_list,10)
    p = paginator.page(pindex)
    page_list = get_page_lsit(p,pindex)
    context = {'title': '商品列表','chart_show':'2','typegoods':typegoods,'nlist':new_list,'page':p,
               'order_by':means,'page_list':page_list,'desct':desct}
    return render(request,'goodsinfo/list.html',context)


class MySearchView(SearchView):
    """My custom search view."""
    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        context['title'] = '搜索结果'
        context['chart_show']='2'
        page = context.get('page_obj')
        page_list = get_page_lsit(page,page.number)
        context['page_list']=page_list
        print page_list
        # do something
        return context

def get_page_lsit(p,pindex):
    '''定义一个传入page对象，得到page_list对象的方法，用于 分页'''
    page_list = []
    if p.paginator.num_pages<=5:
    #当列表总数小于5的时候
        for i in range(1,p.paginator.num_pages+1):
            page_list.append(i)
    else:
    #当列表总数大于5的时候
        if pindex <= 2:
            # print '111111111'
            page_list=[1,2,3,4,5]
        elif pindex >= p.paginator.num_pages-1:
            page_list=[p.paginator.num_pages-4,p.paginator.num_pages-3,p.paginator.num_pages-2,
                       p.paginator.num_pages-1,p.paginator.num_pages]
        else:
            # print '33333333333'
            page_list=[p.number-2,p.number-1,p.number,p.number+1,p.number+2]
    return page_list