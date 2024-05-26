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
from ytmusicapi import YTMusic
ytmusic = YTMusic("oauth.json")

scope = "playlist-read-private user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))



def get_spotify_playlist():
    user_playlists= sp.current_user_playlists(limit= 50, offset=0)
    for playlist in user_playlists['items']:
        print(playlist['name'])


def get_user_tracks():
    user_tracks= sp.current_user_saved_tracks(limit= 50, offset= 0)
    song_list = []
    for track in user_tracks['items']:
        print(track['track']['name'])
        song_list.append(track['track']['name'])
    return song_list


def copy_songs_to_yt_music(playlist_name, tracks):
    playlistId = ytmusic.create_playlist(playlist_name, "test description")


    for track in tracks:
        search_results = ytmusic.search(track)
        ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])





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
    tracks= get_user_tracks()
    copy_songs_to_yt_music("liked_from_spotify", tracks)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
