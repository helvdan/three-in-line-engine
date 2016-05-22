import random


def populate_map(map, map_items):
    output_map = []
    for map_row in map:
        output_row = []
        for cell in map_row:
            if cell:
                random_item = random.choice(map_items.keys())
            else:
                random_item = None
            output_row.append(random_item)
        output_map.append(output_row)

    return output_map
