def setupParameters(dat):
	#dat.destroyCustomPars()
	pass

import xml.etree.ElementTree as ET

def cook(dat):
	dat.clear()
	dat.appendRow(['track', 'label', 'start', 'end', 'length'])
	root = ET.fromstring(dat.inputs[0].text)
	labelTracks = root.findall('./a:labeltrack', {"a": "http://audacity.sourceforge.net/xml/"})
	for labelTrack in labelTracks:
		trackName = labelTrack.attrib['name']
		for label in labelTrack.findall('./a:label', {"a": "http://audacity.sourceforge.net/xml/"}):
			t0, t1 = float(label.attrib['t']), float(label.attrib['t1'])
			dat.appendRow([
				trackName,
				label.attrib['title'],
				t0,
				t1,
				t1 - t0
			])