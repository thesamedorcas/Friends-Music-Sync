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


def get_spotify_playlists():
    '''
    It returns the list of a user's playlist and the playlist id
    '''
    playlist_name_id_pair = []
    user_playlists = sp.current_user_playlists(limit=50, offset=0)
    for playlist in user_playlists['items']:

        playlist_name_id_pair.append(
            {
                "name": playlist['name'],
                "playlist_id": playlist["id"]
            }
        )
    return playlist_name_id_pair


def get_user_liked_tracks():
    '''
    returns an array of current user liked songs
    '''
    user_tracks = sp.current_user_saved_tracks(limit=50, offset=0)
    song_list = []
    for track in user_tracks['items']:
        song_list.append(track['track']['name'])
    return song_list


def copy_songs_to_yt_music(playlist_name, tracks):
    '''
    copies the songs in a playlist in youtube music
    '''
    playlistId = ytmusic.create_playlist(playlist_name, "test description")
    for track in tracks:
        search_results = ytmusic.search(track)
        if not search_results or not "videoId" in search_results[0]:
            continue
        ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])


def get_tracks_from_playlist(playlist_id):
    '''
    returns songs in a playlist
    '''
    tracks_in_playlist = []
    playlist_tracks = sp.playlist_items(playlist_id=playlist_id)
    for track in playlist_tracks["items"]:
        tracks_in_playlist.append(track["track"]["name"])
    return tracks_in_playlist


if __name__ == '__main__':

    # move liked spotify tracks to yt music

    # step 1: get liked songs from spotify
    liked_tracks = get_user_liked_tracks()
    # step 2: copy over songs to yt music
    copy_songs_to_yt_music("liked_from_spotify", liked_tracks)

    # move spotify playlists to yt music

    # step 1: get playlists from spotify
    user_playlists = get_spotify_playlists()
    # step 2: get tracks from each playlist
    for playlist in user_playlists:
        name, playlist_id = playlist["name"], playlist["playlist_id"]
        # step 3: get tracks for each playlist
        songs_in_playlist = get_tracks_from_playlist(playlist_id)
        # step 4: copy songs to yt music
        copy_songs_to_yt_music(name, songs_in_playlist)


    print("completed migration from spotify to youtube")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
