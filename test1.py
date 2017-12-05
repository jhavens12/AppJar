from appJar import gui

app = gui('Test1' '480x320')
app.setGeometry('fullscreen')
#app.setBg('black')
app.setFont(72)
app.addLabel('L1', 'test_label', 1,1,3)
app.setLabelFg('L1', 'blue')
app.go()
