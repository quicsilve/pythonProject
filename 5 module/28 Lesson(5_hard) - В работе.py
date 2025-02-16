# Дополнительное практическое задание по модулю: "Классы и объекты."
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности.
# Задание "Свой YouTube":
# Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные полезные ролики на тему IT (юмористические, интервью и т.д.). Конечно же для старта написания интернет ресурса требуются хотя бы базовые знания программирования.
# Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые будут выполнять похожий функционал на сайте.
# Всего будет 3 класса: UrTube, Video, User.
# Общее ТЗ:
# Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео, авторизации и регистрации пользователя и т.д.
# Подробное ТЗ:
# Каждый объект класса User должен обладать следующими атрибутами и методами:
# Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
# Каждый объект класса Video должен обладать следующими атрибутами и методами:
# Атрибуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
#  Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
# Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
# Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
# Метод log_out для сброса текущего пользователя на None.
# Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
# Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
# Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
# Для метода watch_video так же учитывайте следующие особенности:
# Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
# Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
# Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
# После воспроизведения нужно выводить: "Конец видео"
# Код для проверки:
# ur = UrTube()
# v1 = Video('Лучший язык программирования 2024 года', 200)
# v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# # Добавление видео
# ur.add(v1, v2)
# # Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))
# # Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')
# # Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)
# # Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')
# Вывод в консоль:
# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist
# Примечания:
# Не забывайте для удобства использовать dunder(магические) методы: __str__, __repr__, __contains__, __eq__ и др. (повторить можно здесь)
# Чтобы не запутаться рекомендуется после реализации каждого метода проверять как он работает, тестировать разные вариации.

import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        self.orig_pass = password

    def __repr__(self):
        return f'Пользователь: {self.nickname}, возраст: {self.age}'

    def __str__(self):
        return f'Пользователь: {self.nickname}, возраст: {self.age}'

    def get_params(self):
        return [self.nickname, self.age]

    def reg_params(self):
        return [self.nickname, self.orig_pass, self.age]

    def get_pass(self):
        return self.password

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        if isinstance(duration, str):  # Если длительность строка, то "разбираем" на ч. и мин.
            time = duration.split(':')
            self.duration = int(time[0]) * 3600 + int(time[1]) * 60
        else:
            self.duration = duration  # Если длительность число, то поросто присваиваем
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        adult_status = ''  # сообщение о фильме с названием, длительностью и статусом
        adult_status = 'Фильм для взрослых (18+)' if self.adult_mode else 'Фильм для всей семьи'
        return f'Название: {self.title}. Длительность: {self.duration // 3600}:{self.duration % 3600 / 60:.0f} ч. ' + adult_status

    def data(self):
        return [self.title, self.duration, self.time_now, self.adult_mode]

    def set_tnow(self, time):
        self.time_now = time

    def inc_tnow(self, time):
        self.time_now += time


class UrTube:
    def __init__(self, users, videos, current_user):
        # self.title = title
        self.users = {}  # Для удобства/быстроты поиска пользователей/фильмов - словари.
        self.videos = {}  # Ключ - имя пользователя/название фильма, значение - класс
        self.curent_user = None

    def log_in(self, nickname, password):  # Логин
        if nickname in self.users:  # Смотрим есть ли пользователь в списке Пользователей
            if self.users[nickname].get_pass() == hash(
                    password):  # Смотрим совпадают ли хэши паролей, если пользователь найден
                self.curent_user = self.users[nickname]  # Curent_user будет пользователь класса User
                self.cur_user()  # Вывести текущего пользователя
            else:  
                print('Пароль неверный, проверьте ввод данных (раскладка, CapsLock)')
        else:  
            print(f'Пользователя с ником {nickname} не найдено')

    def register_u(self, nickname, password, age):  # Регистрация
        if nickname in self.users:  
            print(f'Пользователь с ником {nickname} уже существует.')
            print(f'Проверьте данные или авторизуйтесь')
        else:
            self.users[nickname] = User(nickname, password, age)  # Создаем пользователя класса User
            print(f'Успешная регистрация {self.users[nickname].get_params()[0]}')
            self.log_in(nickname, password)  # Автоматическая авторизация после регистрации

    def log_out(self):
        self.curent_user = None

    def add(self, *args):  # добавить видео
        for object_v in args:
            if isinstance(object_v, Video):  # Проверяем объекты на принадлежность классу Video
                if object_v.data()[0] in self.videos:  # Смотрим есть ли название фильма в списке фильмов
                    print(f'Фильм с названием "{object_v.data()[0]}" уже есть в библиотеке')
                else:
                    self.videos[object_v.data()[0]] = object_v

    def get_videos(self, str_to_find):  # поиск видео
        vid_list = [title for title in self.videos.keys() if str_to_find.casefold() in title.casefold()]
        if vid_list:
            return vid_list
        else:
            return f'По параметрам "{str_to_find}" ничего не найдено'

    def watch_video(self, title):  # просмотр видео
        from time import sleep
        wv = self.videos.get(title, None)

        def broadcast():  
            nonlocal wv
            print(f'Фильм {wv.data()[0]}.')
            print('Приятного просмотра')
            print('Время просмотра: ', end='')
            while wv.data()[2] < wv.data()[1]:
                print(wv.data()[2], end=' ')
                wv.inc_tnow(1000)
                sleep(.1)
            print(wv.data()[1])
            wv.set_tnow(0)  # Сброс текущего времени просмотра
            print('Конец просмотра')

        if wv:  # Проверка на наличие фильма
            if self.curent_user != None:  # Фильм есть. Проверка на авторизацию
                if wv.data()[3]:  # Фильм есть. Авторизован. Проверка на adult
                    if self.curent_user.get_params()[1] >= 18:  # Пройдены все проверки
                        broadcast()
                    else:  # Фильм есть и авторизировался. НЕТ 18 ЛЕТ !
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:  # Фильм есть. Авторизован. Проверка на adult не требуется
                    broadcast()
            else:  # Фильм есть, нет авторизации
                print('Войдите в аккаунт, чтобы смотреть видео')
        else:  # Фильма нет 
            print(f'Фильм {title} не обнаружен')

    def users(self):
        return len(self.users)

    def all_users(self):  # все пользователи
        print('Пользователи:')
        if not self.users:
            print('Отсутствуют')
        else:
            for u_data in self.users.values():
                print(f'Ник: {u_data.get_params()[0]}, возраст: {u_data.get_params()[1]}')

    def all_videos(self):  # все видео
        print('Фильмы:')
        if not self.videos:
            print('Отсутствуют')
        else:
            for v_data in self.videos.values():
                print(v_data)

    def cnt_videos(self): # текущее видео
        return len(self.videos)

    def cur_user(self): # текущий пользователь
        if self.curent_user:
            print(f'Текущий пользователь: {self.curent_user.get_params()[0]}')
        else:
            print('Пользователь не авторизован')

# Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
