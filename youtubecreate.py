import os
import requests

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def get_client():
    """ Taken Youtube Data API """
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

def playlist():
    """Creates youtube playlist"""
    request_body = json.dumps({
        "title": "Imported Spotify Playlist",
        "description": "Music from imported from a spotify playlist",
        "status": {
            "privacyStatus": public
        },
    })
