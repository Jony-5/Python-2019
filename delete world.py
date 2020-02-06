from mcpi.minecraft import Minecraft
from mcpi import block 

mc = Minecraft.create("127.0.0.1", 4711)
mc.setting("world_immutable", False)
x, y, z = mc.player.getPos()  



mc.setBlocks(x+140,y+140,z+140,x-140,y-140,z-140, 0)
