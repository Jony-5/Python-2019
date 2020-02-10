#cwc 200121
from mcpi.minecraft import Minecraft
from mcpi import block    
from array import *
import random


def flowe(mc,x,y,z, total):
     done = 0
     while(done < total):
      h = random.randint(0,100)
      l = random.randint(0,100)
      mc.setBlock(x+h,y,z+l,37)
      done = done + 1


def init():
 #ipString = "192.168.1.73"
 ipString = "192.168.7.2"
 #mc = Minecraft.create("127.0.0.1", 4711)
 mc = Minecraft.create(ipString, 4711)
 mc.setting("world_immutable",False)
 #x, y, z = mc.player.getPos()  
 return mc  
numlist=[0,1,2,3,4,64,6,7,0,0,0,12,13,14,15,16,64,18,20,21,22,24,26,30,31,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,64,54,56,57,58,60,61,62,64,65,67,71,73,78,79,80,81,82,83,64,89,95,98,102,103,64
,246,247]

'''
mc.setBlocks(x,y, zz, x+4, y+4, zz, block.IRON_BLOCK.id)
mc.setBlocks(x-1,y, zz, x-1, y+4, zz+4, block.SANDSTONE .id)
mc.setBlocks(x-1,y, zz+4, x+4, y+4, zz+4, block.GOLD_ORE.id)
mc.setBlocks(x+4,y, zz+1, x+4, y+4, zz+4, block.STONE.id)
'''



def main():
     mc=flowe
     mc=init()
     x,y,z=mc.player.getPos()
     for h in range (0,100):
	     for l  in range (0,100):
		     mc.setBlocks(x+h,y, z+l, x+h,y+1,z+l,numlist[random.randint(0,len(numlist)-1)])

	     print()
     #mc.setBlocks(x-1,y-5, z-1, x+11,y-5,z+11,89)
     #mc.setBlocks(x-1,y+10, z-1, x+11,y+10,z+11,89)
     #mc.setBlocks(x-1,y+20, z-1, x+11,y+20,z+11,89)
     mc.player.setPos(x,y+20,z-10)
     
     
if __name__ == "__main__":
    main()     


#API Blocks
#====================
#   AIR                   0
#   STONE                 1
#   GRASS                 2
#   DIRT                  3
#   COBBLESTONE           4
#   WOOD_PLANKS           5
#   SAPLING               6
#   BEDROCK               7
#   WATER_FLOWING         8
#   WATER                 8
#   WATER_STATIONARY      9
#   LAVA_FLOWING         10
#   LAVA                 10
#   LAVA_STATIONARY      11
#   SAND                 12
#   GRAVEL               13
#   GOLD_ORE             14
#   IRON_ORE             15
#   COAL_ORE             16
#   WOOD                 17
#   LEAVES               18
#   GLASS                20
#   LAPIS_LAZULI_ORE     21
#   LAPIS_LAZULI_BLOCK   22
#   SANDSTONE            24
#   BED                  26
#   COBWEB               30
#   GRASS_TALL           31
#   WOOL                 35
#   FLOWER_YELLOW        37
#   FLOWER_CYAN          38
#   MUSHROOM_BROWN       39
#   MUSHROOM_RED         40
#   GOLD_BLOCK           41
#   IRON_BLOCK           42
#   STONE_SLAB_DOUBLE    43
#   STONE_SLAB           44
#   BRICK_BLOCK          45
#   TNT                  46
#   BOOKSHELF            47
#   MOSS_STONE           48
#   OBSIDIAN             49
#   TORCH                50
#   FIRE                 51
#   STAIRS_WOOD          53
#   CHEST                54
#   DIAMOND_ORE          56
#   DIAMOND_BLOCK        57
#   CRAFTING_TABLE       58
#   FARMLAND             60
#   FURNACE_INACTIVE     61
#   FURNACE_ACTIVE       62
#   DOOR_WOOD            64
#   LADDER               65
#   STAIRS_COBBLESTONE   67
#   DOOR_IRON            71
#   REDSTONE_ORE         73
#   SNOW                 78
#   ICE                  79
#   SNOW_BLOCK           80
#   CACTUS               81
#   CLAY                 82
#   SUGAR_CANE           83
#   FENCE                85
#   GLOWSTONE_BLOCK      89
#   BEDROCK_INVISIBLE    95
#   STONE_BRICK          98
#   GLASS_PANE          102
#   MELON               103
#   FENCE_GATE          107
#   GLOWING_OBSIDIAN    246
#   NETHER_REACTOR_CORE 247
