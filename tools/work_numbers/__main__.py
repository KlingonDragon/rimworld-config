import config, control, ui
if __name__ =='__main__':
    ui.cls()
    config.load_work_list()
    active = control.initial_work_state
    action = None
    ui.cls()
    while True:
        ui.h1('Configure your new work list')
        # Do after Header
        if action =='3':active.generate_output()
        ###
        ui.h2('Current Order')
        active.display()
        ui.h2('Options')
        action = input('1) Move Work Item\n2) Undo\n3) Output Current Priorities\n0) Finish\n>>> ')
        # Do Before Clear
        try:
            if action =='1':
                original_index = input('Select an index to move\n>>>')
                insert_before_index = input('Select the index to insert before\n>>>')
                active = active.update(original_index, insert_before_index)
        except:pass
        ###
        ui.cls()
        # Do after clear
        if action =='0':break
        if action =='2':active = active.previous
        if action =='7': # Secret testing option
            active = control.work_list_state([
'Fire', 'Patient', 'Doctor', 'Nurse', 'Urgent', 'Rest', 'Haul+', 'Care', 'Basic', 'Rearm', 'Repair', 'Nuclear', 'Warden', 'Jailor', 'Harvest', 'Sow', 'Cut', 'Cook', 'Butcher', 'Surgeon', 'Handle', 'Train', 'Tame', 'Hunt', 'Load', 'Mortify', 'Deliver', 'Haul', 'Build', 'Demo', 'Mine', 'Drill', 'Refine', 'Clean', 'Tailor', 'Tech', 'Smith', 'Stone', 'Smelt', 'Entertain', 'Brew', 'Fabricate', 'Drug', 'Craft', 'Scan', 'Art', 'Fish'
            ],active)
        ###
    active.generate_output()