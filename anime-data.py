from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import yaml

app = Flask(__name__)
CORS(app) # للسماح للـ HTML/JS بالاتصال بالسيرفر

# تحميل الإعدادات من ملف yaml
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

TARGET_SITE = config['scraper']['target_site']
HOST_IP = config['server']['host']
PORT = config['server']['port']

# --- 1. نظام المصادقة اليدوي ---
@app.route('/api/auth/send_code', methods=['POST'])
def send_code():
    data = request.json
    email = data.get('email')
    # هنا تضع منطق إرسال الإيميل (SMTP)
    print(f"تم إرسال رمز التحقق إلى: {email}")
    return jsonify({"message": "تم الإرسال بنجاح", "status": "success"})

@app.route('/api/auth/verify', methods=['POST'])
def verify_code():
    data = request.json
    code = data.get('code')
    # هنا تضع منطق التحقق من الرمز
    print(f"جاري التحقق من الرمز: {code}")
    return jsonify({"message": "تم تسجيل الدخول", "status": "success"})

# --- 2. الكاشط الداخلي (Scraper) ---
def scrape_anime(url):
    print(f"جاري كشط البيانات من: {url}")
    # هنا تضع كود BeautifulSoup الخاص بك لسحب الحلقات والصور
    # page = requests.get(url)
    # soup = BeautifulSoup(page.content, 'html.parser')
    
    # بيانات وهمية للتجربة (Mock Data)
    return [
        {"title": "Anime 1", "episode": "الحلقة 10", "rating": "8.1", "image": "https://via.placeholder.com/150"},
        {"title": "Anime 2", "episode": "الحلقة 9", "rating": "8.3", "image": "https://via.placeholder.com/150"}
    ]

@app.route('/api/anime/latest', methods=['GET'])
def get_latest_anime():
    try:
        data = scrape_anime(TARGET_SITE)
        return jsonify({"data": data, "status": "success"})
    except Exception as e:
        return jsonify({"error": str(e), "status": "failed"}), 500

if __name__ == '__main__':
    print(f"السيرفر يعمل على: http://{HOST_IP}:{PORT}")
    app.run(host=HOST_IP, port=PORT, debug=True)
