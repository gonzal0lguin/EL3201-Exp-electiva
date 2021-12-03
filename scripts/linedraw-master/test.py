import linedraw
lines = linedraw.sketch("/Users/gonzalolguin/Desktop/testlindraw.jpg")  # return list of polylines, eg.
                                            # [[(x,y),(x,y),(x,y)],[(x,y),(x,y),...],...]
                                            
linedraw.visualize(lines)    
