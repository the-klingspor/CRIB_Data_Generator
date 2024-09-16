'''
fname = '/home/sstojanov3/Desktop/lighting_schemes/lamps.py'
exec(compile(open(fname).read(), fname, 'exec'))
'''
import bpy
import numpy as np

def delete_lamps():
	# deselect all
	bpy.ops.object.select_all(action='DESELECT')

	# selection and deletion
	for obj in bpy.data.objects:

		if obj.type == 'LAMP':
			obj.select = True
			bpy.ops.object.delete()

def make_point_lamp(location, strength = 100, temp = 5000, jitter_location = False):

	if jitter_location == True:
		location = location + np.random.uniform(-1,1,3)

	# Add point lamp
	bpy.ops.object.light_add(type='POINT', location=location, align='WORLD')
	lamp_obj = bpy.context.object

	# Set lamp properties
	lamp_obj.data.energy = strength  # Set lamp energy (brightness)

	# Use nodes
	lamp_obj.data.use_nodes = True

	# Get the node tree of the lamp
	node_tree = lamp_obj.data.node_tree

	# Clear all nodes
	nodes = node_tree.nodes
	for node in nodes:
		nodes.remove(node)

	# Add Blackbody node
	node_blackbody = nodes.new(type='ShaderNodeBlackbody')
	node_blackbody.location = (0, 200)

	# Add Emission node
	node_emission = nodes.new(type='ShaderNodeEmission')
	node_emission.location = (200, 200)

	# Add Light Output node
	node_output = nodes.new(type='ShaderNodeOutputLight')
	node_output.location = (400, 200)

	# Link nodes
	links = node_tree.links
	links.new(node_blackbody.outputs[0], node_emission.inputs[0])
	links.new(node_emission.outputs[0], node_output.inputs[0])

	# Set values
	node_blackbody.inputs[0].default_value = temp
	node_emission.inputs[1].default_value = strength

def make_area_lamp(location, size_x = 0, size_y = 0, strength = 10, temp = 5000, jitter_rotation = False):
	# Add area lamp
	bpy.ops.object.light_add(type='AREA', location=location, align='WORLD')
	lamp_obj = bpy.context.object

	# Set lamp properties
	lamp_obj.data.shape = 'RECTANGLE'
	lamp_obj.data.size = size_x
	lamp_obj.data.size_y = size_y
	lamp_obj.data.energy = strength

	# Use nodes
	lamp_obj.data.use_nodes = True

	# Get the node tree of the lamp
	node_tree = lamp_obj.data.node_tree

	# Clear all nodes
	nodes = node_tree.nodes
	for node in nodes:
		nodes.remove(node)

	# Add Blackbody node
	node_blackbody = nodes.new(type='ShaderNodeBlackbody')
	node_blackbody.location = (0, 200)

	# Add Emission node
	node_emission = nodes.new(type='ShaderNodeEmission')
	node_emission.location = (200, 200)

	# Add Light Output node
	node_output = nodes.new(type='ShaderNodeOutputLight')
	node_output.location = (400, 200)

	# Link nodes
	links = node_tree.links
	links.new(node_blackbody.outputs[0], node_emission.inputs[0])
	links.new(node_emission.outputs[0], node_output.inputs[0])

	# Set values
	node_blackbody.inputs[0].default_value = temp
	node_emission.inputs[1].default_value = strength

	if jitter_rotation == True:
		ang = np.random.uniform(-np.radians(60),np.radians(60))
		bpy.context.active_object.rotation_euler[2] = ang

# area_locations = [[0,-2.5,3],[0,0,3],[0,2.5,3]]
# point_locations = [[2.5,2.5,3],[-2.5,2.5,3],[2.5,-2.5,3],[-2.5,-2.5,3]]

# for location in point_locations:
# 	make_point_lamp(location,strength = 300, temp = 5000, jitter_location = False)

# # for location in area_locations:
# # 	make_area_lamp(location, size_x = 3, size_y = 0.1, strength =  100, temp = 5000, jitter_rotation = False)


def make_global_lighting():
	# Access the world settings
	world = bpy.context.scene.world
	world.use_nodes = True
	nodes = world.node_tree.nodes
	links = world.node_tree.links

	# Clear existing nodes
	for node in nodes:
		nodes.remove(node)

	# Create a Background node
	bg_node = nodes.new(type="ShaderNodeBackground")
	bg_node.inputs['Color'].default_value = (1, 1, 1, 1)  # White light
	bg_node.inputs['Strength'].default_value = 1.0  # Adjust light strength

	# Create World Output node
	output_node = nodes.new(type="ShaderNodeOutputWorld")

	# Link nodes
	links.new(bg_node.outputs['Background'], output_node.inputs['Surface'])