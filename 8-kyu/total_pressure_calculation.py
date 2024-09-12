def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
	R = 0.082
	T_K = temp + 273.15
	P_total = ((given_mass1 / molar_mass1) + (given_mass2 / molar_mass2)) * (R * T_K) / volume
	return P_total
