import adsk.core, adsk.fusion

# Match color properties by id: names are localized (e.g. "색상" in Korean Fusion).
COLOR_PROPERTY_IDS = ("opaque_albedo", "metal_f0", "generic_diffuse", "layered_diffuse", "transparent_color",
                      "glazing_transmission_color")
DEFAULT_MATERIAL = ("silver", "0.700 0.700 0.700 1.000")


def material(com_name):
    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)
    for occs in design.rootComponent.occurrences:
        if occs.component.name != com_name:
            continue
        appearance = occs.component.material.appearance
        for prop in appearance.appearanceProperties:
            if prop.id not in COLOR_PROPERTY_IDS:
                continue
            val = adsk.core.ColorProperty.cast(prop).value
            if val:
                color = f"{round(val.red/255,3)} {round(val.green/255,3)} {round(val.blue/255,3)} {round(val.opacity/255,3)}"
                return appearance.name, color
    return DEFAULT_MATERIAL
