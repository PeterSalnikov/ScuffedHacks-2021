import os
import requests

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd
import time

scopes = ["https://www.googleapis.com/auth/youtube"]


# def get_client():
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
    # return client

def yt_search(playlist_id,title_artist):
    """Searches for video using song title and artist and gets first result"""
    request = client.search().list(
        part="snippet",
        maxResults=1,
        q=title_artist
    )
    response = request.execute()
    videoid = response["items"][0]["id"]["videoId"]
    playlist_input(playlist_id,videoid)


def playlist_input(playlistid, videoid):
    """Adds to youtube playlist"""
    request = client.playlistItems().insert(
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
    request.execute()




if __name__ == "__main__":
    playlist_id = input("Enter your empty Youtube playlist ID: ")

    df = pd.read_csv('track_list.csv')

    for index, row in df.iterrows():
        yt_search(playlist_id, row['tracks'])
        time.sleep(2)