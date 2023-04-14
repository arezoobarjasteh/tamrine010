import pytube
from actor import Actor
def load():
    try:
        file = open('database.txt', 'r')
        file = file.read().lower()
        file = file.split('\n')
        for item in file:
            my_dict = {}
            data = item.split(',')
            if data[0] == 'film':
                my_dict['type'] = data[0]
                my_dict['id'] = int(data[1])
                my_dict['name'] = data[2]
                my_dict['director'] = data[3]
                my_dict['imdb'] = float(data[4])
                my_dict['url'] = data[5]
                my_dict['duration'] = int(data[6])
                my_dict['casts'] = data[7:]
                my_data.append(my_dict)
            
            elif data[0] == 'series':
                my_dict['type'] = data[0]
                my_dict['id'] = int(data[1])
                my_dict['name'] = data[2]
                my_dict['director'] = data[3]
                my_dict['imdb'] = float(data[4])
                my_dict['url'] = data[5]
                my_dict['duration'] = int(data[6]) 
                my_dict['episodes'] = int(data[7])
                my_dict['casts'] = data[8:]
                my_data.append(my_dict)

            elif data[0] == 'documentary':
                my_dict['type'] = data[0]
                my_dict['id'] = int(data[1])
                my_dict['name'] = data[2]
                my_dict['director'] = data[3]
                my_dict['imdb'] = float(data[4])
                my_dict['url'] = data[5]
                my_dict['duration'] = int(data[6])
                my_dict['episodes'] = int(data[7])
                my_dict['casts'] = data[8:]
                my_data.append(my_dict)

            elif data[0] == 'clip':
                my_dict['type'] = data[0]
                my_dict['id'] = int(data[1])
                my_dict['name'] = data[2]
                my_dict['director'] = data[3]
                my_dict['url'] = data[4]
                my_dict['duration'] = int(data[5])
                my_data.append(my_dict)
    except:
        print("Can't load the file")
my_data = []
load()

def get_input():
    name = input('Please enter name: ').lower()
    director = input('Please enter director: ')
    imdb = float(input('Please enter imdb score: '))
    url = input('Please enter URL link: ')
    return name, director, imdb, url

class Media:
    def __init__(self, type=None, id=0, name=None, d=None, imdb=0, url=None, du=0, c=None):
        self.type = type
        self.id = id
        self.name = name
        self.director = d        
        self.url = url
        self.duration = du
        if type == 'film' or type == 'series' or type == 'documentary':
            self.imdb = imdb
            cast = Actor(c)
            casts = cast.Actor_List()
            self.casts = casts

    def Download():
        link = input('pls enter URL link from Youtube: ')
        print('Please Wait ...')
        first_stream = pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./', filename='MyFile.mp4')
        print('Done!')
    
    def Show_info(self):
        if self.type == 'film':
            print(f"Type:{self.type}\nID:{self.id}\nName:{self.name}\nDirector:{self.director}\nImdb score:{self.imdb}\nURL link: {self.url}\nDuration:{self.duration} Min\nCasts:{self.casts}")

        elif self.type == 'series' or self.type == 'documentary':
            print(f"Type:{self.type}\nID:{self.id}\nName:{self.name}\nDirector:{self.director}\nImdb score:{self.imdb}\nURL link: {self.url}\nAverage duration of episodes:{self.duration} Min\nEpisodes:{self.episodes}\nCasts:{self.casts}")

        elif self.type == 'clip':
            print(f"Type:{self.type}\nID:{self.id}\nName:{self.name}\nDirector:{self.director}\nURL link: {self.url}\nDuration:{self.duration} Min")


    def Search_by_name(self):
        if self.type == 'film':
            print(f"Type:{self.type}\nID:{self.id}\nName:{self.name}\nDirector:{self.director}\nImdb score:{self.imdb}\nURL link: {self.url}\nDuration:{self.duration} Min\nCasts:{self.casts}")        

        elif self.type == 'series' or self.type == 'documentary':
            print(f"Type:{self.type}\nID:{self.id}\nName:{self.name}\nDirector:{self.director}\nImdb score:{self.imdb}\nURL link: {self.url}\nAverage duration of episodes:{self.duration} Min\nEpisodes:{self.episodes}\nCasts:{self.casts}")
        
        elif self.type == 'clip':
            print(f"Type:{self.type}\nID:{self.id}\nName:{self.name}\nDirector:{self.director}\nURL link: {self.url}\nDuration:{self.duration} Min")


    def Show_list(self):
        if self.type == 'film' or self.type == 'series' or self.type == 'documentary':
            print(f"Type:{self.type}, Name:{self.name}, Director:{self.director}, Imdb score:{self.imdb}, URL link: {self.url}")
        
        elif self.type == 'clip':
            print(f"Type:{self.type}, Name:{self.name}, URL link: {self.url}, Duration:{self.duration} Min")


        else:
            pass
    
    def Edit(self, user_choice):
        if self.type == 'clip' and user_choice == 4 or user_choice == 5:
            user_choice += 1

        if user_choice == 2:
            new_name = input('Please enter new name: ').lower()
            self.name = new_name
            print('Done!')

        elif user_choice == 3:
            new_di = input('Please enter new director: ')
            self.director = new_di
            print('Done!')

        elif user_choice == 4:
            new_imdb = float(input('Please enter IMDB score: '))
            self.imdb = new_imdb
            print('Done!')

        elif user_choice == 5:
            url = input('Please enter URL link: ')
            self.url = url
            print('Done!')

        elif user_choice == 6:
            du = int(input('Please enter duration: '))
            self.duration = du
            print('Done!')

        elif user_choice == 7:
            casts = input('Please enter casts (cast 1, cast 2, ...): ')
            casts = casts.split(',')
            self.casts = casts
            print('Done!')