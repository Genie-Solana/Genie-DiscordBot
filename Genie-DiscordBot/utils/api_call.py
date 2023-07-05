import os
import requests
import json


def check_social_account(discord_id, name, profile_img):
    if get_social_account_info(discord_id) is None:
        pub_key = create_social_account(name)
        if pub_key is None:
            return False
        if not register_sns(pub_key, discord_id, name, "Solana", profile_img):
            return False

    return True

def check_inbox_account(discord_id):
    if get_inbox_wallet_info(discord_id) is None:
        pub_key = create_inbox_account(discord_id, "Solana")
        if pub_key is None:
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
                pubKey
            {close_bracket}
        {close_bracket}
        """

    response = requests.post(url=os.environ['BACKEND_ENDPOINT'], json={"query": body})
    data = json.loads(response.text)
    
    try:
        data = data['data']['createInboxAccount']['pubKey']
    except:
        return None

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
        data = data['data']['getSocialAccountInfo']['pubKey']
    except:
        return None

    return data

def get_inbox_wallet_info(discord_id):
    open_bracket = '{'
    close_bracket = '}'
    body = f"""
        query {open_bracket}
            getUserInfo (
                discriminator: "{discord_id}"
                snsName: "Discord"
            ) {open_bracket}
                inboxList {open_bracket}
                    pubKey
                    network {open_bracket}
                        name
                    {close_bracket}
                {close_bracket}
            {close_bracket}
        {close_bracket}
        """

    response = requests.post(url=os.environ['BACKEND_ENDPOINT'], json={"query": body})
    data = json.loads(response.text)

    for inbox in data['data']['getUserInfo']['inboxList']:
        if inbox['network']['name'] == "Solana":
            return inbox['pubKey']

    return None

def register_sns(address, discord_id, handle, networkName, profile_img):
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
                profileImg: "{profile_img}"
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

