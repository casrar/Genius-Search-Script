from lyricsgenius import Genius


def main():
    genius = Genius('API TOKEN')
    page = 1

    artist_input_on = input('artist search? [y/n]: ')
    if artist_input_on == 'y':
        artist_being_searched = input('artist name: ')
    word_being_searched = input('word you want to search: ')

    if artist_input_on == 'y':
        while page:
            search = genius.search_lyrics(word_being_searched + ' ' +artist_being_searched,
                                          page=page)
            for hit in search['sections'][0]['hits']:
                song = hit['result']
                highlight = hit['highlights'][0]

                lyrics = highlight['value']
                artist = song['primary_artist']['name']
                title = song['title']
                song_id = song['id']
                occurrences = len(highlight['ranges'])

                if artist == artist_being_searched:
                    print(f"Song: {artist} - {title} | Song ID: {song_id}")
                    print(f"highlighted Lyrics: {lyrics}")
                    print(f"Occurrence: {occurrences} times")
                    print("-" * 40)
            page = search['next_page']
            print('current page: ' + str(page))

    else:
        while page:
            search = genius.search_lyrics(word_being_searched,
                                          page=page)
            for hit in search['sections'][0]['hits']:
                song = hit['result']
                highlight = hit['highlights'][0]

                lyrics = highlight['value']
                artist = song['primary_artist']['name']
                title = song['title']
                song_id = song['id']
                occurrences = len(highlight['ranges'])
                print(f"Song: {artist} - {title} | Song ID: {song_id}")
                print(f"highlighted Lyrics: {lyrics}")
                print(f"Occurrence: {occurrences} times")
                print("-" * 40)
            page = search['next_page']
            print('current page: ' + str(page))


if __name__ == "__main__":
    main()
