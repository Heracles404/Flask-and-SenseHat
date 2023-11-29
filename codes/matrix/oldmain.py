from flask import Flask, render_template, request
from sense_hat import SenseHat
import time
import os

sense = SenseHat()
#pokecolors
r = (255, 0, 0)
org = (255, 128, 0)
g = (0, 102, 102)
y = (255, 255, 0)
d2 = (204, 102, 0)
d3 = (153, 76, 0)
dr = (204, 0, 0)
lg = (0, 255, 0)
dg = (0, 153 ,0)
bg = (0, 153, 153)
og = (0, 204, 0)
m = (153, 0, 0)
lc = (240, 128, 128)
bro = (139, 69, 19)
od = (107, 142, 35)
b = (0, 0, 255)

#squirtle
b1 = (95, 205, 228)
b2 = (44, 133, 129)
b3 = (17, 83, 94)
y2 = (255, 204, 17)
br1 = (188, 120, 22)
br2 = (110, 61, 14)
bb1 = (149, 179, 239)
bb2 = (60, 55, 208)
bb3 = (31, 26, 177)
g2 = (149, 179, 239)


e = (0, 0, 0)
w = (255, 255, 255)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    text = request.form['this_input']

    if 'pattern' in request.form:
        # If a button is clicked, process the corresponding pattern
        pattern = request.form['pattern']
        result = process_pattern(pattern)
    else:
        # If the form is submitted without a button, check for patterns in the text
        if 'Pattern 0' in text:
            result = process_textIn(text)
        elif 'Pattern 1' in text:
            result = process_pattern1()
        elif 'Pattern 2' in text:
            result = process_pattern2()
        elif 'Pattern 3' in text:
            result = process_pattern3()
        else:
            result = process_textIn()

    return render_template('index.html', result=result)

def process_pattern(pattern):
    if pattern == 'Pattern 0':
        return process_textIn()
    elif pattern == 'Pattern 1':
        return process_pattern1()
    elif pattern == 'Pattern 2':
        return process_pattern2()
    elif pattern == 'Pattern 3':
        return process_pattern3()
    else:
        result = process_textIn()

def process_pattern1():
    # Pattern 1
    sense.clear()
    char1 = [
        [e, e, e, e, org, d2, e, e],
        [e, e, e, org, org, org, d2, e],
        [y, r, e, org, g, d2, g, e],
        [org, y, e, org, org, org, d2, e],
        [e, org, e, org, org, y, e, e],
        [e, d2, org, org, y, y, d2, e],
        [e, e, org, y, y, d2, e, d2],
        [e, e, org, e, e, d2, e, e]
    ]

    evo1 = [
        [e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e],
        [e, e, e, w, w, e, e, e],
        [e, e, e, w, w, e, e, e],
        [e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e]
    ]

    evo2 = [
        [e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e],
        [e, e, w, w, w, w, e, e],
        [e, e, w, e, e, w, e, e],
        [e, e, w, e, e, w, e, e],
        [e, e, w, w, w, w, e, e],
        [e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e]
    ]

    evo3 = [
        [e, e, e, e, e, e, e, e],
        [e, w, w, w, w, w, w, e],
        [e, w, e, e, e, e, w, e],
        [e, w, e, e, e, e, w, e],
        [e, w, e, e, e, e, w, e],
        [e, w, e, e, e, e, w, e],
        [e, w, w, w, w, w, w, e],
        [e, e, e, e, e, e, e, e]
    ]

    evo4 = [
        [w, w, w, w, w, w, w, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, w, w, w, w, w, w, w]
    ]

    char2 = [
        [e, e, r, r, e, y, org, e],
        [e, r, r, r, e, e, r, e],
        [w, r, w, r, dr, e, e, dr],
        [r, r, r, r, dr, dr, e, dr],
        [e, e, y, y, r, r, dr, dr],
        [w, r, y, y, y, r, w, e],
        [e, r, dr, e, e, r, r, e],
        [e, e, r, e, e, e, r, e]
    ]

    char3 = [
        [e, org, e, org, e, e, d2, d2],
        [d3, org, org, org, e, d3, g, d3],
        [g, w, org, w, org, g, g, d3],
        [g, org, org, org, org, org, d3, g],
        [org, g, y, y, d2, g, org, g],
        [g, g, y, y, d2, org, g, g],
        [e, org, d2, y, y, org, d2, d2],
        [e, org, org, e, e, org, d3, e]
    ]
    
    flatchar1 = [pixel for row in char1 for pixel in row] 
    flatevo1 = [pixel for row in evo1 for pixel in row]
    flatevo2 = [pixel for row in evo2 for pixel in row]
    flatevo3 = [pixel for row in evo3 for pixel in row]
    flatevo4 = [pixel for row in evo4 for pixel in row]
    flatchar2 = [pixel for row in char2 for pixel in row]
    flatchar3 = [pixel for row in char3 for pixel in row]
    

    for pixel in zip(flatchar1, flatevo1, flatevo2, flatevo3, flatevo4, flatchar2, flatchar3):
        print(pixel, end='')

    sense.set_pixels(flatchar1)
    time.sleep(2)
    sense.set_pixels(flatevo1)
    time.sleep(0.5)
    sense.set_pixels(flatevo2)
    time.sleep(0.5)
    sense.set_pixels(flatevo3)
    time.sleep(0.5)
    sense.set_pixels(flatevo4)
    time.sleep(0.5)
    sense.set_pixels(flatchar2)
    time.sleep(2)
    sense.set_pixels(flatevo1)
    time.sleep(0.5)
    sense.set_pixels(flatevo2)
    time.sleep(0.5)
    sense.set_pixels(flatevo3)
    time.sleep(0.5)
    sense.set_pixels(flatevo4)
    time.sleep(0.5)
    sense.set_pixels(flatchar3)
    time.sleep(2)

    return 'Processing Pattern 1'

