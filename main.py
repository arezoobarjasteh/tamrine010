import colorama
import media
import film
import series
import documentary
import clip
from pyfiglet import Figlet
from colorama import Fore
colorama.init(autoreset=True)


def show_menu():
    print(Fore.CYAN + "1- Add Media\n2- Show info\n3- Show List\n4- Edit Media\n5- Delete Media\n6- Search By Name\n7- Back to Menu")

def show_menu_2():
    print(Fore.CYAN + '1- Film\n2- Series\n3- Documentary\n4- Clip\n5- Download Media\n6- Save and Exit')


def Exit_Program():
    final_str = ''
    try:
        for i in range(len(film.film_object)):
            type = film.film_object[i].type
            id = film.film_object[i].id
            name = film.film_object[i].name
            director = film.film_object[i].director
            imdb = film.film_object[i].imdb
            url = film.film_object[i].url
            duration = film.film_object[i].duration
            casts = film.film_object[i].casts
        
            final_casts = ''
            for j in range(len(casts)):
                c = casts[j]
                if j == (len(casts)-1):
                    final_casts += c
                else:    
                    final_casts += c + ','

            STR = type + ',' + str(id) + ',' + name + ',' + director + ',' + str(imdb) + ',' + url + ',' + str(duration) + ',' + final_casts + '\n'
            final_str += STR
    except:
        print("Can't upload Film data, Because its empty")

    try:
        for i in range(len(series.series_object)):
            type = series.series_object[i].type
            id = str(series.series_object[i].id)
            name = series.series_object[i].name
            director = series.series_object[i].director
            imdb = str(series.series_object[i].imdb)
            url = series.series_object[i].url
            duration = str(series.series_object[i].duration)
            episodes = str(series.series_object[i].episodes)
            casts = series.series_object[i].casts
            
            final_casts = ''
            for j in range(len(casts)):
                c = casts[j]
                if j == (len(casts)-1):
                    final_casts += c
                else:    
                    final_casts += c + ','
        
            STR = type + ',' + str(id) + ',' + name + ',' + director + ',' + str(imdb) + ',' + url + ',' + str(duration) + ',' + episodes + ',' + final_casts + '\n'   
            final_str += STR
    except:
        print("Can't upload Series data, Because its empty")

    try:
        for i in range(len(documentary.doc_object)):
            type = documentary.doc_object[i].type
            id = str(documentary.doc_object[i].id)
            name = documentary.doc_object[i].name
            director = documentary.doc_object[i].director
            imdb = str(documentary.doc_object[i].imdb)
            url = documentary.doc_object[i].url
            duration = str(documentary.doc_object[i].duration)
            episodes = str(documentary.doc_object[i].episodes)
            casts = documentary.doc_object[i].casts
            
            final_casts = ''
            for j in range(len(casts)):
                c = casts[j]
                if j == (len(casts)-1):
                    final_casts += c
                else:    
                    final_casts += c + ','
        
            STR = type + ',' + str(id) + ',' + name + ',' + director + ',' + str(imdb) + ',' + url + ',' + str(duration) + ',' + episodes + ',' + final_casts + '\n' 
            final_str += STR
    except:
        print("Can't upload Documentary data, Because its empty")

    for i in range(len(clip.clip_object)):
        type = clip.clip_object[i].type
        id = str(clip.clip_object[i].id)
        name = clip.clip_object[i].name
        director = clip.clip_object[i].director
        url = clip.clip_object[i].url
        duration = str(clip.clip_object[i].duration)
    
        if i == (len(clip.clip_object)-1):
            STR = type + ',' + id + ',' + name + ',' + director + ',' + url + ',' + duration
        else:
            STR = type + ',' + id + ',' + name + ',' + director + ',' + url + ',' + duration + '\n'
    
        final_str += STR

    data_file = open('database.txt', 'w')
    data_file.write(final_str)
    data_file.close()
    exit()

f = Figlet(font='standard')
print(f.renderText('Media Info'))
while True:
    print(Fore.CYAN + '<<< Menu >>>')
    show_menu_2()
    user_choice = int(input("Please choose an option: "))

    if user_choice == 1:
        while True:
            print(Fore.CYAN + "1- Add Media\n2- Show info\n3- Show List\n4- Edit Media\n5- Delete Media\n6- Search By Name\n7- Search by Time\n8- Back to Menu")
            user_choice = int(input('Please choose an option: '))
            
            if user_choice == 1:
                film.Film.Add()

            elif user_choice == 2:
                film.Film.Show_info()

            elif user_choice == 3:
                film.Film.Show_list()

            elif user_choice == 4:
                film.Film.Edit()

            elif user_choice == 5:
                film.Film.Delete()

            elif user_choice == 6:
                film.Film.Search_by_name()

            elif user_choice == 7:
                film.Film.Search_by_time()

            elif user_choice == 8:
                break

            else:
                print("Error, Index Out of range")
    
    elif user_choice == 2:
        while True:
            show_menu()
            user_choice = int(input('Please choose an option: '))
            
            if user_choice == 1:
                series.Series.Add()

            elif user_choice == 2:
                series.Series.Show_info()

            elif user_choice == 3:
                series.Series.Show_list()

            elif user_choice == 4:
                series.Series.Edit()

            elif user_choice == 5:
                series.Series.Delete()

            elif user_choice == 6:
                series.Series.Search_by_name()
            
            elif user_choice == 7:
                break
            
            else:
                print("Error, Index Out of range")

    elif user_choice == 3:
        while True:
            show_menu()
            user_choice = int(input('Please choose an option: '))
            
            if user_choice == 1:
                documentary.Documentary.Add()

            elif user_choice == 2:
                documentary.Documentary.Show_info()

            elif user_choice == 3:
                documentary.Documentary.Show_list()

            elif user_choice == 4:
                documentary.Documentary.Edit()

            elif user_choice == 5:
                documentary.Documentary.Delete()

            elif user_choice == 6:
                documentary.Documentary.Search_by_name()

            elif user_choice == 7:
                break
            else:
                print("Error, Index Out of range")

    elif user_choice == 4:
        while True:
            show_menu()
            user_choice = int(input('Please choose an option: '))
            
            if user_choice == 1:
                clip.Clip.Add()

            elif user_choice == 2:
                clip.Clip.Show_info()

            elif user_choice == 3:
                clip.Clip.Show_list()

            elif user_choice == 4:
                clip.Clip.Edit()

            elif user_choice == 5:
                clip.Clip.Delete()

            elif user_choice == 6:
                clip.Clip.Search_by_name()

            elif user_choice == 7:
                break

            else:
                print("Error, Index Out of range")

    elif user_choice == 5:
        media.Media.Download()

    elif user_choice == 6:
        Exit_Program()

    else:
        print("Error, Index Out of range")