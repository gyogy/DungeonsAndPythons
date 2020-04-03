
def load_map(map_path):
    file = open(map_path, "r")
    dungeon_map = []
    dungeon_level = split_line(file.readline())

    while(dungeon_level != split_line('--Treasures\n') and dungeon_level != split_line('--Treasures')):
        if(dungeon_level == []):
            raise ValueError('Not a correct format for the txt file')
        if('\n' in dungeon_level):
            dungeon_level = dungeon_level[0:-1]
        dungeon_map.append(dungeon_level)
        dungeon_level = split_line(file.readline())
        
    file.close()
    return dungeon_map        

# Splits line from file to to list of chars 
def split_line(word):
    return [char for char in word]

def load_treasures(map_path):
    file = open(map_path, "r")
    treasures = []
    treasure = file.readline().split(', ')
    while(treasure != ['--Treasures\n']):
        #Reaching end of the file without Treasure line found
        if treasure == ['']:
            raise ValueError('Incorrect format of file(No --Treasures)')
        treasure = file.readline().split(', ')

    treasure = file.readline().split(', ')

    while(treasure != ['--Enemies\n']):
        if treasure == ['']:
            raise ValueError('Incorrect format of file(No --Enemies)')
        treasures.append(treasure)
        treasure = file.readline().split(', ')

    file.close()
    return treasures
