# items/views.py

from django.shortcuts import render
from .riot_api import get_tier_summoner_list, get_summoner_puuid

def tier_summoner_list(request, tier='DIAMOND', division='I'):
    summoners = get_tier_summoner_list(tier, division)
    summoner_ids = [summoner['summonerId'] for summoner in summoners]
    puuids = [get_summoner_puuid(summoner_id) for summoner_id in summoner_ids]
    return render(request, 'items/tier_summoner_list.html', {'puuids': puuids})

def serve_riot_file(request):
    file_path = os.path.join('media', 'riot.txt')
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return HttpResponse(content, content_type='text/plain')
    else:
        raise Http404("File not found")
