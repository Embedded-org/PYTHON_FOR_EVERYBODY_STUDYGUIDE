import tkinter
import time

# Make the window large so that we can see more detail. 
CANVAS_WIDTH = 1000;
CANVAS_HEIGHT = 750;

# The viewpoint coordinates - the min and max long and lat
MIN_LONGITUDE = -130;
MAX_LONGITUDE = -60;
MIN_LATITUDE = +22;
MAX_LATITUDE = +55;

def main():
    n_done = 0
    # get a drawing canvas
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'US Cities')

    # load the file!
    with open('us-cities.txt') as cities_file:
        # skip the first line, its just a header
        next(cities_file)

        # read the file one line at a time
        for line in cities_file:
            # get rid of all the whitespace
            line = line[:-1]
            # split the line into parts
            parts = line.split(',')
            # parts = [city, state, lat, lon]
            lat = float(parts[2])
            lon = float(parts[3])
            plot_one_city(canvas, lat, lon)

            # why not :-)
            n_done += 1
            if n_done % 100 == 0:
                canvas.update()
                time.sleep(1/50)
        canvas.mainloop()


'''
Given the longitude and latitude of a city (in double form), displays
a dot for that city.
'''
def plot_one_city(canvas, latitude, longitude) :
    # Determine where on screen the city should be drawn. 
    x = longitude_to_x(longitude)
    y = latitude_to_y(latitude)
    plot_pixel(canvas, x, y)

'''
Plots a pixel at the specified (x, y) coordinate.'''
def plot_pixel(canvas, x, y):
    # Create a 1x1 rectangle
    canvas.create_rectangle(x, y, x+1, y+1, fill="blue", outline="blue")

'''
Given a raw longitude, returns the screen x coordinate where
it should be displayed.
'''
def longitude_to_x(longitude):
    return CANVAS_WIDTH * (longitude - MIN_LONGITUDE) / (MAX_LONGITUDE - MIN_LONGITUDE)

'''
Given a raw latitude, returns the screen y coordinate where
it should be displayed.
'''
def latitude_to_y(latitude):
    return CANVAS_HEIGHT * (1.0 - (latitude - MIN_LATITUDE) / (MAX_LATITUDE - MIN_LATITUDE))


######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title=None):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas


if __name__ == '__main__':
    main()
