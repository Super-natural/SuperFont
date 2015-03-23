


#!/Applications/FontForge.app/Contents/Resources/opt/local/bin


#http://fontforge.github.io/python.html#Glyph
#fontforge -script convert.py "this is an excellent script" C4HeaReg.ttf

import fontforge
import sys

#gets the length of the string passed in
length = len(sys.argv[1])
curFont = fontforge.open(sys.argv[2])
newfont = fontforge.font()

for x in range(0, length):
    curFont.selection.select(sys.argv[1][x])
    curFont.copy()
    newfont.selection.select(sys.argv[1][x])
    newfont.paste()


theGlyphs = newfont.glyphs()


os.chdir(os.path.dirname(sys.argv[3]+"/"))


#print theGlyphs
newfont.fontname=sys.argv[4]+".min"
newfont.generate(sys.argv[4]+"_min.ttf")
newfont.generate(sys.argv[4]+"_min.woff")
newfont.generate(sys.argv[4]+"_min.woff2")
newfont.generate(sys.argv[4]+"_min.svg")
newfont.generate(sys.argv[4]+"_min.eot")
