bl_info = {
    "name": "TapTapSwap",
    "description": "add some usefull swapping shortcut",
    "author": "Samuel Bernou, based on Cédric Lepiller/Hjalti Hjalmarsson/my ideas ;)",
    "version": (1, 5, 0),
    "blender": (2, 78, 0),
    "location": "Hit TAB swap outliner/property editor, Z swap dopesheet/graph editor, shift+Z in timeline, ctrl+shift+alt+X swap active object's properties tabs from anywhere",
    "warning": "",
    "wiki_url": "",
    "category": "User Interface" }

import bpy


C = bpy.context
D = bpy.data

def set_panel(panel):
    '''take a panel name and apply it to properties zone'''
    for area in bpy.context.screen.areas:
        if area.type == 'PROPERTIES':
            for space in area.spaces:
                if space.type == 'PROPERTIES':
                    space.context = panel
                    return (1)
    return (0)


def get_panel():
    '''return active panel name of the properties zone'''
    for area in bpy.context.screen.areas:
        if area.type == 'PROPERTIES':
            for space in area.spaces:
                if space.type == 'PROPERTIES':
                    return(space.context)
    return (0)


def bone_has_physics(ob):
    if ob.rigid_body or ob.rigid_body_constraint:
        return (1)
    else:
        return (0)

def has_physics(ob):
    if ob.rigid_body or ob.rigid_body_constraint:
        # print ('rigid_body or ob.rigid_body_constraint')#Dbg#
        return (1)
    if ob.type == 'MESH' and ob.collision.use:
        # print ('collision')#Dbg#
        return (1)
    if has_mod(ob):
        # print ('has_modifier')#Dbg#
        for m in ob.modifiers:
            if m.type in ['CLOTH', 'SOFT_BODY', 'FLUID_SIMULATION', 'DYNAMIC_PAINT', 'SMOKE']:
                return(1)
    return (0)

def has_mod(ob):
    return(len(ob.modifiers))

def has_const(ob):
    return(len(ob.constraints))

def has_mat(ob):
    return(len(ob.material_slots))

def has_particles(ob):
    return(len(ob.particle_systems))


def Swap_properties_panel():
    #check  for an active object
    obj = bpy.context.object
    if not obj:
        return (1, 'must select an active object')

    pan = get_panel()
    if not pan:
        return (1, '"properties" region must be visible on screen')

    DicObjects = {
    'MESH': ['DATA','MATERIAL','PARTICLES','PHYSICS', 'OBJECT','CONSTRAINT', 'MODIFIER',],
    'CURVE' : ['DATA','MATERIAL','OBJECT','CONSTRAINT','MODIFIER',],
    'EMPTY': ['DATA','PHYSICS', 'OBJECT','CONSTRAINT',],
    'ARMATURE': ['DATA', 'BONE','BONE_CONSTRAINT', 'PHYSICS', 'OBJECT','CONSTRAINT',],
    'CAMERA' : ['DATA','OBJECT','CONSTRAINT',],
    'LATTICE' : ['DATA','OBJECT','CONSTRAINT','MODIFIER',],
    'LAMP' : ['DATA','PHYSICS','OBJECT','CONSTRAINT',],
    'FONT' : ['DATA','MATERIAL','PHYSICS','OBJECT','CONSTRAINT', 'MODIFIER',],
    }

    tp = obj.type

    props = DicObjects[tp]
    # print(props)#Dbg#

    #actualize props list to keep only available
    for p in list(props):
        if p == 'PARTICLES' and not has_particles(obj):
            props.remove(p)
        if p == 'MODIFIER' and not has_mod(obj):
            props.remove(p)
        if p == 'MATERIAL' and not has_mat(obj):
            props.remove(p)
        if p == 'CONSTRAINT' and not has_const(obj):
            props.remove(p)
        if p == 'PHYSICS' and not has_physics(obj):
            props.remove(p)

    print (props, 'availables panels')#Dbg#


    if pan in props:
        nextpan = props[(props.index(pan)+1)%len(props)]
    else:
        nextpan = props[0]

    set_panel(nextpan)
    return(0,'')


