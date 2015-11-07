import pygame 
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (  #Diffrent Nodes for vertices given in three dimensional coordinates
	(1, -1, -1),
	(1, 1, -1),
	(-1, 1, -1),
	(-1, -1, -1),
	(1, -1, 1),
	(1, 1, 1),
	(-1, -1, 1),
	(-1, 1, 1)
	)

edges = ( #Nodes for the twelve edges of the cube to be rendered
	(0, 1),
	(0, 3),
	(0, 4),
	(2, 1),
	(2, 3),
	(2, 7),
	(6, 3),
	(6, 4),
	(6, 7),
	(5, 1),
	(5, 4),
	(5, 7)
	)

surfaces = ( #Nodes for the various surfaces to be rendered
	(0, 1, 2, 3),
	(3, 2, 7, 6),
	(6, 7, 5, 4),
	(4, 5, 1, 0),
	(1, 5, 7, 2),
	(4, 0, 3, 6)
	)

colors = ( #Sets a list of colors
	(1, 0, 0),
	(0, 1, 0),
	(0, 0, 1),
	(0, 0, 0),
	(1, 1, 1),
	(0, 1, 1),
	(1, 0, 0),
	(0, 1, 0),
	(0, 0, 1),
	(0, 0, 0),
	(1, 1, 1),
	(0, 1, 1),
	)

def Cube(): 
	glBegin(GL_QUADS) #Draws the surfaces on the line
	for surface in surfaces:
		x = 0
		for vertex in surface:
			x+=1
			glColor3fv(colors[x])
			glVertex3fv(vertices[vertex])
	glEnd()

	glBegin(GL_LINES)  #Draws lines between the nodes
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])

	glEnd()

def main():
	pygame.init()
	display = (800, 600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL) #Makes working with your monitor's refresh rate more friendly using DOUBLEBUF

	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0) #Sets FOV, aspect ratio and clipping plane

	glTranslatef(0.0, 0.0, -5) #Moves about the object

	glRotatef(0, 0, 0, 0) # Rotates object

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygam.quit()
				quit()

		if event.type == pygame.KEYDOWN: #Moves object in 3D plane
			if event.key == pygame.K_LEFT: #Translate left
				glTranslatef(-0.1,0,0) 
			if event.key == pygame.K_RIGHT: #Translate right
				glTranslatef(0.1,0,0)
			if event.key == pygame.K_UP: #Translate up 
				glTranslatef(0,0.1,0)
			if event.key == pygame.K_DOWN: #Translate down
				glTranslatef(0,-0.1,0)

		if event.type == pygame.MOUSEBUTTONDOWN: #Allows panning (zooming)
			if event.button == 4: #Four is the event for panning in
				glTranslatef(0,0,0.1)
			if event.button == 5: #Five is the event for panning out
				glTranslatef(0,0,-0.1)

		#glRotatef(1, 3, 1, 1) #Rotates the cube
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #What needs to be cleared
		Cube()
		pygame.display.flip() 
		pygame.time.wait(10)

main()