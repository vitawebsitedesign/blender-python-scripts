import bpy # Imports the bpy module
from math import radians

# Creates a variable called my_cursor_location that stores the location of the 3D cursor
my_cursor_location = bpy.context.scene.cursor.location

# Creates a variable called x_cursor and stores the x location of the 3d cursor
x_cursor = my_cursor_location.x
y_cursor = my_cursor_location.y
z_cursor = my_cursor_location.z

x_rotation = radians(90)

for obj in range(10):
    # Adds a UV sphere to the scene using these arguments
    bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, align='WORLD', location=(x_cursor, y_cursor, z_cursor), rotation=(x_rotation, 0.0, 0.0), scale=(1.0, 1.0, 1.0))

    # Adds a subdivision modifier to the UV sphere
    bpy.ops.object.modifier_add(type='SUBSURF')

    # Sets the subdivision modifier levels to 2
    bpy.context.object.modifiers["Subdivision"].levels = 2

    # Shades the UV sphere smooth
    bpy.ops.object.shade_smooth()

    x_cursor += 5
    y_cursor += 5
    z_cursor += 5
