import pygame as pg
import pg_extended as pgx


app = pgx.Window('notepad', [800, 600])

main = pgx.System(preLoadState=True)

navbg = pgx.Section(
	{
		'x':0,
		'y':0,
		'width':pgx.DynamicValue(app, 'screenWidth'),
		'height':pgx.DynamicValue(app, 'screenHeight', percent=5)
	}, pg.Color(0,50,255)
)

textArea = pgx.TextInput(
	pgx.Section(
		{
			'x':0,
			'y':pgx.DynamicValue(app, 'screenHeight', percent=5),
			'width':pgx.DynamicValue(app, 'screenWidth'),
			'height':pgx.DynamicValue(app, 'screenHeight', percent=95)
		}, pg.Color(0,50,50)
	), 'ariel', pg.Color(255, 255, 255), -1, '', pg.Color(0,0,0),0,None,None, None, None, 'left', 'top'
)

textArea.textBox.text = "hello saurabh"
textArea.textBox.fontSize = pgx.DynamicValue(30)

main.addElement(navbg, 'bg')
main.addElement(textArea, 'txt')

app.addSystem(main, 'main')
app.setSystemZ('main', 0)

app.activateSystems('main')

app.openWindow()