class Swap_panel_prop(bpy.types.Operator):
    bl_idname = "samtools.swap_panel_prop"
    bl_label = "Swap panel properties"
    bl_description = "Swap panel on properties"
    bl_options = {"REGISTER"}

    C = bpy.context
    D = bpy.data

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        Swap_properties_panel()
        return {"FINISHED"}


###--KEYMAPS
addon_keymaps = []
def register_keymaps():
    addon = bpy.context.window_manager.keyconfigs.addon

    addon_keymaps.append(km)


###---Keymap

addon_keymaps = []
def register_keymaps():
    addon = bpy.context.window_manager.keyconfigs.addon

    ######--object property swap
    ##view3Donly:
    # km = addon.keymaps.new(name = "3D View", space_type = "VIEW_3D")
    ##all view:
    km = addon.keymaps.new(name = "Window",space_type='EMPTY', region_type='WINDOW')
    ##ctrl+shift+X taken by carver ! so add alt
    kmi = km.keymap_items.new("samtools.swap_panel_prop", type = "X", value = "PRESS", shift = True, ctrl = True, alt=True)

    #-#-#-#-- keymap only (zone)
    ######Outliner/Properties Swap
    ##from Properties to Outliner - Tab
    km = addon.keymaps.new(name = "Property Editor",space_type='PROPERTIES', region_type='WINDOW')
    kmi = km.keymap_items.new("wm.context_set_enum", type = "TAB", value = "PRESS")
    kmi.properties.data_path = 'area.type'
    kmi.properties.value = 'OUTLINER'
    addon_keymaps.append(km)

    ##from Outliner to Properties - Tab
    km = addon.keymaps.new(name = "Outliner",space_type='OUTLINER', region_type='WINDOW')
    kmi = km.keymap_items.new("wm.context_set_enum", type = "TAB", value = "PRESS")
    kmi.properties.data_path = 'area.type'
    kmi.properties.value = 'PROPERTIES'
    addon_keymaps.append(km)


    ######dopesheet/GraphEditor Swap - Z
    ##from dopesheet to Graph
    km = addon.keymaps.new(name = "Dopesheet", space_type='DOPESHEET_EDITOR', region_type='WINDOW')
    kmi = km.keymap_items.new("wm.context_set_enum", type = "Z", value = "PRESS")
    kmi.properties.data_path = 'area.type'
    kmi.properties.value = 'GRAPH_EDITOR'
    addon_keymaps.append(km)

    ##from Graph to dopesheet - Z
    km = addon.keymaps.new(name = "Graph Editor",space_type='GRAPH_EDITOR', region_type='WINDOW')
    kmi = km.keymap_items.new("wm.context_set_enum", type = "Z", value = "PRESS")
    kmi.properties.data_path = 'area.type'
    kmi.properties.value = 'DOPESHEET_EDITOR'
    addon_keymaps.append(km)

    ######dopesheet/Timeline Swap
    ##from timeline to dopesheet - shift Z
    km = addon.keymaps.new(name = "Timeline", space_type='TIMELINE', region_type='WINDOW')
    kmi = km.keymap_items.new("wm.context_set_enum", type = "Z", value = "PRESS", shift = True)
    kmi.properties.data_path = 'area.type'
    kmi.properties.value = 'DOPESHEET_EDITOR'
    addon_keymaps.append(km)

    ##from dopesheet to timeline - shift Z
    km = addon.keymaps.new(name = "Dopesheet",space_type='DOPESHEET_EDITOR', region_type='WINDOW')
    kmi = km.keymap_items.new("wm.context_set_enum", type = "Z", value = "PRESS", shift = True)
    kmi.properties.data_path = 'area.type'
    kmi.properties.value = 'TIMELINE'
    addon_keymaps.append(km)



def unregister_keymaps():
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        for kmi in km.keymap_items:
            km.keymap_items.remove(kmi)
        wm.keyconfigs.addon.keymaps.remove(km)
    addon_keymaps.clear()


###--REGISTER
def register():
    if not bpy.app.background:
        bpy.utils.register_module(__name__)
        register_keymaps()

def unregister():
    if not bpy.app.background:
        unregister_keymaps()
        bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
