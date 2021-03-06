import sys
sys.path = ['/Users/Sebastian/Dropbox/_ot/code/pyprind'] + sys.path
import time
import pyprind


print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing Basic Percentage Indicator\n')

n = 100
sleeptime = 0.02

perc = pyprind.ProgPercent(n)
for i in range(n):
    time.sleep(sleeptime)
    perc.update()

print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing stdout Stream\n')

perc = pyprind.ProgPercent(n, stream=sys.stdout)
for i in range(n):
    time.sleep(sleeptime)
    perc.update()

print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing Percentage Indicator Generator\n')

for i in pyprind.prog_percent(range(n), stream=sys.stdout):
    time.sleep(sleeptime)


print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing monitor function\n')

perc = pyprind.ProgPercent(n, monitor=True)
for i in range(n):
    time.sleep(sleeptime)
    perc.update()
print(perc)


print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing Item Tracking\n')

items = ['file_%s.csv' % i for i in range(0, n)]
perc = pyprind.ProgPercent(len(items))
for i in items:
    time.sleep(sleeptime)
    perc.update(item_id=i)
