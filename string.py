# String data type


" "
' '
""" """


# concatination: +

first_name = ' Caleb'

last_name = ' Abc'
#---------------------------------------------------
time = 'at 12.35'

place = 'Moscow'

prog_language = 'python.'

text_1 = 'you are invited to our python conference that will take place in'

text = 'Hello Mr.'

text_2 = '. We will talk about programing big games with '

text_3 = 'Also we make realistic version of game Minecraft. I think that will be great!!!'

text_5 = 'With all best wishes, David.'
#---------------------------------------------------
#print('Hello' + first_name + last_name)

#                               String formatting

# f string

print(f"""{text}{first_name} {last_name}, {text_1} {place} 
{time}{text_2}{prog_language} 
{text_3}
{text_5}""")