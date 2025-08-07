import math

def solution(F1, F2, theta) :
    theta_rad = math.radians(theta)
    R = math.sqrt(F1**2 + F2**2 + 2 * F1 * F2 * math.cos(theta_rad))
    phi = math.atan2(F2 * math.sin(theta_rad), F1 + F2 * math.cos(theta_rad))
    phi_deg = math.degrees(phi)
    return [R, phi_deg]
