def send_email(message, recipient , sender = "university.help@gmail.com"):

    if "@" not in sender and (".net"  or ".ru" or ".com") not in sender and "@" not in recipient and (".net" or ".ru" or ".com") not in recipient:
        print("Неверный формат мыла", sender, "и", recipient, "не пойдет")

    elif sender == recipient:
        print("Мыло одинаковое, не пойдет")

    elif sender == "university.help@gmail.com":
        print("Ура, все прошло как по маслу, отправилось c", sender, "на", recipient)
    else:
        print("Мыло что-ли поменял? Аж не узнал, но письмо равно отправил на", recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
