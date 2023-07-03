import os
import requests
import json


def create_social_account(nickname):
    open_bracket = '{'
    close_bracket = '}'
    body = f"""
        mutation {open_bracket}
            createSocialAccount (
                nickname: "{nickname}"
            ) {open_bracket}
                success
            {close_bracket}
        {close_bracket}
        """

    response = requests.post(url=BACKEND_ENDPOINT, json={"query": body})
    data = json.loads(response.text)
    data = data['data']['success']

    return data

def create_inbox_account(discord_id, network_name):
    open_bracket = '{'
    close_bracket = '}'
    body = f"""
        mutation {open_bracket}
            createInboxAccount (
                discriminator: "{discord_id}"
                snsName: "Discord"
                networkName: "{network_name}"
            ) {open_bracket}
                success
            {close_bracket}
        {close_bracket}
        """

    response = requests.post(url=BACKEND_ENDPOINT, json={"query": body})
    data = json.loads(response.text)
    data = data['data']['success']

    return data
