bl_info = {
    "name": "AreaSwap",
    "description": "Hit TAB to swap Outliner/Property & Z to swap Dopesheet/Graph editor",
    "author": "Samuel Bernou, based on Cédric Lepiller and Hjalti Hjalmarsson ideas",
    "version": (1, 0, 0),
    "blender": (2, 78, 0),
    "location": "Hit TAB over outliner or property editor and Z over dopesheet or graph editor",
    "warning": "",
    "wiki_url": "",
    "category": "User Interface" }

import bpy

###---Keymap

addon_keymaps = []
def register_keymaps():
    addon = bpy.context.window_manager.keyconfigs.addon

    ######Outliner/Properties Swap
    ##from Properties to Outliner
    km = addon.keymaps.new(name = "Property Editor",space_type='PROPERTIES', region_type='WINDOW')
    kmi = km.keymap_items.new("wm.context_set_enum", type = "TAB", value = "PRESS")
    kmi.properties.data_path = 'area.type'
    kmi.properties.value = 'OUTLINER'
    addon_keymaps.append(km)
 
    ##from Outliner to Properties
    km = addon.keymaps.new(name = "Outliner",space_type='OUTLINER', region_type='WINDOW')
    kmi = km.keymap_items.new("wm.context_set_enum", type = "TAB", value = "PRESS")
    kmi.properties.data_path = 'area.type'
    kmi.properties.value = 'PROPERTIES'
    addon_keymaps.append(km)


    ######dopesheet/GraphEditor Swap
    ##from dopesheet to Graph
    km = addon.keymaps.new(name = "Dopesheet", space_type='DOPESHEET_EDITOR', region_type='WINDOW')
    kmi = km.keymap_items.new("wm.context_set_enum", type = "Z", value = "PRESS")
    kmi.properties.data_path = 'area.type'
    kmi.properties.value = 'GRAPH_EDITOR'
    addon_keymaps.append(km) 
 
    ##from Graph to dopesheet
    km = addon.keymaps.new(name = "Graph Editor",space_type='GRAPH_EDITOR', region_type='WINDOW')
    kmi = km.keymap_items.new("wm.context_set_enum", type = "Z", value = "PRESS")
    kmi.properties.data_path = 'area.type'
    kmi.properties.value = 'DOPESHEET_EDITOR'
    addon_keymaps.append(km)


def unregister_keymaps():
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        for kmi in km.keymap_items:
            km.keymap_items.remove(kmi)
        wm.keyconfigs.addon.keymaps.remove(km)
    addon_keymaps.clear()

###---Register

def register():
    if not bpy.app.background:
        register_keymaps()

def unregister():
    if not bpy.app.background:
        unregister_keymaps()

if __name__ == "__main__":
    register()
