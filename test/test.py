import irminsul

irminsul.change_url(irminsul.Url.API, "http://tobibito.eu.pythonanywhere.com")
irminsul.change_mode(irminsul.Mode.CACHE)

chars = irminsul.characters.get_names()

characters_local = []
for name in chars:
    char = irminsul.characters.get(name)
    characters_local.append(char)

print(characters_local)
