from bs4 import BeautifulSoup

def get_src(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    iframe_tags = soup.find_all('iframe')
    for iframe in iframe_tags:
        src = iframe.get('src')
        return src
