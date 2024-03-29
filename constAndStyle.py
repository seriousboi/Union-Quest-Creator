
#game constants
mapLength = 26
mapWidth = 19
itemNames = ["Door","Rock","Entity","Trap","Treasure","Annotation"] #known items
furniture = ["bookshelf","cupboard","table","chair","fireplace","desk","torture table","tomb","stairway","weapons rack"]
monsters = ["orc","goblin","skeleton","zombie","mummy","fimir","warrior","demon"]
nonMonsters = ["human","elve","dwarf"]
speciesList = monsters+nonMonsters

furnitureDims = {"bookshelf":(2,1),"cupboard":(2,1),"table":(2,1),"chair":(1,1),"fireplace":(3,1),"desk":(2,1),"torture table":(2,1),"tomb":(2,1),"stairway":(2,2),"weapons rack":(3,1)}

furnitureAmounts = {"bookshelf":2,"cupboard":1,"table":2,"chair":1,"fireplace":1,"desk":1,"torture table":1,"tomb":1,"stairway":1,"weapons rack":0}

doorTypes = ["normal","invisible","steel","ornate"]
doorColors = {"normal":(193,90,58),"invisible":(224, 252, 255),"steel":(170, 170, 170),"ornate":(255, 204, 0)}

speciesToFr = { "orc":"Orc","goblin":"Goblin","fimir":"Fimir",
                "skeleton":"Squelette","zombie":"Zombie","mummy":"Mommie",
                "warrior":"Ancient Guerrier","demon":"Démon",
                "human":"Humain","elve":"Elfe","dwarf":"Nain",
                "Unkown":"Inconnue"}

skillStats = ["strength","dexterity","constitution",
             "intelligence","perception","charisma"]

statsColors = {"strength":(252, 202, 0),"dexterity":(130, 209, 207),"constitution":(252, 3, 107),
          "intelligence":(11, 3, 252),"perception":(68, 163, 8),"charisma":(175, 2, 232),
          "health":(255, 0, 0),"stamina":(113, 227, 174)}

statsAbridged = {"strength":"STR","dexterity":"DEX","constitution":"CONST",
                 "intelligence":"INT","perception":"PER","charisma":"CHAR",
                 "health":"HP","stamina":"STAM"}

statsToFr = {"strength":"force","dexterity":"dextérité","constitution":"constitution",
             "intelligence":"intelligence","perception":"perception","charisma":"charisme",
             "health":"vie","stamina":"endurance"}

#style constants
butInCol = (215,174,129) #inside color of buttons
butOutCol = (170,115,90) #outside color of buttons
butPresInCol = (190,144,109) #inside color of pressed buttons
butPresOutCol = (170,115,90) #out color of pressed buttons

#same with another palette
but2InCol = (194,214,66)
but2OutCol = (151,163,73)
but2PresInCol = (170,200,80)
but2PresOutCol = (151,163,73)

generatorInCol = [200,200,200]
generatorOutCol = [150,150,150]
otherInCol = generatorInCol
otherOutCol = generatorOutCol

generatorOptInCol = [170,170,210]
generatorOptOutCol = [120,120,160]

nbMaxDoors = 21

nbRooms = 22
nbHallways = 54
nbRockConnectors = 58
nbDoorConnectors = 94

originalRooms = [
#big room
{"coordinates":(10,7,6,5),"color":(168,148,135)},
#topleft rooms
{"coordinates":(1,1,4,3),"color":(174,120,87)},
{"coordinates":(5,1,4,3),"color":(166,82,74)},
{"coordinates":(1,4,4,5),"color":(118,118,123)},
{"coordinates":(5,4,4,5),"color":(162,189,83)},
{"coordinates":(9,1,3,5),"color":(149,188,192)},
#topright rooms
{"coordinates":(14,1,3,5),"color":(166,61,40)},
{"coordinates":(17,1,4,4),"color":(179,185,203)},
{"coordinates":(21,1,4,4),"color":(210,172,107)},
{"coordinates":(17,5,4,4),"color":(194,143,64)},
{"coordinates":(21,5,4,4),"color":(205,210,109)},
#bottomleft rooms
{"coordinates":(1,10,4,4),"color":(225,210,127)},
{"coordinates":(1,14,4,4),"color":(160,159,191)},
{"coordinates":(5,10,2,3),"color":(192,222,232)},
{"coordinates":(7,10,2,3),"color":(124,158,150)},
{"coordinates":(5,13,4,5),"color":(188,116,103)},
{"coordinates":(9,13,3,5),"color":(180,158,102)},
#bottomright rooms
{"coordinates":(17,10,4,4),"color":(168,172,209)},
{"coordinates":(21,10,4,4),"color":(210,189,100)},
{"coordinates":(18,14,3,4),"color":(185,141,96)},
{"coordinates":(21,14,4,4),"color":(124,184,105)},
{"coordinates":(14,13,4,5) ,"color":(172,126,118)},
#must be last to be drawn properly
]

