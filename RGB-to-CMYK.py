#RGB to CMYK Color Conversion

def RGB_to_CMYK(R1,G1,B1):
	R = R1/255
	G = G1/255
	B = B1/255

	K = (1 - max(R,G,B))

	if K == 1:
		C = (1 - R - K)
		M = (1 - R - K)
		Y = (1 - B - K)
	else:
		C = (1 - R - K) / (1 - K)
		M = (1 - G - K) / (1 - K)
		Y = (1 - B - K) / (1 - K)

	CMYK = [C, M, Y, K]
	CMYK = [i * 100 for i in CMYK]
	CMYK_str = ", ".join(str(round(element)) for element in CMYK)
	return CMYK_str


def main():
	R1 = int(input('Red component:'))
	G1 = int(input('Green component:'))
	B1 = int(input('Blue component:'))
	print('CMYK representation:',RGB_to_CMYK(R1,G1,B1))

main()