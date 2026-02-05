import requests
from bs4 import BeautifulSoup
import random

def start_zood():
    # الصق الرابط الطويل اللي جبته من Make.com هنا بين علامتي التنصيص
    WEBHOOK_URL = "https://hook.eu1.make.com/q3628igtbrxmah6zqsuhowstjox5cmww"
    
    url = "https://haraj.com.sa/tags/إبل"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('div', class_='ad-item-content')[:5]
        
        for item in items:
            title = item.find('h3').text.strip()
            # عناوين ذكية عشان قوقل يرفعك للصدارة
            smart_title = f"فرصة: {title} | حراج السعودية"
            
            data = {
                "title": smart_title,
                "content": f"عرض جديد في سوق الإبل: {title}. لمزيد من العروض تابع منصة ذود."
            }
            requests.post(WEBHOOK_URL, json=data)
            print(f"تم الإرسال بنجاح: {smart_title}")
            
    except Exception as e:
        print(f"حدث خطأ: {e}")

if __name__ == "__main__":
    start_zood()
