def direction(facing, turn):
    facings = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    degrees = [0, 45, 90, 135, 180, 225, 270, 315]

    if facing not in facings:
        return("Error: facing does't correct")
    if turn % 45 != 0:
        return("Error: turn should be multiple of 45")
    if turn not in range(-1080, 1080):
        return("Error: facing should be between -1080 and 1080")
    turn = turn % 360 if turn > 360 else turn

    new_degree = degrees[facings.index(facing)] + turn
    new_degree = new_degree % 360 if new_degree >= 360 else new_degree
    return facings[degrees.index(new_degree)]
