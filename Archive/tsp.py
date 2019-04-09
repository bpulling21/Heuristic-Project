# tsp.py
# Provided by Dr. Iwerks
# Date: 4/5/19
# A driver program for testing TSP heuristics.

import turtle
import tour

def main():
    # Load Data
    point_data = open('tsp1000.txt', 'r')
    dimensions = point_data.readline().split()
    width = float(dimensions[0])
    height = float(dimensions[1])

    # data is a 2D storing all points from the input file
    data = []
    for line in point_data:
        data.append(line.split())
        
    # Create a tour object
    my_tour = tour.Tour()

    # Insert the points into the tour
    for location in data:
        # Offset for Turtle drawing
        pt = tour.Point(float(location[0]) - width / 2, float(location[1]) - height / 2)
        my_tour.insert_smallest(pt) # Can alternatively call insert_smallest

    # Draw the tour on the screen
    screen = turtle.Screen()
    screen.setup(900, 900)
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    my_tour.draw(t)

    # Report the results
    print('Tour length: ' + str(my_tour.get_length()))    
    print('Number of points: ' + str(my_tour.get_size()))

    turtle.mainloop()

main()
