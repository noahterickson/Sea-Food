import configparser

import json
import spotipy
import spotipy.oauth2 as oauth2

def main():
    config = configparser.ConfigParser()
    config.read('config.cfg')
    client_id = config.get('SPOTIFY', 'CLIENT_ID')
    client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')


    auth = oauth2.SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )

    token = auth.get_access_token()
    spotify = spotipy.Spotify(auth=token)

    caviar_uri = "spotify:user:spotify:playlist:37i9dQZF1DX0XUsuxWHRQd"
    results = spotify.user_playlist_tracks("Spotify",caviar_uri)
    
    with open('20181202.json', 'w') as outfile:
        json.dump(results, outfile, indent=4)

if __name__ == "__main__":
    main()