def roomDicToTuple(room):
    x = room["coordinates"][0]
    y = room["coordinates"][1]
    width =  room["coordinates"][2]
    height = room["coordinates"][3]
    weirdTuple = (x,y,width,height,room["color"])
    return weirdTuple

def tupleToRoomDic(tuple):
    return {"coordinates":(tuple[0],tuple[1],tuple[2],tuple[3]),"color":(tuple[4][0],tuple[4][1],tuple[4][2])}

hallways = [
#north central hallway
(10.5,6.5),(13,6.5),(15.5,6.5),
#south central hallway
(10.5,12.5),(13,12.5),(15.5,12.5),
#east central hallway
(16.5,7.5),(16.5,9.5),(16.5,11.5),
#west central hallway
(9.5,7.5),(9.5,9.5),(9.5,11.5),
#north vertical hallway
(13,2.5),(13,4.5),
#south vertical hallway
(13,14.5),(13,16.5),
#west horizontal hallway
(3,9.5),(5.5,9.5),(7.5,9.5),
#east horizontal hallway
(18.5,9.5),(20.5,9.5),(23,9.5),
#north horizontal hallway
(3,0.5),(5.5,0.5),(8,0.5),(10.5,0.5),(13,0.5),(15.5,0.5),(18,0.5),(20.5,0.5),(23,0.5),
#south horizontal hallway
(3,18.5),(5.5,18.5),(8,18.5),(10.5,18.5),(13,18.5),(16,18.5),(18.5 ,18.5),(20.5,18.5),(23,18.5),
#east vertical hallway
(25.5,3),(25.5,5.5),(25.5,7.5),(25.5,9.5),(25.5,11.5),(25.5,13.5),(25.5,16),
#west vertical hallway
(0.5,2.5),(0.5,5.5),(0.5,7.5),(0.5,9.5),(0.5,11.5),(0.5,13.5),(0.5,16),
]

rockConnectors = [
#north central hallway
((22,23),[(11, 6)]),((23,24),[(14,6)]),
#south central hallway
((25,26),[(11,12)]),((26,27),[(14,12)]),
#east central hallway
((28,29),[(16,8)]),((29,30),[(16,10)]),
#west central hallway
((31,32),[(9,8)]),((32,33),[(9,10)]),
#north vertical hallway
((23,35),[(12,5),(13,5)]),((35,34),[(12,3),(13,3)]),((34,48),[(12,1),(13,1)]),
#south vertical hallway
((26,36),[(12,13),(13,13)]),((36,37),[(12,15),(13,15)]),((37,57),[(12,17),(13,17)]),
#west horizontal hallway
((72,38),[(1,9)]),((38,39),[(4,9)]),((39,40),[(6,9)]),((40,32),[(8,9)]),
#east horizontal hallway
((29,41),[(17,9)]),((41,42),[(19,9)]),((42,43),[(21,9)]),((43,65),[(24,9)]),
#north horizontal hallway
((44,45),[(4,0)]),((45,46),[(6,0)]),((46,47),[(9,0)]),((47,48),[(11,0)]),((48,49),[(14,0)]),((49,50),[(16,0)]),((50,51),[(19,0)]),((51,52),[(21,0)]),
#south horizontal hallway
((53,54),[(4,18)]),((54,55),[(6,18)]),((55,56),[(9,18)]),((56,57),[(11,18)]),((57,58),[(14,18)]),((58,59),[(17,18)]),((59,60),[(19,18)]),((60,61),[(21,18)]),
#east vertical hallway
((62,63),[(25,4)]),((63,64),[(25,6)]),((64,65),[(25,8)]),((65,66),[(25,10)]),((66,67),[(25,12)]),((67,68),[(25,14)]),
#west vertical hallway
((69,70),[(0,4)]),((70,71),[(0,6)]),((71,72),[(0,8)]),((72,73),[(0,10)]),((73,74),[(0,12)]),((74,75),[(0,14)]),
#inner corners
((31,22),[(9,6)]),((24,28),[(16,6)]),((30,27),[(16,12)]),((25,33),[(9,12)]),
#outer corners
((69,44),[(0,0)]),((52,62),[(25,0)]),((68,61),[(25,18)]),((53,75),[(0,18)]),
]

