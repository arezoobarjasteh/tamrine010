from media import my_data
from media import Media

def Load_For_Object():
    for i in range(len(my_data)):
        if my_data[i]['type'] == 'clip':
            new_object = Clip(my_data[i]['type'], my_data[i]['id'], my_data[i]['name'], my_data[i]['director'], my_data[i]['url'], my_data[i]['duration'])
            clip_object.append(new_object)

clip_object = []
class Clip(Media):
    def __init__(self, type, id, name, d, url, du):
        Media.__init__(self, type=type, id=id, name=name, d=d, url=url, du=du)

    def Show_info():
        id = int(input('Please enter ID: '))
        for i in range(len(clip_object)):
            if id == clip_object[i].id:
                Media.Show_info(clip_object[i])
                break
        else:
            print("Can't find this ID !!!")

    def Search_by_name():
        name = input('Please enter name: ').lower()
        for i in range(len(clip_object)):
            if clip_object[i].name == name:
                Media.Search_by_name(clip_object[i])
                break
        
        else:
            print("Can't find this item !!!")

    def Show_list():
        for i in range(len(clip_object)):
            Media.Show_list(clip_object[i])

    def Add():
        while True:    
            id = int(input('Please enter ID :'))
            for i in range(len(clip_object)):
                if id == clip_object[i].id:
                    print('This ID already exist, Please enter another ID.')
                    break
            
            else:
                break
        
        name = input('Please enter name: ').lower()
        director = input('Please enter director: ')
        url = input('Please enter URL link: ')
        duration = int(input('Please enter duration: '))
        new_object = Clip('clip', id, name , director, url, duration)
        clip_object.append(new_object)
        print('Done!')
    
    def Delete():
        id = int(input('Please enter ID: '))
        for i in range(len(clip_object)):
                if id == clip_object[i].id:
                    del clip_object[i]
                    print('Done!')
                    break
        
        else:
            print("Can't find this ID")

    def Edit():
        
        id = int(input('Please enter ID: '))
        for i in range(len(clip_object)):
            if id == clip_object[i].id:
                print('1- ID\n2- Name\n3- Director\n4- URL\n5- duration')
                user_choice = int(input('Please choose an option: '))
                c = 1

                if user_choice == 1:
                    while True:
                        new_id = int(input('Please enter new ID: '))
                        for i in range(len(clip_object)):
                            if new_id == clip_object[i].id:
                                print('This ID already exist, Please enter another ID.')
                                break
            
                        else:
                            break

                    clip_object[i].id = new_id
                    print('Done!')
                    break

                elif 2 <= user_choice <= 5:
                    Media.Edit(clip_object[i], user_choice)
                
                elif user_choice > 5:
                    print('Error, Index out of range')

        if c != 1:
            print("Can't find this ID !!!")

Load_For_Object()