import media
from media import Media
from media import my_data

def Load_For_Object():
    for i in range(len(my_data)):
        if my_data[i]['type'] == 'series':
            new_object = Series(my_data[i]['type'], my_data[i]['id'], my_data[i]['name'], my_data[i]['director'], my_data[i]['imdb'], my_data[i]['url'], my_data[i]['duration'], my_data[i]['episodes'], my_data[i]['casts'])
            series_object.append(new_object)

series_object = []
class Series(Media):
    def __init__(self, type, id, name, d, imdb, url, du, epi, c):
        Media.__init__(self, type, id, name, d, imdb, url, du, c)
        self.episodes = epi

    def Show_info():
        id = int(input('Please enter ID: '))
        for i in range(len(series_object)):
            if id == series_object[i].id:
                Media.Show_info(series_object[i])
                break
        else:
            print("Can't find this ID !!!")

    def Search_by_name():
        name = input('Please enter name: ').lower()
        for i in range(len(series_object)):
            if series_object[i].name == name:
                Media.Search_by_name(series_object[i])
                break
        
        else:
            print("Can't find this item !!!")
    
    def Show_list():
        for i in range(len(series_object)):
            Media.Show_list(series_object[i])
            

    def Add():
        while True:    
            id = int(input('Please enter ID :'))
            for i in range(len(series_object)):
                if id == series_object[i].id:
                    print('This ID already exist, Please enter another ID.')
                    break
            
            else:
                break
        
        name, director, imdb, url = media.get_input()
        duration = int(input('Please enter Average duration of episodes: '))
        epi = int(input('Please enter number of episodes: '))
        casts = input('Please enter casts (cast 1, cast 2, ...): ')
        casts = casts.split(',')
        new_object = Series('series', id, name , director, imdb, url, duration, epi, casts)
        series_object.append(new_object)
        print('Done!')
        

    def Delete():
        id = int(input('Please enter ID: '))
        for i in range(len(series_object)):
                if id == series_object[i].id:
                    del series_object[i]
                    print('Done!')
                    break
        
        else:
            print("Can't find this ID")

    def Edit():
        id = int(input('Please enter ID: '))
        for i in range(len(series_object)):
            if id == series_object[i].id:
                print('1- ID\n2- Name\n3- Director\n4- IMDB\n5- URL\n6- duration\n7- Casts\n8- Episodes')
                user_choice = int(input('Please choose an option: '))
                c = 1

                if user_choice == 1:
                    while True:
                        new_id = int(input('Please enter new ID: '))
                        for i in range(len(series_object)):
                            if new_id == series_object[i].id:
                                print('This ID already exist, Please enter another ID.')
                                break
            
                        else:
                            break

                    series_object[i].id = new_id
                    print('Done!')
                    break

                elif 2 <= user_choice <= 7:
                    Media.Edit(series_object[i], user_choice)
                    break
                
                elif user_choice == 8:
                    new_ep = int(input('Please enter number of episodes: '))
                    series_object[i].episodes = new_ep
                    print('Done!')
                    break
                
                elif user_choice > 8:
                    print('Error, Index out of range')

        if c != 1:
            print("Can't find this ID !!!")


Load_For_Object()