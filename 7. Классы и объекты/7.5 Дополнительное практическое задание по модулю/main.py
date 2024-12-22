from time import sleep

class UrTube:
    def __init__(self, current_user = None):
        self.users = []
        self.videos = []
        self.current_user = current_user

    def log_out(self):
        self.current_user = None

    def log_in(self, nickname, password):
        successful_log_in = False
        for name in self.users:
            if nickname == name.nickname:
                if hash(password) == hash(name.password):
                    self.current_user = name
                    successful_log_in = True
                    print(f"Welcome {str(self.current_user)}!\n")
                    break
        if not successful_log_in: print("Wrong nickname or password!")

    def register(self, nickname, password, age):
        account_exists = False
        for i in range(0, len(self.users)):
            if self.users[i].nickname == nickname:
                account_exists = True
                print(f"User {nickname} already exists!")
        if not account_exists:
            print(f"Creating {nickname} account...")
            self.users.append(User(nickname, password, age))
            print(f"{nickname} account successfully created!")
            self.log_in(nickname, password)

    def add(self, *args):
        for i in args:
            if i in self.videos:
                print(f"There is video with that title already!")
            else: self.videos.append(i)

    def get_videos(self, search_word):
        find_videos = []
        for i in self.videos:
            if search_word.lower() in str(i).lower() or str(i).lower() in search_word.lower():
                find_videos.append(i.title)
        if not find_videos: print("There is no video with this title!")
        return find_videos

    def watch_video(self, film_name):
        found_video = False
        access_to_video = True
        log_in = True
        for i in range(0, len(self.videos)):
            if self.current_user is None:
                log_in = False
                break
            if str(self.videos[i]) == str(film_name):
                found_video = True
                if self.videos[i].adult_mode and self.current_user.age >= 18 or not self.videos[i].adult_mode:
                    playing = True
                    self.videos[i].time_now = 0
                    print(f"Playing '{film_name}'")
                    while True:
                        if not self.videos[i].time_now >= self.videos[i].duration:
                            print(self.videos[i].time_now)
                            self.videos[i].time_now += 1
                            sleep(1)
                        elif not playing or self.videos[i].time_now >= self.videos[i].duration:
                            print(self.videos[i].time_now)
                            print("End of the video.")
                            break
                    break
                else: access_to_video = False
                break
        if not log_in: print("Please log in first!")
        elif not found_video: print("There is no video with this title!")
        elif not access_to_video: print("You have no access to this video!")

class Video:

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __len__(self):
        return self.duration

class User:
    def __init__(self, nickname, password,  age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

    def __len__(self):
        return self.age

#Entry variables
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень-программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print("\nSearch check:")
print(str(ur.get_videos('лучший')))
print(str(ur.get_videos('ПРОГ')))

# Проверка на вход пользователя и возрастное ограничение
print("\nChecking user enter and adult mode:")
ur.watch_video('Для чего девушкам парень-программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень-программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень-программист?')

# Проверка входа в другой аккаунт
print("\nChecking entering in to other account:")
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
print("\nTrying to play not existing video:")
ur.watch_video('Лучший язык программирования 2024 года!')