doorConnectors = [
#bottomleft intern doors
((11,12),[(3,13),(3,14)]),((12,15),[(4,15),(5,15)]),((15,16),[(8,15),(9,15)]),((11,15),[(4,13),(5,13)]),((13,15),[(6,12),(6,13)]),((14,15),[(7,12),(7,13)]),((14,13),[(6,11),(7,11)]),((13,11),[(5,11),(4,11)]),
#bottomleft extern doors
((14,33),[(8,11),(9,11)]),((16,25),[(10,13),(10,12)]),((16,36),[(11,14),(12,14)]),((16,37),[(11,16),(12,16)]),((16,56),[(10,17),(10,18)]),((15,55),[(7,18),(7,17)]),((15,54),[(5,17),(5,18)]),((12,53),[(2,17),(2,18)]),((12,75),[(0,16),(1,16)]),((11,74),[(0,13),(1,13)]),((11,73),[(0,11),(1,11)]),((11,38),[(2,10),(2,9)]),((13,39),[(5,10),(5,9)]),((14,40),[(7,9),(7,10)]),
#bottomright intern doors
((21,17),[(17,13),(17,12)]),((17,18),[(20,12),(21,12)]),((18,20),[(22,13),(22,14)]),((20,19),[(20,15),(21,15)]),((19,21),[(18,15),(17,15)]),((17,19),[(19,14),(19,13)]),
#bottomright extern doors
((20,61),[(23,17),(23,18)]),((19,60),[(20,17),(20,18)]),((19,59),[(18,17),(18,18)]),((21,58),[(15,17),(15,18)]),((21,37),[(14,16),(13,16)]),((21,36),[(14,14),(13,14)]),((21,27),[(15,13),(15,12)]),((17,30),[(17,11),(16,11)]),((17,41),[(18,10),(18,9)]),((17,42),[(20,10),(20,9)]),((18,43),[(23,10),(23,9)]),((18,66),[(24,11),(25,11)]),((18,67),[(24,13),(25,13)]),((20,68),[(24,16),(25,16)]),
#topright intern doors
((6,7),[(16,3),(17,3)]),((7,8),[(20,3),(21,3)]),((8,10),[(22,4),(22,5)]),((10,9),[(20,6),(21,6)]),((9,6),[(16,5),(17,5)]),((7,9),[(19,4),(19,5)]),
#topright extern doors
((6,34),[(13,2),(14,2)]),((6,35),[(13,4),(14,4)]),((6,24),[(15,5),(15,6)]),((9,28),[(16,7),(17,7)]),((9,41),[(18,9),(18,8)]),((9,42),[(20,9),(20,8)]),((10,43),[(23,9),(23,8)]),((10,64),[(24,7),(25,7)]),((10,63),[(24,5),(25,5)]),((8,62),[(24,2),(25,2)]),((6,49),[(15,1),(15,0)]),((7,50),[(18,1),(18,0)]),((7,51),[(20,1),(20,0)]),((8,52),[(23,1),(23,0)]),
#topleft intern doors
((1,2),[(4,2),(5,2)]),((2,5),[(8,2),(9,2)]),((5,4),[(8,4),(9,4)]),((4,3),[(4,6),(5,6)]),((3,1),[(3,3),(3,4)]),((2,4),[(6,3),(6,4)]),
#topleft extern doors
((5,34),[(11,2),(12,2)]),((5,35),[(11,4),(12,4)]),((5,22),[(10,5),(10,6)]),((4,31),[(8,7),(9,7)]),((3,38),[(2,8),(2,9)]),((4,39),[(5,8),(5,9)]),((4,40),[(7,8),(7,9)]),((1,69),[(0,2),(1,2)]),((3,70),[(0,5),(1,5)]),((3,71),[(0,7),(1,7)]),((1,44),[(2,1),(2,0)]),((2,45),[(5,1),(5,0)]),((2,46),[(7,1),(7,0)]),((5,47),[(10,1),(10,0)]),
#central extern doors
((0,22),[(10,7),(10,6)]),((0,23),[(13,7),(13,6)]),((0,24),[(15,7),(15,6)]),((0,25),[(10,11),(10,12)]),((0,26),[(12,11),(12,12)]),((0,27),[(15,11),(15,12)]),((0,28),[(15,7),(16,7)]),((0,29),[(15,9),(16,9)]),((0,30),[(15,11),(16,11)]),((0,31),[(9,7),(10,7)]),((0,32),[(9,9),(10,9)]),((0,33),[(9,11),(10,11)])
]
