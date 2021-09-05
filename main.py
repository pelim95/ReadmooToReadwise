from App.Service.importer import import_csv
from App.Service.requester import add_into_readwise

if __name__ == '__main__':
    highlight_jsons = import_csv('')
    add_into_readwise('tESzFyrf8605X1JnlksetlWef5yCslyEnnOhBmDRws0yREUgSB', highlight_jsons)
