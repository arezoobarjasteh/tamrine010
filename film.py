import media
from media import my_data
from media import Media
def Load_For_Object():
    for i in range(len(my_data)):
        if my_data[i]['type'] == 'film':
            new_object = Film(my_data[i]['type'], my_data[i]['id'], my_data[i]['name'], my_data[i]['director'], my_data[i]['imdb'], my_data[i]['url'], my_data[i]['duration'], my_data[i]['casts'])
            film_object.append(new_object)

film_object = []
class Film(Media):
    
    def __init__(self,type=None, id=0, name=None, d=None, imdb=0, url=None, du=0, c=None):
        Media.__init__(self, type=type, id=id, name=name, d=d, imdb=imdb, url=url, du=du, c=c)
    
    def Show_info():
        id = int(input('Please enter ID: '))
        for i in range(len(film_object)):
            if id == film_object[i].id:
                Media.Show_info(film_object[i])
                break
        else:
            print("Can't find this ID !!!")

    def Search_by_name():
        name = input('Please enter name: ').lower()
        for i in range(len(film_object)):
            if film_object[i].name == name:
                Media.Search_by_name(film_object[i])
                break
        
        else:
            print("Can't find this item !!!")

    def Show_list():
        for i in range(len(film_object)):
            Media.Show_list(film_object[i])
    
    def Add():
        while True:    
            id = int(input('Please enter ID :'))
            for i in range(len(film_object)):
                if id == film_object[i].id:
                    print('This ID already exist, Please enter another ID.')
                    break
            
            else:
                break
        
        name, director, imdb, url = media.get_input()
        duration = int(input('Please enter duration: '))
        casts = input('Please enter casts (cast 1, cast 2, ...): ')
        casts = casts.split(',')
        new_object = Film('film', id, name , director, imdb, url, duration, casts)
        film_object.append(new_object)
        print('Done!')
        

    def Delete():
        id = int(input('Please enter ID: '))
        for i in range(len(film_object)):
                if id == film_object[i].id:
                    del film_object[i]
                    print('Done!')
                    break
        
        else:
            print("Can't find this ID")

    def Edit():
        
        id = int(input('Please enter ID: '))
        for i in range(len(film_object)):
            if id == film_object[i].id:
                print('1- ID\n2- Name\n3- Director\n4- IMDB\n5- URL\n6- duration\n7- Casts')
                user_choice = int(input('Please choose an option: '))
                c = 1

                if user_choice == 1:
                    while True:
                        new_id = int(input('Please enter new ID: '))
                        for i in range(len(film_object)):
                            if new_id == film_object[i].id:
                                print('This ID already exist, Please enter another ID.')
                                break
            
                        else:
                            break

                    film_object[i].id = new_id
                    print('Done!')
                    break

                elif 2 <= user_choice <= 7:
                    Media.Edit(film_object[i], user_choice)
                
                elif user_choice > 7:
                    print('Error, Index out of range')

        if c != 1:
            print("Can't find this ID !!!")
    
    def Search_by_time():
        time1 = int(input('Please enter first Time: '))
        time2 = int(input('Please enter second Time: '))
        
        c = 0
        for i in range(len(film_object)):
            if time1<= film_object[i].duration <= time2:
                c = 1
                print(f"Film {i+1}: {film_object[i].name}", end='\t')
        
        if c == 1:
            print()
            
        elif c != 1:
            print('None!')

Load_For_Object()