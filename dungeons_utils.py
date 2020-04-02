
def load_map(map_path):
    file = open(map_path, "r")
    dungeon_map = []
    dungeon_level = split_line(file.readline())

    while(dungeon_level != split_line('--Treasures\n')):
        dungeon_level.remove('\n')
        dungeon_map.append(dungeon_level)
        dungeon_level = split_line(file.readline())
        

    return dungeon_map        

# Splits line from file to to list of chars 
def split_line(word):
    return [char for char in word]

def load_treasures(map_path):
    file = open(map_path, "r")
    treasures = []
    treasure = []
    while(file.readline() != '--Treasures\n'):
        pass

    treasure = file.readline().split(', ')
    while treasure != ['--Enemies']:
        treasures.append(treasure)
        treasure = file.readline().split(', ')
    
    return treasures

