def find_routes(routes):
    start_points = {src for src, _ in routes}
    end_points = {dst for _, dst in routes}
    start = (start_points - end_points).pop()
    route_map = {src: dst for src, dst in routes}
    result = [start]
    while start in route_map:
        start = route_map[start]
        result.append(start)
        
    return ', '.join(result)
