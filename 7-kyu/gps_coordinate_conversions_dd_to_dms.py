def convert_to_dms(dd_lat, dd_lon):
    def convert_dd_to_dms(dd, is_latitude):
        if is_latitude:
            direction = 'N' if dd >= 0 else 'S'
        else:
            direction = 'E' if dd >= 0 else 'W'
        
        dd_abs = abs(dd)
        degrees = int(dd_abs)
        remaining = (dd_abs - degrees) * 60
        minutes = int(remaining)
        seconds = round((remaining - minutes) * 60, 3)
        
        if seconds >= 60:
            seconds -= 60
            minutes += 1
        if minutes >= 60:
            minutes -= 60
            degrees += 1
        
        ddd = f"{degrees:03d}"
        mm = f"{minutes:02d}"
        ss = f"{seconds:06.3f}"
        ss_parts = ss.split('.')
        ss_formatted = f"{ss_parts[0].zfill(2)}.{ss_parts[1]}"
        return f"{ddd}*{mm}'{ss_formatted}\"{direction}"
    
    dms_lat = convert_dd_to_dms(dd_lat, True)
    dms_lon = convert_dd_to_dms(dd_lon, False)
    return (dms_lat, dms_lon)
