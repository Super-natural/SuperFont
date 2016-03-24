# SuperFont
A small python script that creates "minified" font files in various web-ready formats. It does this by utilising the python FontForge API found at [FontForge](http://fontforge.github.io/)

## Steps
1. Install FontForge from above link
2. Open terminal at this project
  * Ensure your src font (that which you are minifying) is in the "srcFonts" folder
3. Run this command:

  ```fontforge -script SuperFont.py _srcFonts/nameOfMyFont.otf _outputs nameOfMyOutputFont```

4. Your font should appear in the outputs folder

## Notes
* Please rename your output font after each iteration. There is an errorless overwrite issue that occasionally pops up meaning your font won't overwrite the existing font.
* The script currently includes A-Z both upper and lowercase, numbers 0-9 and most major punctuation and a few minor. For full list please view line 21 of the .py script
* If you only want certain glyphs to be output add another parameter to your command stating either `letters` or `numbers` e.g.

 ```fontforge -script SuperFont.py _srcFonts/nameOfMyFont.otf _outputs nameOfMyOutputFont numbers```
