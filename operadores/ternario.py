lockdown = True
grana = 30

status = 'Em casa' if lockdown or grana <= 100 else'Uhuuuu' # Se e caso ao contrátrio

print (f'O status é: {status}')
