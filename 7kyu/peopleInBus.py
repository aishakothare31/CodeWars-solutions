def number(bus_stops):
    #an array of integer arrays which consist of the no. of people boarding and departing from the bus. 
    #To determine no. of people left in bus after last stop
    return sum(board-left for board,left in bus_stops)