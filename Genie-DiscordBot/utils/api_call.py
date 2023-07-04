import os
import requests
import json


def check_social_account(discord_id, name):
    if get_social_account_info(discord_id) is None:
        pub_key = create_social_account(name)
        if pub_key is None:
            return False
        if not register_sns(pub_key, discord_id, name, "Solana"):
            return False

    return True

def create_social_account(nickname):
    open_bracket = '{'
    close_bracket = '}'
    body = f"""
        mutation {open_bracket}
            createSocialAccount (
                nickname: "{nickname}"
            ) {open_bracket}
                success
                pubKey
            {close_bracket}
        {close_bracket}
        """
    response = requests.post(url=os.environ['BACKEND_ENDPOINT'], json={"query": body})
    data = json.loads(response.text)
    
    try:
        data = data['data']['createSocialAccount']['pubKey']
    except:
        return None

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

    response = requests.post(url=os.environ['BACKEND_ENDPOINT'], json={"query": body})
    data = json.loads(response.text)
    data = data['data']['success']

    return data

def get_social_account_info(discord_id):
    open_bracket = '{'
    close_bracket = '}'
    body = f"""
        query {open_bracket}
            getSocialAccountInfo (
                discriminator: "{discord_id}"
                snsName: "Discord"
            ) {open_bracket}
                pubKey
                nickname
            {close_bracket}
        {close_bracket}
        """

    response = requests.post(url=os.environ['BACKEND_ENDPOINT'], json={"query": body})
    data = json.loads(response.text)
    try:
        data = data['getSocialAccountInfo']['pubKey']
    except:
        return None

    return data

def register_sns(address, discord_id, handle, networkName):
    open_bracket = '{'
    close_bracket = '}'
    body = f"""
        mutation {open_bracket}
            registerSns (
                address: "{address}"
                snsName: "Discord"
                handle: "{handle}"
                discriminator: "{discord_id}"
                networkName: "{networkName}"
            ) {open_bracket}
                success
            {close_bracket}
        {close_bracket}
        """
    response = requests.post(url=os.environ['BACKEND_ENDPOINT'], json={"query": body})
    data = json.loads(response.text)
    try:
        data = data['data']['registerSns']['success']
    except:
        return False
    return data

