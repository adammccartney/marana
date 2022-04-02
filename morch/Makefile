SHELL := /usr/bin/bash
PYTHON := ../../venv/bin/python3

INSTRUMENTS_DIR := instruments
SCORE_DIR := score
SKETCH_DIR := sketch

INSTRUMENTS := $(wildcard $(INSTRUMENTS_DIR)/*.py) 
OBJECTS := $(addprefix $(BUILD_DIR)/, $(notdir $(SOURCES:.py=.ly)))

SKETCHES := $(wildcard $(SKETCH_DIR)/*.ly)

BUILD_DIR := build

default: $(BUILD_DIR)/score.pdf

brass: $(BUILD_DIR)/brass-sketch.pdf

$(BUILD_DIR)/score.pdf: bassoon_voice hrn_three_voice copy_score
	@ lilypond -o $(BUILD_DIR)/score $(BUILD_DIR)/score.ly

# Copy lilypond score to build_dir 
copy_score: 
	@ mkdir -p $(BUILD_DIR)
	@ cp $(SCORE_DIR)/score.ly $(BUILD_DIR)

bassoon_voice: 
	@ mkdir -p $(BUILD_DIR)
	@ $(PYTHON) $(INSTRUMENTS_DIR)/bassoon.py > $(BUILD_DIR)/bassoon.ly

hrn_three_voice:
	@ mkdir -p $(BUILD_DIR)
	@ $(PYTHON) $(INSTRUMENTS_DIR)/hrn3.py > $(BUILD_DIR)/hrn3.ly

$(BUILD_DIR)/brass-sketch.pdf: setup_brass
	@ mkdir -p $(BUILD_DIR)
	@ lilypond -o $(BUILD_DIR)/brass-sketch $(BUILD_DIR)/iygh-score.ly

setup_brass: $(SKETCH_DIR)/brass.ly 
	@ mkdir -p $(BUILD_DIR)
	@ cp $(SKETCH_DIR)/brass.ly $(BUILD_DIR)
	@ cp $(SCORE_DIR)/iygh-score.ly $(BUILD_DIR)


$(SKETCH_DIR)/brass.ly: $(SKETCH_DIR)/brass.py
	@ $(PYTHON) $(SKETCH_DIR)/brass.py > $(SKETCH_DIR)/brass.ly

clean:
	rm -rf $(BUILD_DIR) 

.PHONY: default clean