def process_pattern2():
    # Pattern 2
    sense.clear()
    bulba1 = [
        [e, e, e, e, e, lg, lg, e],
        [e, e, e, og, lg, lg, lg, og],
        [e, e, og, lg, lg, lg, og, og],
        [e, bg, bg, dg, dg, lg, og, og],
        [e, w, bg, w, dg, bg, dg, og],
        [e, bg, r, bg, bg, bg, bg, dg],
        [e, e, dg, dg, bg, dg, bg, dg],
        [e, e, bg, e, bg, dg, bg, e],
    ]

    evo1 = [
        [e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e],
        [e, e, e, w, w, e, e, e],
        [e, e, e, w, w, e, e, e],
        [e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e]
    ]

    evo2 = [
        [e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e],
        [e, e, w, w, w, w, e, e],
        [e, e, w, e, e, w, e, e],
        [e, e, w, e, e, w, e, e],
        [e, e, w, w, w, w, e, e],
        [e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e]
    ]

    evo3 = [
        [e, e, e, e, e, e, e, e],
        [e, w, w, w, w, w, w, e],
        [e, w, e, e, e, e, w, e],
        [e, w, e, e, e, e, w, e],
        [e, w, e, e, e, e, w, e],
        [e, w, e, e, e, e, w, e],
        [e, w, w, w, w, w, w, e],
        [e, e, e, e, e, e, e, e]
    ]

    evo4 = [
        [w, w, w, w, w, w, w, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, w, w, w, w, w, w, w]
    ]

    bulba2 = [
        [e, e, r, r, e, e, e, e],
        [e, m, r, r, r, e, e, e],
        [e, m, m, r, og, og, e, e],
        [e, og, og, lg, lg, lg, og, e],
        [og, og, lg, lg, dg, dg, bg, og],
        [e, dg, dg, bg, w, bg, w, e],
        [dg, dg, dg, bg, bg, r, bg, e],
        [dg, e, dg, bg, e, e, bg, e]
    ]

    bulba3 = [
        [e, e, r, y, y, r, m, e],
        [e, m, r, lc, lc, lc, m, m],
        [e, m, bro, lc, lc, bro, e, e],
        [e, og, lg, lg, lg, od, od, dg],
        [og, dg, dg, og, lg, dg, od, od],
        [w, bg, bg, w, og, dg, dg, od],
        [bg, r, r, bg, bg, dg, bg, dg],
        [e, bg, e, bg, e, e, bg, bg]
    ]
    
    flatbulba1 = [pixel for row in bulba1 for pixel in row]
    flatevo1 = [pixel for row in evo1 for pixel in row]
    flatevo2 = [pixel for row in evo2 for pixel in row]
    flatevo3 = [pixel for row in evo3 for pixel in row]
    flatevo4 = [pixel for row in evo4 for pixel in row]
    flatbulba2 = [pixel for row in bulba2 for pixel in row]
    flatbulba3 = [pixel for row in bulba3 for pixel in row]

    for pixel in zip(flatbulba1, flatevo1, flatevo2, flatevo3, flatevo4, bulba2, bulba3):
        print(pixel, end='')

    sense.set_pixels(flatbulba1)
    time.sleep(2)
    sense.set_pixels(flatevo1)
    time.sleep(0.5)
    sense.set_pixels(flatevo2)
    time.sleep(0.5)
    sense.set_pixels(flatevo3)
    time.sleep(0.5)
    sense.set_pixels(flatevo4)
    time.sleep(0.5)
    sense.set_pixels(flatbulba2)
    time.sleep(2)
    sense.set_pixels(flatevo1)
    time.sleep(0.5)
    sense.set_pixels(flatevo2)
    time.sleep(0.5)
    sense.set_pixels(flatevo3)
    time.sleep(0.5)
    sense.set_pixels(flatevo4)
    time.sleep(0.5)
    sense.set_pixels(flatbulba3)
    time.sleep(2)
    
    return 'Processing Pattern 2'

