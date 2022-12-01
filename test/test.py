import irminsul

irminsul.change_url('api', "http://127.0.0.1:5000")

categories = irminsul.get_categories()
characters = irminsul.get_character_names()
albedo = irminsul.get_character('Albedo')

print(categories)
print(characters)
print(albedo.data)
