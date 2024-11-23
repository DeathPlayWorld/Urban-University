
def validating_domain(domain):
    while domain[0] != ".": domain = domain[1:-1] + domain[-1]
    return domain

def get_domain(address:str):
    domain = address[-4:-1] + address[-1]
    return validating_domain(domain)

def valid_mail(sender, recipient):
    if ((get_domain(sender) != ".ru" and get_domain(sender) != ".com" and get_domain(sender) != ".net") or
        (get_domain(recipient) != ".ru" and get_domain(recipient) != ".com" and get_domain(recipient) != ".net") or
        ("@" not in sender or "@" not in recipient)):
        return "Domain_Error"
    elif sender == recipient:
        return "Self_Message"
    else: return "Valid_Message"

def send_email(message, recipient, *,sender = "university.help@gmail.com"):
    match valid_mail(sender, recipient):
        case "Domain_Error":
            print("\nНевозможно отправить письмо с адреса", sender, "на адрес", recipient)
        case "Self_Message":
            print("\nНельзя отправить письмо самому себе!")
        case "Valid_Message":
            if sender != "university.help@gmail.com":
                print("\nНЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
            else:
                print("\nПисьмо успешно отправлено с адреса", sender, "на адрес", recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
