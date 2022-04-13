font = AllFonts()[0] # gets the first item in all fonts and sets it to the current font
copyFont = AllFonts()[1] # gets the second font in the list
copied = CurrentFont().selectedGlyphs

#makes new glyph from selected glyphs adds .sc 
for glyph in copied:
    name = glyph.name
    # name = name + ".sc"
    newGlyph = copyFont.newGlyph(name)
    
    #copies glyphs and width from old to new
    newGlyph.appendGlyph(glyph)
    newGlyph.width = glyph.width
    
    #transforms glyph to bold width
    # midpoint = glyph.width/2
    # newGlyph.scaleBy((1.75,1), origin = (midpoint,0))
    
    #copies glyph into background layer
    layername = copyFont.layerOrder[1]
    backlayer = copyFont.getLayer(layername)
    
    bg = backlayer.insertGlyph(glyph)
    # bg.width = glyph.width
    
    
    #gets date and time
    from datetime import datetime
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M")
    print(date_time)
    
    #adds note to new glyphs with date of copy
    timestamp = "Pasted from " + font.info.familyName + " " + font.info.styleName + ", " + glyph.name + " @ " + date_time
    print(timestamp)
    newGlyph.note = timestamp
  
print("done")