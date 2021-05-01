import os
import requests

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
playlist_id = input("Enter your empty Youtube playlist ID: ")

def get_client():
    """ Taken from Youtube's Data API """
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    client = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    return client


def yt_search(title_artist):
    """Searches for video using song title and artist and gets first result"""
    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=title_artist
    )
    s_response = request.execute()
    videoid = s_response[0].get("id").get("videoId")
    playlist_input(videoid, playlist_id, title_artist)

def playlist_input(playlistid, videoid, title_artist):
    """Adds to youtube playlist"""
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlistid,
                "position": 0,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": videoid
                }
            }
        }
    )
    pl_response= request.execute()
    return pl_response
