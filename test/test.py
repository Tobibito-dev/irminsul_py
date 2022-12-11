import irminsul

irminsul.change_url(irminsul.Url.API, "http://tobibito.eu.pythonanywhere.com")
irminsul.change_mode(irminsul.Mode.LOCAL, force_download=False)

print(irminsul.weapons.get_name('MistsplitterReforged'))
