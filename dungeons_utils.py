
def load_map(map_path):
    file = open(map_path, "r")
    dungeon_map = []
    dungeon_level = split_line(file.readline())

    while(dungeon_level != split_line('--Treasures\n') and dungeon_level != split_line('--Treasures')):
        if(dungeon_level == []):
            file.close()
            raise ValueError('Not a correct format for the txt file')
        if('\n' in dungeon_level):
            dungeon_level = dungeon_level[0:-1]
        dungeon_map.append(dungeon_level)
        dungeon_level = split_line(file.readline())

    file.close()
    if check_if_dungeon_map_has_forbidden_symbols(dungeon_map):
        return dungeon_map


def check_if_dungeon_map_has_forbidden_symbols(dungeon_map):
    forbidden_symbols = ['.', '#', 'E', 'H', 'T', 'G', 'S', 'R']
    for level in dungeon_map:
        for square in level:
            if square not in forbidden_symbols:
                raise ValueError('Invalid character on the map')

    return True


# Splits line from file to to list of chars
def split_line(word):
    return [char for char in word]


def load_treasures(map_path):
    file = open(map_path, "r")
    treasures = []
    treasure = file.readline().split(', ')
    while(treasure != ['--Treasures\n']):
        # Reaching end of the file without Treasure line found
        if treasure == ['']:
            file.close()
            raise ValueError('Incorrect format of file(No --Treasures)')
        treasure = file.readline().split(', ')

    treasure = file.readline().split(', ')

    while(treasure != ['--Enemies\n']):
        if treasure == ['']:
            file.close()
            raise ValueError('Incorrect format of file(No --Enemies)')
        treasures.append(treasure)
        treasure = file.readline().split(', ')

    file.close()
    return treasures


def load_enemies(map_path):
    file = open(map_path, 'r')
    enemies = []
    enemy = file.readline().split(', ')

    while(enemy != ['--Enemies\n']):
        # Reaching end of the file without Enemies line found
        if enemy == ['']:
            file.close()
            raise ValueError('Incorrect format of file (No --Enemies)')
        enemy = file.readline().split(', ')

    enemy = file.readline().split(', ')

    while(enemy != ['--EOG\n'] and enemy != ['--EOG']):
        if enemy == ['']:
            file.close()
            raise ValueError('Incorrect format of file (No --EOG)')
        enemies.append(enemy)
        enemy = file.readline().split(', ')

    file.close()
    return enemies
