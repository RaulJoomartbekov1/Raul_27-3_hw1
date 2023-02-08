class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def double_health_points(self):
        self.health_points *= 2

    def __str__(self):
        return f'nickname is {self.nickname}\n' \
               f'superpower is {self.superpower}\n' \
               f'health points = {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero('Р”РµР№РґР°СЂР°', 'РђРЅРёРјРµ РїРµСЂСЃРѕРЅР°Р¶', 'РІР·СЂС‹РІ', 10, 'РСЃРєСѓСЃС‚РІРѕ СЌС‚Рѕ РІР·СЂС‹РІ!')

print(f'name is {hero.get_name()}')
hero.double_health_points()
print(f'length of the catchphrase is {len(hero.catchphrase)}')
print(hero)
