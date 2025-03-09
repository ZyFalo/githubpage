import os
import django
import requests
from bs4 import BeautifulSoup
from django.utils import timezone
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'album.settings')
django.setup()

from apps.noticias.models import Noticia

def scrape_article_content(article_url):
    response = requests.get(article_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content_div = soup.find('div', class_='article-content')
    paragraphs = content_div.find_all('p')
    content = "\n".join([p.get_text() for p in paragraphs])
    return content

def scrape_news():
    url = 'https://www.futbolred.com/futbol-colombiano/liga-betplay'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    news_list = []

    for article in soup.find_all('article', class_='mod-intro-articulo'):
        title = article.find('h3', class_='titulo-intro').text.strip()
        description = article.find('p', class_='texto-intro').text.strip()
        link = article.find('a', class_='boton')['href']
        full_link = f"https://www.futbolred.com{link}"
        imageurl = article.find('img')['src']
        full_imageurl = f"https://www.futbolred.com{imageurl}"
        date_str = article.find('span', class_='fecha').text.strip()
        
        # Ajustar el formato de la fecha
        try:
            if 'a.m.' in date_str or 'p.m.' in date_str:
                # Si la fecha contiene 'a.m.' o 'p.m.', es una hora del día de hoy
                date = datetime.strptime(date_str, '%I:%M %p')
                date = date.replace(year=timezone.now().year, month=timezone.now().month, day=timezone.now().day)
                date = timezone.make_aware(date, timezone.get_current_timezone())
            else:
                # Si la fecha es una fecha completa
                date = datetime.strptime(date_str, '%b. %d de %Y')
                date = timezone.make_aware(date, timezone.get_current_timezone())
        except ValueError:
            date = timezone.now()  # En caso de error, usar la fecha actual

        content = scrape_article_content(full_link)

        news_list.append({
            'title': title,
            'description': description,
            'link': full_link,
            'imageurl': full_imageurl,
            'date': date,
            'content': content
        })

    return news_list

if __name__ == '__main__':
    Noticia.objects.all().delete()

    news = scrape_news()
    for item in news:
        Noticia.objects.update_or_create(
            title=item['title'],
            defaults={
                'description': item['description'],
                'content': item['content'],
                'imageurl': item['imageurl'],
                'date': item['date'],
                'last_updated': timezone.now()
            }
        )