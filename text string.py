size(1080, 1920)
font = CurrentFont()

t = FormattedString()
# set a font
t.font('Pau Hana')
# set a font size
t.fontSize(72)

#add glyphs to string t in order
for glyphName in font.glyphOrder:
    t.appendGlyph(glyphName)

#create textbox with string
textBox(t, (100, 100, 880, 1720))