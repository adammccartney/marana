
SHELL = /bin/bash

.PHONY: materials segments

collect:
	rm -f builds/segments/*.ly;
	cd segments && for segment in segment_*; do \
		sed '/^\\score/,/^\}/!d;/^\\score/d;/^\}/d' $$segment/illustration.ly > ../builds/segments/$${segment/_/_}.ily; \
	done;

segments:
	make segment_A
	make segment_B
	make segment_C
	make segment_D
	make segment_E
	make segment_F
	make segment_G

segment_A:
	python ./segments/segment_A/definition.py

segment_B:
	python ./segments/segment_B/definition.py

segment_C:
	python ./segments/segment_C/definition.py

segment_D:
	python ./segments/segment_D/definition.py

segment_E:
	python ./segments/segment_E/definition.py

segment_F:
	python ./segments/segment_F/definition.py

segment_G:
	python ./segments/segment_G/definition.py


