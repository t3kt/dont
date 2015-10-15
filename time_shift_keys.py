def setupParameters(dat):
	page = dat.appendCustomPage('Custom')
	p = page.appendInt('Newid', label='New ID')[0]
	p.min=1
	p.normMin=1
	p.clampMin=True
	p.normMax=20
	p=page.appendFloat('Startoffset')[0]
	p.normMin=-200
	p.normMax=200
	p=page.appendFloat('Endoffset')[0]
	p.normMin=-200
	p.normMax=200
	

def cook(dat):
	inkeys = dat.inputs[0]
	dat.copy(inkeys)
	newId = dat.par.Newid.eval()
	startOffset = dat.par.Startoffset.eval()
	endOffset = dat.par.Endoffset.eval()
	for row in dat.rows()[1:]:
		row[0].val = newId
		t = float(row[1])
		if t == 0:
			continue
		if row[2] == '0':
			t += endOffset
		else:
			t += startOffset
		row[1].val = t
