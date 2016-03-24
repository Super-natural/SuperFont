 # -*- coding: utf-8 -*-


#!/Applications/FontForge.app/Contents/Resources/opt/local/bin
#http://fontforge.github.io/python.html#Glyph

# USE COMMAND:
#fontforge -script fontMinify.py _srcFonts/srcFont.ttf _outputs outputName


import fontforge
import sys
import os

curFont = fontforge.open(sys.argv[1])
newfont = fontforge.font()


outputGlypthsType = sys.argv[4]
if outputGlypthsType == "numbers":
  string = str("1234567890")
elif outputGlypthsType == "letters":
  string = str("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
else:
  string = str("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@$%^&*(/\')_-+=,.;:?1234567890"+'"'+"£"+"€"+"®"+"™"+"¢")


strLength = len(string)

for x in range(0, strLength):
    # print string[x]
    curFont.selection.select(string[x])
    curFont.copy()
    newfont.selection.select(string[x])
    newfont.paste()


theGlyphs = newfont.glyphs()

os.chdir(os.path.dirname(sys.argv[2]+"/"))


#print theGlyphs
newfont.fontname = sys.argv[3]+".min"
newfont.familyname = "SuperCustom"

newfont.generate(sys.argv[3]+"_min.ttf")
newfont.generate(sys.argv[3]+"_min.woff")
# newfont.generate(sys.argv[3]+"_min.woff2") #Doesn't seem to like this one
newfont.generate(sys.argv[3]+"_min.svg")
newfont.generate(sys.argv[3]+"_min.eot")
