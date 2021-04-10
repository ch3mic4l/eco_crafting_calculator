class TableHeaders:

    def __init__(self):
        self.headers = []
        self.position = 0
        self.line_where_headers_end = 0
        self.lookup = {
            'Crafting Station': 'crafting_station',
            'Item': 'item',
            'Materials': 'materials',
            'Level Needed': 'level_needed',
            'Crafting Time(mins)': 'crafting_time',
            'Labour Cost': 'labor_cost',
            'XP Gained': 'xp_gained'
        }
