import media
from media import Media
from media import my_data

def Load_For_Object():
    for i in range(len(my_data)):
        if my_data[i]['type'] == 'documentary':
            new_object = Documentary(my_data[i]['type'], my_data[i]['id'], my_data[i]['name'], my_data[i]['director'], my_data[i]['imdb'], my_data[i]['url'], my_data[i]['duration'], my_data[i]['episodes'], my_data[i]['casts'])
            doc_object.append(new_object)

doc_object = []
class Documentary(Media):
    def __init__(self, type, id, name, d, imdb, url, du, epi, c):
        Media.__init__(self, type=type, id=id, name=name, d=d, imdb=imdb, url=url, du=du, c=c)
        self.episodes = epi

    def Show_info():
        id = int(input('Please enter ID: '))
        for i in range(len(doc_object)):
            if id == doc_object[i].id:
                Media.Show_info(doc_object[i])
                break
        else:
            print("Can't find this ID !!!")

    def Search_by_name():
        name = input('Please enter name: ').lower()
        for i in range(len(doc_object)):
            if doc_object[i].name == name:
                Media.Search_by_name(doc_object[i])
                break
        
        else:
            print("Can't find this item !!!")

    def Show_list():
        for i in range(len(doc_object)):
            Media.Show_list(doc_object[i])

    def Add():
        while True:    
            id = int(input('Please enter ID :'))
            for i in range(len(doc_object)):
                if id == doc_object[i].id:
                    print('This ID already exist, Please enter another ID.')
                    break
            
            else:
                break

        name, director, imdb, url = media.get_input()
        duration = int(input('Please enter Average duration of episodes: '))
        epi = int(input('Please enter number of episodes: '))
        casts = input('Please enter casts (cast 1, cast 2, ...): ')
        casts = casts.split(',')
        new_object = Documentary('series', id, name , director, imdb, url, duration, epi, casts)
        doc_object.append(new_object)
        print('Done!')

    def Delete():
        id = int(input('Please enter ID: '))
        for i in range(len(doc_object)):
                if id == doc_object[i].id:
                    del doc_object[i]
                    print('Done!')
                    break

    def Edit():
        id = int(input('Please enter ID: '))
        for i in range(len(doc_object)):
            if id == doc_object[i].id:
                print('1- ID\n2- Name\n3- Director\n4- IMDB\n5- URL\n6- duration\n7- Casts\n8- Episodes')
                user_choice = int(input('Please choose an option: '))
                c = 1

                if user_choice == 1:
                    while True:
                        new_id = int(input('Please enter new ID: '))
                        for i in range(len(doc_object)):
                            if new_id == doc_object[i].id:
                                print('This ID already exist, Please enter another ID.')
                                break
            
                        else:
                            break

                    doc_object[i].id = new_id
                    print('Done!')
                    break

                elif 2 <= user_choice <= 7:
                    Media.Edit(doc_object[i], user_choice)
                    break
                
                elif user_choice == 8:
                    new_ep = int(input('Please enter number of episodes: '))
                    doc_object[i].episodes = new_ep
                    print('Done!')
                    break
                
                elif user_choice > 8:
                    print('Error, Index out of range')

        if c != 1:
            print("Can't find this ID !!!")

        
        else:
            print("Can't find this ID")

Load_For_Object()