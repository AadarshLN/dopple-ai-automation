from DrissionPage import Chromium, ChromiumOptions
import time

PROFILE_PATH = r'C:\Users\lnaad\AppData\Local\Google\Chrome\User Data'

co = ChromiumOptions()
co.set_argument('--no-sandbox')
co.set_argument('--disable-dev-shm-usage')
co.set_user_data_path(PROFILE_PATH)
co.set_argument('--profile-directory=Aadarsh')

tab = Chromium().latest_tab
tab.get('https://www.dopple.ai/create')

popup = tab.ele("tag:h2@@text()=Remind me later", timeout=5)
if popup:
    popup.click()

ele1 = tab.ele('@name=name', timeout=10)
ele1.input('Zhongli', clear=True)

ele2 = tab.ele('@name=tagLine', timeout=10)
ele2.input('A Mysterious Consultant', clear=True)

# Step 1: Upload profile image → crop modal appears → save
profile_input = tab.eles('@type=file', timeout=10)[0]
profile_input.input(r'zhongli.jpg')
tab.ele('tag:button@@text()=Save Image', timeout=15).click(by_js=True)

# Step 2: Click "Choose another" → banner crop flow
tab.ele('tag:button@@text()=Choose another', timeout=10).click(by_js=True)

# Step 3: Upload banner image → crop modal appears → save
banner_input = tab.eles('@type=file', timeout=10)[1]
banner_input.input(r'ZhongliInfo.jpg')
tab.ele('tag:button@@text()=Save Image', timeout=15).click(by_js=True)

# Fill bio
ele3 = tab.ele('tag:textarea@name=bio', timeout=10)
ele3.scroll.to_see()
time.sleep(0.3)
tab.actions.move_to(ele3).click()
time.sleep(0.5)
ele3.input('A mysterious consultant from the Wangshen Funeral Parlour who is always calm and composed, with a deep understanding of the world around him. He is a master of the art of persuasion and is able to navigate complex social situations with ease. Despite his calm demeanor, he is a formidable opponent and should not be underestimated.', clear=True)

# Open Category dropdown and select "Games"
category_btn = tab.ele('tag:span@@text()=Select category', timeout=10).parent().parent()
category_btn.scroll.to_see()
time.sleep(0.5)
tab.actions.move_to(category_btn).click()
time.sleep(1)
games_option = tab.ele('tag:li@@text()=Games', timeout=5)
tab.actions.move_to(games_option).click()

# Open Visibility dropdown and select "Private"
visibility_btn = tab.ele('tag:span@@text()=Select visibility', timeout=10).parent().parent()
visibility_btn.scroll.to_see()
time.sleep(0.5)
tab.actions.move_to(visibility_btn).click()
time.sleep(1)
private_option = tab.ele('tag:li@@text()=Private', timeout=5)
tab.actions.move_to(private_option).click()

# Click Continue and wait for step 2 to render
continue_btn = tab.ele('tag:button@class:bg-active', timeout=10)
continue_btn.scroll.to_see()
continue_btn.click(by_js=True)
# Wait for the bio field (step 1) to vanish, confirming step 2 is shown
tab.wait.ele_hidden('tag:textarea@name=bio', timeout=15)

# Fill description on next page
desc = tab.ele('tag:textarea@name=description', timeout=15)
desc.click(by_js=True)
time.sleep(0.3)
desc.input('Zhongli is a tall and elegant man from Liyue who always dresses in traditional Liyue attire. He has long, flowing black hair and piercing golden eyes that seem to see right through you. He is a calm and composed individual who is always willing to lend a helping hand to those in need. Despite his gentle demeanor, he is a formidable warrior who is not to be underestimated.', clear=True)

# Fill greeting
greeting = tab.ele('tag:input@name=greeting', timeout=15)
greeting.scroll.to_see()
time.sleep(0.3)
tab.actions.move_to(greeting).click()
time.sleep(0.5)
greeting.input('Hello there! I have many names but you can call me Zhongli. I am here at your service. Should you need any assistance, please do not hesitate to ask. I am always happy to help.', clear=True)

# Open Content Rating dropdown and select "Max (18+)"
rating_btn = tab.ele('tag:span@@text()=Select rating', timeout=10).parent().parent()
rating_btn.scroll.to_see()
time.sleep(0.5)
tab.actions.move_to(rating_btn).click()
time.sleep(1)
max_option = tab.ele('tag:span@@text()=Max (18+)', timeout=5)
tab.actions.move_to(max_option).click()

# Tick the terms and conditions checkbox — empty button identified by border-gray-400 class
terms_checkbox = tab.ele('tag:button@class:border-gray-400', timeout=10)
terms_checkbox.scroll.to_see()
tab.actions.move_to(terms_checkbox).click()

continue_btn = tab.ele('tag:button@class:bg-active', timeout=10)
continue_btn.scroll.to_see()
tab.actions.move_to(continue_btn).click()
time.sleep(2)

#Character creation done if needed user can copy the link of the chat for sharing

