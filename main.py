# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
'''
What I want my app to do:
    1. Copy playlist from Spotify to Youtube Music
    2. Copy playlist from Youtube Music to Spotify
    3. Track music that has been synced in a database
    4. Expose tracked music through api
    5. Deploy app to aws
'''
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))



def get_spotify_playlist():
    user_playlists= sp.current_user_playlists(limit= 50, offset=0)
    for playlist in user_playlists['items']:
        print(playlist['name'])




# def spotify_to_yt_music():
#
#     get_spotify_playlist()
#
#     get_songs_in_spotify_playlist()
#
#     copy_songs_to_yt_music()
#
#


def print_hi(name):

    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    get_spotify_playlist()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
