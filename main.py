import pygame as pg
import pg_extended as pgx
import easygui as easy

app = pgx.Window('notepad', [800, 600])

main = pgx.System(preLoadState=True)

navbg = pgx.Section(
	{
		'x':0,
		'y':0,
		'width':pgx.DynamicValue(app, 'screenWidth'),
		'height':pgx.DynamicValue(app, 'screenHeight', percent=5)
	}, pg.Color(44, 44, 44)
)

textArea = None

def save():
	fileUrl = easy.fileopenbox()
	file = open(fileUrl, 'w+')
	file.write(textArea.inputText)
	file.close()

def load():
	fileUrl = easy.fileopenbox()
	file = open(fileUrl, 'r')
	data = file.read()
	file.close()
	textArea.inputText = data
	textArea.setTextBoxValue()
	textArea.textBox.update()

saveButton = pgx.Button(
	pgx.TextBox(
		pgx.Section(
			{
				'x':pgx.DynamicValue(app, 'screenWidth', percent=91),
				'y':0,
				'width':pgx.DynamicValue(app, 'screenWidth', percent=9),
				'height':pgx.DynamicValue(app, 'screenHeight', percent=5)
			}, pg.Color(60, 60, 60)
		), 'Save', 'courier', pg.Color(238, 249, 249), pgx.DynamicValue(17)
	), pressedBG= pg.Color(70, 70, 70),
	callback=pgx.CallbackSet((
		pgx.Callback("mouseUp", save),
	))
)

loadButton = pgx.Button(
	pgx.TextBox(
		pgx.Section(
			{
				'x':pgx.DynamicValue(app, 'screenWidth', percent=82),
				'y':0,
				'width':pgx.DynamicValue(app, 'screenWidth', percent=9),
				'height':pgx.DynamicValue(app, 'screenHeight', percent=5)
			}, pg.Color(60, 60, 60)
		), 'Load', 'courier', pg.Color(238, 249, 249), pgx.DynamicValue(17)
	), pressedBG= pg.Color(70, 70, 70),
	callback=pgx.CallbackSet((
		pgx.Callback("mouseUp", load),
	))
)

textArea = pgx.TextInput(
	pgx.Section(
		{
			'x':0,
			'y':pgx.DynamicValue(app, 'screenHeight', percent=5),
			'width':pgx.DynamicValue(app, 'screenWidth'),
			'height':pgx.DynamicValue(app, 'screenHeight', percent=95)
		}, pg.Color(39, 39, 39)
	), 'courier', pg.Color(238, 249, 249),alignTextHorizontal='left', alignTextVertical='top'
)

textArea.textBox.fontSize = pgx.DynamicValue(20)
textArea.textBox.paddingLeft = 0
main.addElement(navbg, 'bg')
main.addElement(textArea, 'txt')
main.addElement(saveButton, 'button')
main.addElement(loadButton,'loadbtn')

app.addSystem(main, 'main')
app.setSystemZ('main', 0)

app.activateSystems('main')

app.openWindow()
