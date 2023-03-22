import time
import desktop
import os, sys
import movie_link_finder
import mshtml
from trending import top_anime
import download

directory = desktop.finddesktop()
import single
import anifo
import animehtml
import movie_series
import movie_info
import meme
info = name = frame = ''
while True:
    choice = input('''
----------------ANIMOV----------------by @jidukrishnapj on insta
    1.RESULTS FROM GOGOANIME,NETMOVIES
    2.JUST FOLLOW THE INSTRUCTION
    3.IF ERROR COMES PLZ CONTACT JIDU
    4.u can only watch anime and movie/series in option b and c
    5.if any prob in getting back just press enter key
    5.type of options are mentioned in the eg
    VERY IMP U NEED CHROME IN UR PC



    a.text meme
    b.watch movie/series
    c.watch anime
    d.Top anime
    e.Top airing (anime)
    f.Top tv series (anime)
    g.Top movies (anime)
    h.Top ova (anime)
    i.Top special (anime)
    j.Most popular (anime)
    k.Most favorite (anime)
    

    choice (eg: a):''').lower()
    print('''
    ''')
    ai = 'nop'
    if len(choice) == 1:
        if choice in 'defghijk':
            top_anime(choice)


        elif choice=='a':
            meme.ra()


        elif choice == 'b':
            try:
                type, link, dir = movie_link_finder.ms(directory)
                if type == 'series':
                    info, frame, dir, name = movie_series.mseries(link, dir)
                elif type == 'movies':
                    info, frame, dir, name = movie_info.mseries(link, dir)
                else:
                    pass
                try:
                    ai = mshtml.watch(info, frame, dir, name)
                except:
                    print('error')

                if ai == 'yes':
                    os.system('cls')
                    os.system(f'{sys.executable} {os.path.abspath(__file__)}')
                else:
                    print('that epi may be unavailable or not yet released')


            except Exception as f:
                print(f'the error happened is {f} if u can understand plz act accordingly or contact the dev')

        elif choice == 'c':
            try:
                a, epi, inf = single.single_epi()
                dow = download.donwloadsingle(a)
                inf = anifo.info(inf)
                res=animehtml.watch(a, dow, inf, epi, directory)
                if res=='yes':pass
                os.system('anime.html')
            except Exception as e:
                print(f'the error happened is {e} if u can understand plz act accordingly or contact the dev')

    q = input('enter to continue')
    print('refresh in 3 sec')
    time.sleep(3)
    os.system('cls')
