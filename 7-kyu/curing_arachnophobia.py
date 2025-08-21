def draw_spider(leg_size, body_size, mouth, eye):
    legs = {
        1: ("^", "^"),
        2: ("/\\", "/\\"),
        3: ("/╲", "╱\\"),
        4: ("╱╲", "╱╲")
    }

    left_leg, right_leg = legs[leg_size]
    eye_count = 2 ** body_size
    left_eyes = eye * (eye_count // 2)
    right_eyes = eye * (eye_count // 2)
    left_body = "(" * body_size
    right_body = ")" * body_size
    spider = f"{left_leg}{left_body}{left_eyes}{mouth}{right_eyes}{right_body}{right_leg}"
    return spider
