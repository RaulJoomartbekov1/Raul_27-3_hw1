GeekTech = {
    'addres':'Tokyogula 175',
    'courses':['Android','Backend','Frontend'],
    'bag':{'fails','errors','stack'}
}
del GeekTech['bag']
GeekTech['instagramm'] = 'geektech_edu'
GeekTech['number phone'] = '0770001234'
GeekTech['address'] = 'ibraimova 103'
GeekTech['courses'].insert(1, 'UX_UI')
GeekTech['courses'] = set(GeekTech['courses'])
GeekTech['date'] = '07.05.2018'
print(f"curses count - {len(GeekTech['courses'])}")
for key, value in GeekTech.items():
    print(f'{key}: {value}')
print(GeekTech)