import config, ui
class work_list_state():
    def __init__(self, work_list_order, previous=None):
        self.order = work_list_order
        self.previous = previous if previous != None else self
    def __repr__(self) -> str:
        return '< work_list_state : {} >'.format(self.order)
    def display(self):
        ui.columns('\n'.join('{}) {}'.format(index, work) for index,work in enumerate(self.order)))
    def update(self, original_index, insert_before_index):
        original_index=int(original_index)
        insert_before_index=int(insert_before_index)
        temp_order = self.order.copy()
        temp_order.insert(insert_before_index + (0 if original_index>insert_before_index else -1), temp_order.pop(original_index))
        return work_list_state(temp_order, self)
    def generate_output(self):
        priority = 0
        new_priorities = {work_item: None for work_item in config.work_list}
        for index, work_item in enumerate(self.order):
            if config.work_list.index(work_item) < config.work_list.index(self.order[index-1]):priority+=1
            new_priorities[work_item] = priority
        ui.columns('\n'.join(['{}: {}'.format(work_item, priority) for work_item,priority in new_priorities.items()]))
            
initial_work_state=None
def initialise():
    global initial_work_state
    initial_work_state = work_list_state(config.work_list)
initialise()