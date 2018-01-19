import os

##print(os.getcwd())
##root, dirs, files = os.walk('.')
##print(root, dirs, files)

for root, dirs, files in os.walk('.'):
##    print(root, dirs, files)
    for filename in files:
        if filename.endswith('svg.png'):
            print(filename)
            name = filename.replace('.svg', '')
            name = name.replace('600px-', '')
            name = name.replace('800px-', '')
            name = name.replace('Flag_of_', '')
            print(name)
            os.rename(filename, name)

##os.rename('Cyprus.svg.png', 'Cyprus.png')
