from math import floor

def BuildNeighbors(dat, rows, cols):
	dat.clear()
	dat.appendRow(['pt', 'col', 'row', 'left', 'right', 'top', 'bottom'])

	n = rows * cols
	for i in range(n):
		c = i % cols
		r = floor(i / cols)

		left = -1 if c == 0 else i - 1
		right = -1 if c == (cols - 1) else i + 1
		top = -1 if r == (rows - 1) else i + cols
		bottom = -1 if r == 0 else i - cols
		dat.appendRow([i, c, r, left, right, top, bottom])

