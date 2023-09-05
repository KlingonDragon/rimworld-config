import os
os.chdir(os.path.dirname(__file__))
work_list = []
import ui, control
def load_work_list():
    _load_list_from_file(_select_list_file())
    control.initialise()
def _select_list_file():
    options = os.listdir('./work_lists')
    while True:
        try:
            ui.cls()
            ui.h1('Select File')
            return './work_lists/{}'.format(options[int(input('{}\n\n>>> '.format('\n'.join(['{}) {}'.format(index,file) for index,file in enumerate(options)]))))])
        except:pass
def _load_list_from_file(file_name):
    global work_list
    try:
        with open(file_name) as file:work_list = [x.strip() for x in file.readlines()]
    except Exception as e:
        print('ERROR', 'Failed to load list from file', e)
