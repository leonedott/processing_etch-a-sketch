w_width = 1000
w_height = 800

screen_width = 5*(w_width/6)
screen_height = 4*(w_height/6)

screen_center_y = (w_height/2)-(w_width/20)

button_size = 9*(w_width/80)
button_center_y = screen_center_y+(w_height/3)+7*(w_height/60)

x = w_width/2
y = screen_center_y 



def knob(x_position, y_position, size_of, tag_01, tag_02):
    fill(149, 165, 166)
    stroke(52, 73, 94)
    strokeWeight(5)
    ellipse(x_position, y_position, size_of, size_of)
    line(x_position - size_of/2, y_position, x_position + size_of/2, y_position)

    fill(52, 73, 94)
    textSize(button_size/6)
    textAlign(CENTER)
    text(tag_01, x_position, y_position - size_of/8)
    text(tag_02, x_position, y_position + size_of/4)


def setup():
    
    frameRate(10)
    size (w_width, w_height)
    
    # Frame
    rectMode(CENTER)
    noStroke()
    fill(192, 57, 43)
    rect (w_width/2, w_height/2, w_width, w_height)
    
    # Screen
    fill(189, 195, 199)
    stroke(52, 73, 94)
    strokeWeight(5)
    rect (w_width/2, screen_center_y, screen_width, screen_height, w_height/30)
    
    # Knobs
    left_knob = knob(w_width/6, button_center_y, button_size, 'LEFT (e)', 'RIGHT (c)')
    right_knob = knob(5*(w_width/6), button_center_y, button_size, 'UP (i)', 'DOWN (n)')
    
    # 'CLEAR' Button
    fill(243, 156, 18)
    stroke(211, 84, 0)
    square(w_width/2, button_center_y, button_size)
    fill(211, 84, 0)
    textSize(button_size/5)
    textAlign(CENTER, CENTER)
    text('CLEAR', w_width/2, button_center_y)
    
    # 'SAVE' button
    fill(46, 204, 113)
    stroke(39, 174, 96)
    square(w_width/2 + (button_size*1.1), button_center_y, button_size/2)
    fill(52, 73, 94)
    textSize(button_size/8)
    textAlign(CENTER, CENTER)
    text('SAVE', w_width/2 + (button_size*1.1), button_center_y)

def draw():
    
    global x
    global y
    
    fill(120)
    noStroke()
    ellipse(x, y, 3, 3)
    
    if mousePressed is True: 
        if mouseX > (w_width/6 - button_size/2) and mouseX < (w_width/6 + button_size/2):
            if mouseY > button_center_y - button_size/2 and mouseY < button_center_y:
                x = x-1
            if mouseY > button_center_y and mouseY < button_center_y + button_size/2:
                x = x+1
        if mouseX > (5*(w_width/6)) - button_size/2 and mouseX < (5*(w_width/6)) + button_size/2:
            if mouseY > button_center_y - button_size/2 and mouseY < button_center_y:
                y = y-1
            if mouseY > button_center_y and mouseY < button_center_y + button_size/2:
                y = y+1
        ellipse(x, y, 1, 1)
        if mouseX > w_width/2 + (button_size*1.1) - (button_size/4) and mouseX < w_width/2 + (button_size*1.1) + (button_size/4) and mouseY > button_center_y - button_size/4 and mouseY > button_center_y - button_size/4:
            selectOutput('Select a file to write to: ', 'fileSelected')
        if mouseX > w_width/2 - button_size/2 and mouseX < w_width/2 + button_size/2 and mouseY > button_center_y - button_size/2 and mouseY < button_center_y + button_size/2:
            setup()
            x = w_width/2
            y = screen_center_y
            
    if keyPressed:
        if key == 's' or key == 'S':
            selectOutput('Select a file to write to: ', 'fileSelected')
        elif key == 'e' or key == 'E':
            x = x-1
        elif key == 'c' or key == 'C':
            x = x+1
        elif key == 'i' or key == 'I':
            y = y-1
        elif key == 'n' or key == 'N':
            y = y+1    
        ellipse(x, y, 1, 1)
                
def fileSelected(selection):
    if selection == None:
        pass
    else:
        dir2 = selection.getPath()
        save(dir2 + '.jpg')
    
        
        
    

    
            

        
        
        
