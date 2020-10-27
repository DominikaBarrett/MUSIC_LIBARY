"""
The main program should use functions from music_reports and display modules
"""
from file_handling import import_data,export_data
from music_reports import get_albums_by_genre, get_genre_stats,get_longest_album,get_last_oldest,get_last_oldest_of_genre,get_album_by_year,get_total_albums_length
from display import print_albums_list,print_command_result,print_program_menu,print_album_info

MENU = ['display all teh albums','get_albums_by_genre', 'get_genre_stats','get_longest_album','get_last_oldest','get_last_oldest_of_genre','get_total_albums_length','get album by year']
file_albums = import_data()
def delete_album_by_artist_and_album_name(albums, artist, album_name):
    """
    Deletes album of given name by given artist from list and updates data file

    :param list albums: currently existing albums
    :param str artist: artist who recorded the album
    :param str album_name: name of album to be deleted

    :returns: updated albums' list
    :rtype: list
    """
    result = []
    for album in albums:
        if not (artist == album[0] and album_name == album[1]):
            result.append(album)
    export_data(result)
    return result



def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """


    print_command_result('MUSIC LIBARY \n')

    while True:
        global file_albums
        global MENU
        print_command_result('Menu\n')
        print_program_menu(MENU)
        print('___________________________________________________\n')
        user_input =input('Please chose one of teh following option:')
        if user_input =='1':
            print_command_result('LIST OF ALBUMS\n')
            print_albums_list(file_albums)
        elif user_input =='2':
            genre = input('Enter a music genre: ')
            gen_albums = get_albums_by_genre(file_albums, genre)
            print_command_result('all of the file data\n')
            print_albums_list(gen_albums)
        elif user_input=='3':
            genre =input('Enter genre: \n')
            last_oldest_by_gen = get_last_oldest_of_genre(file_albums,genre)
            print_command_result('Oldest album of chosen genre:\n')
            print_album_info(last_oldest_by_gen)
        elif user_input =='4':
            longest_album = get_longest_album(file_albums)
            print_command_result('Longest album is:\n')
            print_album_info(longest_album)
        elif user_input =='5':
            lenght_f_album = get_total_albums_length(file_albums)
            print_command_result('"Total albums lenght is(float):\n"')
            print_command_result(str(lenght_f_album))
        elif user_input =='6':
            year = input("Enter choosen year: ")
            album_years = get_album_by_year(file_albums,year)
            print_command_result('Album chosen by year\n')
            print_albums_list(album_years)
        elif user_input =='7':
            last_oldest = get_last_oldest(file_albums)
            print_command_result('oldest album\n')
            print_albums_list(last_oldest)
        elif user_input =='8':
            genre_stat =get_genre_stats(file_albums)
            print_command_result('Statistic\n')
            print_album_info(genre_stat)
        elif user_input =='9':
            break
        else:
            continue








    #
    # genre = input('Enter a music genre: ')
    # file_albums = import_data()
    # # print(file_albums)
    #
    # print_albums_list(get_albums_by_genre(file_albums, genre))
    # statistic_gen = get_genre_stats(file_albums)
    # # for stat_genre in statistic:
    # print(statistic_gen)
    # longest_album = get_longest_album(file_albums)
    # print(longest_album)
    # get_last_olde = get_last_oldest(file_albums)
    # print(get_last_olde)
    # last_oldest_by_gen = get_last_oldest_of_genre(file_albums,genre)
    # print(last_oldest_by_gen)
    # get_album_by_year(file_albums,2001)
    # delete_album_by_artist_and_album_name(file_albums,'Pink Floyd','The Dark Side Of The Moon')

if __name__ == '__main__':
    main()
