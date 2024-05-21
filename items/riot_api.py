# items/riot_api.py

import requests
import os

# 환경 변수에서 API_KEY 가져오기
API_KEY = os.getenv('RIOT_API_KEY')
REGION = 'kr'

def get_tier_summoner_list(tier, division, page=1):
    url = f'https://{REGION}.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{tier}/{division}?page={page}&api_key={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_summoner_puuid(summoner_id):
    url = f'https://{REGION}.api.riotgames.com/lol/summoner/v4/summoners/{summoner_id}?api_key={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('puuid')
    else:
        response.raise_for_status()
