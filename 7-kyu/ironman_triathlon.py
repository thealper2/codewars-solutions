def i_tri(distance):
    total = 140.6
    if distance == 0:
        return 'Starting Line... Good Luck!'
    if distance >= total:
        return "You're done! Stop running!"
    
    if distance < 2.4:
        return {'Swim': f'{total - distance:.2f} to go!'}
    elif distance < 114.4:
        return {'Bike': f'{total - distance:.2f} to go!'}
    else:
        remaining = total - distance
        if remaining > 10:
            return {'Run': f'{remaining:.2f} to go!'}
        else:
            return {'Run': 'Nearly there!'}
