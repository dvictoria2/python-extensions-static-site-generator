
@hooks.register("generate_menu")
def generate_menu(html, ext):
    template = '<li><a href="{}{}">{}</a></li>'
    menu_item = lambda name, ext: template.format(name, ext, name.title())
    menu = "\n".join([menu_item(path.stem, ext) for path in files])
    return "<ul>\n{}</ul>\n{}".format(menu, html)