import bpy

#-------------------------------------------
# This section adds in the Plane
#-------------------------------------------

# Construct a filler planar mesh with 4 vertices
bpy.ops.mesh.primitive_plane_add(size=15, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

# Set object names
for obj in bpy.context.selected_objects:
    obj.name = "theBackground"
    obj.data.name = "theBackground"

# Enter edit mode
bpy.ops.object.mode_set(mode='EDIT')

# Subdivide the selected mesh
bpy.ops.mesh.subdivide(number_cuts=3)

# Sets the object interaction mode
bpy.ops.object.mode_set(mode='OBJECT')

# Move up edge
vertexList = [15, 14, 13, 2, 3]
for idx in vertexList:
    bpy.data.objects["theBackground"].data.vertices[idx].co.z += 8

# Sets a Subdivision Surface of level 2
bpy.ops.object.subdivision_set(level=2, relative=False)

# Render and display faces shaded smooth
bpy.ops.object.shade_smooth()


#-------------------------------------------
# This section adds in the Camera
#-------------------------------------------

bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, -6, 1), rotation=(1.5708, 0, 0), scale=(1, 1, 1))

#-------------------------------------------
# This section adds in the Monkey
#-------------------------------------------

bpy.ops.mesh.primitive_monkey_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 1), scale=(1, 1, 1))

# Sets a Subdivision Surface of level 2
bpy.ops.object.subdivision_set(level=2, relative=False)

# Render and display faces shaded smooth
bpy.ops.object.shade_smooth()

#-------------------------------------------
#  Adds two lights to the scene
#-------------------------------------------

bpy.ops.object.light_add(type='AREA', radius=1, align='WORLD', location=(0.210207, 0.45328, 3.3), scale=(1, 1, 1), rotation=(0, 0, 0))
bpy.context.object.data.energy = 100

# Set light object name
for obj in bpy.context.selected_objects:
    obj.name = "KeyLight"
    obj.data.name = "KeyLight"