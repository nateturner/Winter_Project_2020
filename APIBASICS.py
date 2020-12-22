from riotwatcher import LolWatcher, ApiError

# golbal variables
api_key = 'RGAPI-23dbfb58-88f4-436a-a30e-818fe71f0f77'
watcher = LolWatcher(api_key)
my_region = 'na1'

me = watcher.summoner.by_name(my_region, 'Rad Radius')
print("ACCOUNT DATA")
for line in me:
    print(str(line) + ': ' + str(me[line]))
print()
my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
print("RANKED DATA")
for line in my_ranked_stats[0]:
    print(str(line) + ': ' + str(my_ranked_stats[0][line]))