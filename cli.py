from smartra import calculate_smartra_pin

def get_last_6_digits (text_input: str) -> int:
	try:
		return int(text_input[-6:])
	except (ValueError, IndexError):
		raise ValueError


def main():
	print('[*] SMARTRA VIN to PIN calculator')
	print('[*] This calculator should apply for all Hyundai and KIA models equipped with SMARTRA2')
	print('[*] From 2007 or so, some models started using SMARTRA3 and a different algorithm - beware.')

	while True:
		try:
			last_6_digits = get_last_6_digits(input('[*] Enter your VIN or just it\'s last 6 digits: '))
			calculated_pin = calculate_smartra_pin(last_6_digits)
			print('[*] All good! Your immo pin should be: {}'.format(calculated_pin))
			break
		except ValueError:
			print('[!] Something went wrong. Try again')

if __name__ == '__main__':
	main()