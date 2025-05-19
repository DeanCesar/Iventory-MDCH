from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
    orders=Order.objects.all()
    products=Product.objects.all()
    orders_count=orders.count()
    product_count=products.count()
    workers_count=User.objects.all().count()
    if request.method == 'POST':
        form=OrderForm (request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form=OrderForm ()
    context={
        'orders':orders,
        'form':form,
        'products':products,
        'product_count':product_count,
        'workers_count':workers_count,
        'orders_count':orders_count,

    }
    return render (request, 'dashboard/index.html', context)

@login_required
def staff(request):
    workers =User.objects.all()
    workers_count= workers.count()
    orders_count = Order.objects.all().count()
    product_count=Product.objects.all().count()
    context={
        'workers': workers,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'product_count': product_count,
    }
    return render (request, 'dashboard/staff.html', context)

@login_required
def staff_detail(request, pk):
    workers= User.objects.get(id=pk)
    context={
        'workers':workers,
        'selected_staff_username': workers.username,
    }
    return render(request, 'dashboard/staff_detail.html', context )

@login_required
def product(request):
    items=Product.objects.all() #Using ORM
    product_count=items.count()
    #items=Product.objects.raw('SELECT*FROM dashboard_product')
    workers_count =User.objects.all().count()

    orders_count = Order.objects.all().count()
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name= form.cleaned_data.get('name')
            messages.success (request, f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form=ProductForm()
    context={
        'items':items,
        'form':form,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'product_count': product_count,
    }
    return render (request, 'dashboard/product.html',context)


@login_required
def product_delete(request, pk):
    item= Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

@login_required
def product_update(request, pk):
    item=Product.objects.get(id=pk)
    if request.method=='POST':
        form=ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form=ProductForm(instance=item)
    context={
        'form': form,

    }
    return render(request, 'dashboard/product_update.html', context)
@login_required
def order(request):
    order = Order.objects.filter(status='pendiente')
    orders_count=order.count()
    workers_count =User.objects.all().count()
    product_count=Product.objects.all().count()

    context = {
        'order': order,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'product_count': product_count,

    }
    return render(request, 'dashboard/order.html', context)


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

@login_required
def accept_order(request, order_id):
    # Solo permitir si el usuario es staff/admin
    if not request.user.is_staff:
        return redirect('dashboard-order')  # opcional: o mostrar error/403

    order = get_object_or_404(Order, pk=order_id)
    if order.status == 'pendiente':
        # Actualizar estado a "aceptada"
        order.status = 'aceptada'
        # Actualizar stock del producto asociado
        product = order.product
        product.quantity -= order.cantidad  # descontar la cantidad pedida del stock
        # Si se desea, verificar que product.quantity no quede negativo
        product.save()
        order.save()
    # Redirigir de vuelta a la lista de pendientes (dashboard-order)
    return redirect('dashboard-order')


@login_required
def deny_order(request, order_id):
    if not request.user.is_staff:
        return redirect('dashboard-order')
    order = get_object_or_404(Order, pk=order_id)
    if order.status == 'pendiente':
        order.status = 'denegada'
        order.save()
    return redirect('dashboard-order')