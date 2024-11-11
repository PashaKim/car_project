import smtplib
from email.mime.text import MIMEText

from car_project.settings import MAIL_FROM, MAIL_PASS, MAIL_TO, SMTP_SERVER, SMTP_PORT
from main.models import CustomerRequest


def send_email_to_admin(customer_request: CustomerRequest):
    smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    msg_txt = f"""
        Ім'я/ телефон:  {customer_request.customer.user.first_name} / {customer_request.customer.user.username}  \n
        Марка та модель авто: {customer_request.car_model} \n
        VIN: {customer_request.car_vin} \n
        Назва запчастини: {customer_request.car_part_name} \n
        Місто: {customer_request.car_city} \n
        Додаткова інформація: {customer_request.additional_info} \n
        
        в адмінці: moderatory/main/customerrequest/{customer_request.id}/change/
    """
    msg = MIMEText(msg_txt)
    msg['Subject'] = f"Нове замовлення: {customer_request.customer.user.username} / {customer_request.car_part_name}"
    msg['From'] = MAIL_FROM
    smtp.ehlo()
    smtp.starttls()
    smtp.login(MAIL_FROM, MAIL_PASS)
    smtp.sendmail(MAIL_FROM, MAIL_TO, msg.as_string())
    smtp.quit()


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

