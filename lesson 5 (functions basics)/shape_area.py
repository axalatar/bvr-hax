def area_finder(shape, width, height):
    if(shape == "circle"):
        return 3.1415 * ((width/2) ** 2)
    elif(shape == "triangle"):
        return (width * height) / 2
    else:
        return width * height