# Coded by Squirrel Modeller. Spaghetti code works
# Colission extensions for Unreal Engine. Add/remove extensions in
# "exportnames" for other game engines/formats.

# Syntax:
#   foo                 (collection)
#     foo_Collision     (collection)
#       XXX_foo_XX      (object, colission)
#     foo.fbx           (object, asset)

# Select "foo" collection and run the script.

import bpy
import os

exportnames = ["UCX_", "UBX_", "UCP_", "USP_"]
tempobjects = []
name = ""

# export to blend file location
basedir = os.path.dirname(bpy.data.filepath)

if not basedir:
    raise Exception("Blend file is not saved")

view_layer = bpy.context.view_layer

obj_active = view_layer.objects.active
selection = bpy.context.view_layer.active_layer_collection


for collisioncollection in selection.collection.children_recursive:
    for obj in selection.collection.objects:
        if (obj.name == collisioncollection.name[0:-10]):
            for collisionobjects in collisioncollection.objects:
                if (collisionobjects.name[0:4] in exportnames):
                    tempobjects.append(collisionobjects)
                else:
                    print("Object \"" + collisionobjects.name +
                          "\" is not a valid collision object. Please rename the object.")

            tempobjects.append(obj)
            for exportobj in tempobjects:
                exportobj.select_set(True)

            # Settings for export
            name = bpy.path.clean_name(obj.name)
            bpy.path.clean_name(obj.name)
            fn = os.path.join(basedir, name)
            bpy.ops.export_scene.fbx(
                filepath=fn + ".fbx", use_selection=True, mesh_smooth_type='FACE')

            bpy.ops.object.select_all(action='DESELECT')
        else:
            print("The collision folder \"" + collisioncollection.name +
                  "\" is incorrectly named. The syntax should be: \"_Collision\"")
            break
    # breaks after first collection. Avoids user error of having multiple collections
    break
else:
    if (selection.name[-10::] == "_Collision"):
        print("Select the parent collection")
    else:
        print("The collection selected invalid")


# reselect the collection
bpy.context.view_layer.active_layer_collection = selection
