import irminsul

irminsul.change_url(irminsul.Url.API, "http://tobibito.eu.pythonanywhere.com")
irminsul.change_mode(irminsul.Mode.CACHE)

albedo = irminsul.characters.get('Albedo')
print(albedo.get_name())
