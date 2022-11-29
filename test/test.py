import irminsul

irminsul.change_url('api', "http://tobibito.eu.pythonanywhere.com")

categories = irminsul.get_categories()
characters = irminsul.get_character_names()
albedo = irminsul.get_character('Albedo')

print(categories)
print(characters)
print(albedo.get_icon('side'))
