from DrissionPage import Chromium, ChromiumOptions
from datetime import datetime
import time
import json

chat_url = r'https://www.dopple.ai/profile/b82217b8-91fa-454c-a619-90661e9fdd0a'
PROFILE_PATH = r'C:\Users\lnaad\AppData\Local\Google\Chrome\User Data'
MESSAGES_FILE = 'messages.txt'
OUTPUT_FILE = f'responses_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'

co = ChromiumOptions()
co.set_argument('--no-sandbox')
co.set_argument('--disable-dev-shm-usage')
co.set_user_data_path(PROFILE_PATH)
co.set_argument('--profile-directory=Aadarsh')

tab = Chromium().latest_tab
tab.get(chat_url)

chat_btn = tab.ele('tag:button@@text()=Chat Now', timeout=10)
chat_btn.click()

popup = tab.ele("tag:h2@@text()=Remind me later", timeout=5)
if popup:
    popup.click()

with open(MESSAGES_FILE, 'r') as f:
    messages = [line.strip() for line in f if line.strip()]

results = []

for message in messages:
    message_area = tab.ele('tag:textarea@placeholder=Message Zhongli...', timeout=10)
    message_area.click()
    message_area.input(message)
    message_area.input('\n')

    # Wait for response to appear
    time.sleep(6)

    # Grab the last assistant message bubble
    bubbles = tab.eles('css:.border-chat-ai', timeout=5)
    response_text = bubbles[-1].text if bubbles else ''

    results.append({'message': message, 'response': response_text})
    print(f'Q: {message}\nA: {response_text}\n')

    time.sleep(2)

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f'Saved {len(results)} responses to {OUTPUT_FILE}')
