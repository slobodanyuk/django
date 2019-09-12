from django.shortcuts import render

def main(request):
    context = {'username': 'ilya', 'role': 'admin'}
    return render(request, 'mainapp/main.html', context=context)


def products(request):
    return render(request, 'mainapp/products.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')
