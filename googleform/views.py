from django.shortcuts import render
from selenium import webdriver
import time
import os
from django.core.mail import EmailMessage
from django.conf import settings



url="https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform"

def index(request):
    web = webdriver.Chrome()
    web.get(url)
    time.sleep(6)

    fullname="Shyamprasad N. Gundeti"
    name=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name.send_keys(fullname)

    contact=9869124896
    contact_int=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    contact_int.send_keys(contact)

    email_id="shyamgundetin@gmail.com"
    email_id_str=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    email_id_str.send_keys(email_id)

    full_address="Mumbai"
    full_address_str=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
    full_address_str.send_keys(full_address)

    Pin_code=400025
    Pin_code_int=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Pin_code_int.send_keys(Pin_code)

    date_of_birth='04-15-1983'
    date_of_birth_str=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    date_of_birth_str.send_keys(date_of_birth)

    gender="Male"
    gender_str=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    gender_str.send_keys(gender)

    code="GNFPYC"
    code_str=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    code_str.send_keys(code)

    code_str=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    code_str.click()
    

    web.current_url
    screenshot_filename = 'confirmation_page.png' 
    screenshot_file_path = os.path.join('googleform', screenshot_filename)
    web.save_screenshot(screenshot_file_path)
    web.quit()

  
    recipient_email = 'tech@themedius.ai'
    cc_email = 'hr@themedius.ai'
    
    
    email = EmailMessage(
        subject='Python (Selenium) Assignment - [shyamprasad N. Gundeti]',
        body='Please Find attached The Of Screenshot of Google Form Submitted Response.',
        from_email=settings.EMAIL_HOST_USER,
        to=[recipient_email],
        cc=[cc_email],
    )

    screenshot_path = "googleform/confirmation_page.png"
    with open(screenshot_path, 'rb') as f:
        email.attach('screenshot.png', f.read(), 'image/png')
    
    context = {
        'recipient_email': recipient_email,
        'cc_email': cc_email,
    }

    try:
        email.send()
        return render(request, 'index.html', context)
    except Exception as e:
        return render(request, 'error.html', {'error_message': str(e)})
