from django.shortcuts import render, redirect
from .forms import URLForm
from .models import URLRecord
import requests
import matplotlib.pyplot as plt
from io import BytesIO
import base64


def url_list(request):
    urls = URLRecord.objects.all()
    form = URLForm()
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_list')
    return render(request, 'url_list.html', {'urls': urls, 'form': form})

def check_url(request, pk):
    url_record = URLRecord.objects.get(pk=pk)
    try:
        response = requests.get(url_record.url)
        url_record.status = response.status_code == 200
        url_record.save()
    except requests.RequestException:
        url_record.status = False
        url_record.save()
    return redirect('url_list')

def check_all_urls(request):
    urls = URLRecord.objects.all()
    for url_record in urls:
        try:
            response = requests.get(url_record.url)
            url_record.status = response.status_code == 200
            url_record.save()
        except requests.RequestException:
            url_record.status = False
            url_record.save()
    return redirect('url_list')

def delete_url(request, pk):
    url_record = URLRecord.objects.get(pk=pk)
    url_record.delete()
    return redirect('url_list')
def statistics(request):
    available_count = URLRecord.objects.filter(status=True).count()
    unavailable_count = URLRecord.objects.filter(status=False).count()
    # Установка цветов для рабочих и нерабочих URL
    colors = ['green', 'red']
    labels = ['Рабочие URL', 'Нерабочие URL']
    sizes = [available_count, unavailable_count]

    # Построение круговой диаграммы
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Статистика рабочих и нерабочих URL')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Преобразование изображения в строку base64
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    # Возвращаем шаблон с изображением графика
    return render(request, 'statistics.html', {'available_count': available_count, 'unavailable_count': unavailable_count,'graphic': graphic})