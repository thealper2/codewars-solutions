def color_2_grey(image):
    def color_grey(R, G, B):
        result = []
        for x in [(R + G + B) / 3, (R + G + B) / 3, (R + G + B) / 3]:
            result.append(round(x))
            
        return result
    
    return [[color_grey(*x) for x in y] for y in image]
