import re
import debug

def rotr(input, n):
	"""Rotate n bits of input to the right"""
	return (input >> n) | (input << 32 - n)

def shiftr(input, n):
	"""Shift n bits of input to the right"""
	return input >> n

mod_const = 0b100000000000000000000000000000000

def sha256(input, is_hex = False):
	"""Calculate sha256 of input.
	If is_hex is True, input is evaluated as hex string. Otherwise as utf8.
	"""

	H = [
		0x6a09e667, 0xbb67ae85,
		0x3c6ef372, 0xa54ff53a,
		0x510e527f, 0x9b05688c,
		0x1f83d9ab, 0x5be0cd19
	]

	K = [
		0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
		0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
		0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
		0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
		0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
		0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
		0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
		0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
	]
 
	if is_hex:
		if not re.match("^[0-9a-f]+$", input, re.IGNORECASE) or len(input) % 2 != 0:
			raise ValueError(f"Invalid hex input: {input}")

	# Convert input string to bytearray
	binary = bytearray.fromhex(input) if is_hex else bytearray(input, "utf8")
	input_length = len(binary)

	# Append byte 0x80 (0b10000000)
	binary.append(0x80)

	# Pad until we get a multiple of 64 bytes (minus 8 bytes, for input length)
	remaining_bytes = (64 - len(binary) - 8) % 64
	for i in range(remaining_bytes):
		binary.append(0)

	# Append 8 bytes with the original input length (in bits), totalling a multiple of 64 bytes or 512 bits
	binary.extend(int.to_bytes(input_length * 8, 8, 'big'))

	# Split data into blocks of 64 bytes each and cycle through them
	num_blocks = len(binary) // 64
	for block_count in range(num_blocks):
		block_start = block_count * 64
		block = binary[block_start : block_start + 64]
		W = []
		i = 0

		# Create message schedule (W) for this block. The 64 bytes will become 16 words (4 bytes each)
		while i < len(block):
			temp = (block[i] << 8) | block[i + 1]
			temp = (temp << 8) | block[i + 2]
			temp = (temp << 8) | block[i + 3]
			W.append(temp)
			i += 4
		
		# Add 48 more words initialized to zero, such that we have an array W of 64 words
		remaining_words = 64 - len(W)
		for i in range(remaining_words):
			W.append(0)
	
		# Perform rotate/shift in words W[16:64], finalizing W
		for i in range(16, 64):
			s0 = rotr(W[i - 15], 7) ^ rotr(W[i - 15], 18) ^ shiftr(W[i - 15], 3)
			s1 = rotr(W[i - 2], 17) ^ rotr(W[i - 2], 19) ^ shiftr(W[i - 2], 10)
			W[i] = (W[i - 16] + s0 + W[i - 7] + s1) % mod_const

		# Compression loop. Calculate variables a-h
		a, b, c, d, e, f, g, h = H[0], H[1], H[2], H[3], H[4], H[5], H[6], H[7]
		for i in range(64):
			s1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25)
			ch = (e & f) ^ (~e & g)
			temp1 = (h + s1 + ch + K[i] + W[i]) % mod_const
			s0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22)
			maj = (a & b) ^ (a & c) ^ (b & c)
			temp2 = (s0 + maj) % mod_const
			h = g
			g = f
			f = e
			e = (d + temp1) % mod_const
			d = c
			c = b
			b = a
			a = (temp1 + temp2) % mod_const
		
		# Update the hash
		H[0] = (H[0] + a) % mod_const
		H[1] = (H[1] + b) % mod_const
		H[2] = (H[2] + c) % mod_const
		H[3] = (H[3] + d) % mod_const
		H[4] = (H[4] + e) % mod_const
		H[5] = (H[5] + f) % mod_const
		H[6] = (H[6] + g) % mod_const
		H[7] = (H[7] + h) % mod_const

	# Concatenate final hash
	hash = H[0]
	for i in range(1, len(H)):
		hash = (hash << 32 ) | H[i]

	result = hex(hash)[2:]
	return result.rjust(64, "0")
