arrow_base_height = int(input('Enter arrow base height:\n'))

arrow_base_width = int(input('Enter arrow base width:\n'))

arrow_head_width = int(input('Enter arrow head width:\n'))



'''print('')
# Draw arrow base (height = 3, width = 2)
print ('**')
print ('**')
print ('**')

# Draw arrow head (width = 4)
print ('****')
print ('***')
print ('**')
print ('*')'''



while arrow_head_width <= arrow_base_width:
    arrow_head_width= int(input('''Enter arrow head width:
'''))
print("")



for index in range (arrow_base_height):
    index= ('*' * arrow_base_width)
    print(index)



for z in range(arrow_head_width):
    z= ('*' * arrow_head_width)
    print(z)
    arrow_head_width= arrow_head_width-1







