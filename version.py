
# Script to help Version your font file following the Hannes Method.
# It's not the most elegent solution but it has worked for me so far. 
# It will add a glyph to your font called version and increase the version count each time you run the script. It only supports through version 999

# Add the following open Type Feature to your font

# feature calt {
#    sub v period x by version;
#    } calt;


#variable to hold your initials
firstInitial = 'r'
lastInitial = 'm'

font = CurrentFont()

#creates dictionary for number word to numbers
unit = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# turn number into word -> print(unit[5])
# turn word into number -> print(unit.index('one'))

#check if there is a glyph named version.
if 'version' in font:
    print('has gylph')
    
    #sets new variable for this glyph
    version = font['version']

    #gets the current version number
    #slices to just get the number
    fullVersion = version.components[2:-2]
    #converts name to number
    versionString = ''
    for item in fullVersion:
        versionString += str(unit.index(item.baseGlyph))
        
    #update glyph with new version
    versionNum = int(versionString)
    versionNum += 1
    versionString = str(versionNum)
    
    #clears old version
    version.clearComponents()


#if not create one    
else:
    print('no glyph')
    font.newGlyph("version")

    #sets new variable for this glyph
    version = font['version']
    
    #sets version number
    versionNum = 1
    versionString = str(versionNum)
    
    #writes code to the feature (adds it to the bottom with the +=)
    font.features.text += '\nfeature calt {\n    sub v period x by version;\n } calt;' 


#gets width of most the variables
vWidth = font['v'].width
periodWidth = font['period'].width
firstDigit = int(versionString[0])
firstDigitWidth = font[unit[firstDigit]].width
firstInitialWidth = font[firstInitial].width
lastInitialRightMargin = font[lastInitial].rightMargin
shift = 0    

#add v. and first digit components
version.appendComponent('v')
shift += vWidth
version.appendComponent('period', offset=(shift,0))
shift += periodWidth
version.appendComponent(unit[firstDigit], offset=(shift,0))
shift += firstDigitWidth

#checks if version is in double digits
if 10 <= versionNum <= 99:
    #sets second variable
    secondDigit = int(versionString[1])
    #gets width of second variables
    secondDigitWidth = font[unit[secondDigit]].width
    #adds component of second digit
    version.appendComponent(unit[secondDigit], offset=(shift,0))
    shift += secondDigitWidth
    
#checks if version is triple digits
elif versionNum >= 100:
    #gets width of second & third variables
    secondDigit = int(versionString[1])
    thirdDigit = int(versionString[2])
    #gets width of all the variables
    secondDigitWidth = font[unit[secondDigit]].width
    thirdDigitWidth = font[unit[thirdDigit]].width
    #adds component of second & third digit        
    version.appendComponent(unit[secondDigit], offset=(shift,0))
    shift += secondDigitWidth
    version.appendComponent(unit[thirdDigit], offset=(shift,0))
    shift += thirdDigitWidth
    
#do nothing?
else:
    print('single digit')    
    
#add initials to the end of the component
version.appendComponent(firstInitial,  offset=(shift,0))
shift += firstInitialWidth
version.appendComponent(lastInitial,  offset=(shift,0))
shift += lastInitialRightMargin
version.rightMargin = lastInitialRightMargin

print('version.'+ versionString + firstInitial + lastInitial)