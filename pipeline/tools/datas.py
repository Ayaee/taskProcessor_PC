import glob


def getFiles():
    hardcodedPath = 'G:/Artfx/TD4/WS_MicroFilm/MOVIE/ASSETS'
    files = glob.glob(hardcodedPath + "/*/*/*/*.*")
    return files


#Test
if __name__ == '__main__':
    for f in getFiles():
        print(f)