def process_pattern3():
    # Pattern 3
    sense.clear()
    squirt1 = [
        [e, e, e, b1, b2, e, e, e],
        [e, e, b1, b1, b1, b2, e, e],
        [e, e, w, b1, w, b2, e, e],
        [b1, e, e, b3, b3, br2, e, b1],
        [e, b1, br1, y2, y2, br1, b1, e],
        [e, e, y2, y2, y2, y2, br2, e],
        [e, e, b1, br1, br1, b1, br2, b2],
        [e, e, b1, e, e, e, b1, y],
    ]

    evo1 = [
        [e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e],
        [e, e, e, w, w, e, e, e],
        [e, e, e, w, w, e, e, e],
        [e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e]
    ]

    evo2 = [
        [e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e],
        [e, e, w, w, w, w, e, e],
        [e, e, w, e, e, w, e, e],
        [e, e, w, e, e, w, e, e],
        [e, e, w, w, w, w, e, e],
        [e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e]
    ]

    evo3 = [
        [e, e, e, e, e, e, e, e],
        [e, w, w, w, w, w, w, e],
        [e, w, e, e, e, e, w, e],
        [e, w, e, e, e, e, w, e],
        [e, w, e, e, e, e, w, e],
        [e, w, e, e, e, e, w, e],
        [e, w, w, w, w, w, w, e],
        [e, e, e, e, e, e, e, e]
    ]

    evo4 = [
        [w, w, w, w, w, w, w, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, w, w, w, w, w, w, w]
    ]

    squirt2 = [
        [e, e, e, e, w, e, e, w],
        [w, w, e, e, bb1, w, e, bb1],
        [w, w, br1, br1, br1, bb3, bb2, bb2],
        [w, br1, br1, bb1, bb3, w, bb2, w],
        [bb1, br2, br2, bb1, bb3, bb3, r, bb2],
        [bb1, br2, br2, bb2, br1, y2, y2, e],
        [e, bb1, bb2, bb3, y2, y2, bb1, bb2],
        [e, e, bb3, bb2, e, e, bb2, e]
    ]

    squirt3 = [
        [e, w, e, br1, br1, br1, e, w],
        [bb2, bb2, bb3, bb2, br1, br2, br2, g2],
        [w, bb2, g2, bb3, w, g2, br2, br2],
        [bb2, bb2, bb3, bb3, w, bb2, bb3, br2],
        [w, br1, br1, y, w, bb2, bb2, bb3],
        [e, y2, y2, y2, br1, w, g2, g2],
        [bb2, bb2, br1, br2, br2, bb2, bb3, g2],
        [bb2, bb3, e, e, e, bb2, bb3, e]
    ]
    
    flatsquirt1 = [pixel for row in squirt1 for pixel in row]
    flatevo1 = [pixel for row in evo1 for pixel in row]
    flatevo2 = [pixel for row in evo2 for pixel in row]
    flatevo3 = [pixel for row in evo3 for pixel in row]
    flatevo4 = [pixel for row in evo4 for pixel in row]
    flatsquirt2 = [pixel for row in squirt2 for pixel in row]
    flatsquirt3 = [pixel for row in squirt3 for pixel in row]

    
    for pixel in zip(flatsquirt1, flatevo1, flatevo2, flatevo3, flatevo4, squirt2, squirt3):
        print(pixel, end='')

    sense.set_pixels(flatsquirt1)
    time.sleep(2)
    sense.set_pixels(flatevo1)
    time.sleep(0.5)
    sense.set_pixels(flatevo2)
    time.sleep(0.5)
    sense.set_pixels(flatevo3)
    time.sleep(0.5)
    sense.set_pixels(flatevo4)
    time.sleep(0.5)
    sense.set_pixels(flatsquirt2)
    time.sleep(2)
    sense.set_pixels(flatevo1)
    time.sleep(0.5)
    sense.set_pixels(flatevo2)
    time.sleep(0.5)
    sense.set_pixels(flatevo3)
    time.sleep(0.5)
    sense.set_pixels(flatevo4)
    time.sleep(0.5)
    sense.set_pixels(flatsquirt3)
    time.sleep(2)
    
    
    return 'Processing Pattern 3'

def process_textIn():
    # for custom text display
    sense.clear()
    text = request.form['this_input']

    ret = f"Displaying {text}"
    
    sense.show_message(text, text_colour=b)
    return ret

# stopping display
@app.route('/Stop', methods=['POST'])
def Stop():
    os.system('sudo shutdown now')
    return 'Stopping...'

# halt Pi
@app.route('/Halt', methods=['POST'])
def Halt():
    os.system('sudo shutdown -h now')
    return 'Shutting down...'


if __name__ == '__main__':
    app.run(debug=True)
