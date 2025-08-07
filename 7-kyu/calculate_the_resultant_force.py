import math


def solution(F1, F2, theta) :
    theta_rad = math.radians(theta)
    R = math.sqrt(F1**2 + F2**2 + 2 * F1 * F2 * math.cos(theta_rad))
    if R == 0:
        phi_deg = 0.0
        
    else:
        sin_phi = (F2 * math.sin(theta_rad)) / R
        sin_phi = min(1, max(-1, sin_phi))
        phi_rad = math.asin(sin_phi)
        phi_deg = math.degrees(phi_rad)
        
    return [R, phi_deg]
