SHELL := /usr/bin/bash
PYTHON := ../../venv/bin/python3

INSTRUMENTS_DIR := instruments
SCORE_DIR := score
SRC_DIR := src
SKETCH_DIR := sketch

SOURCES  := $(wildcard $(SRC_DIR)/*.py)
SKETCHES := $(addprefix $(SKETCH_DIR)/, $(notdir $(SOURCES:.py=.ly)))

BUILD_DIR := build

default: $(BUILD_DIR)/score.pdf

brass: $(BUILD_DIR)/brass-sketch.pdf

$(BUILD_DIR)/score.pdf: bassoon_voice copy_score
	@ lilypond -o $(BUILD_DIR)/score $(BUILD_DIR)/score.ly

# Copy lilypond score to build_dir 
copy_score: 
	@ mkdir -p $(BUILD_DIR)
	@ cp $(SCORE_DIR)/score.ly $(BUILD_DIR)

bassoon_voice: 
	@ mkdir -p $(BUILD_DIR)
	@ $(PYTHON) $(INSTRUMENTS_DIR)/bassoon.py > $(BUILD_DIR)/bassoon.ly

$(BUILD_DIR)/brass-sketch.pdf: setup_brass
	@ mkdir -p $(BUILD_DIR)
	@ lilypond -o $(BUILD_DIR)/brass-sketch $(BUILD_DIR)/iygh-score.ly

setup_brass: $(SKETCH_DIR)/brass.ly 
	@ mkdir -p $(BUILD_DIR)
	@ cp $(SKETCH_DIR)/brass.ly $(BUILD_DIR)
	@ cp $(SCORE_DIR)/iygh-score.ly $(BUILD_DIR)


sketches: $(SKETCHES)

# compile sketches
$(SKETCH_DIR)/%.ly: $(SRC_DIR)/%.py
	@ printf "%8s %-40s %s\n" $(PYTHON) $<
	@ mkdir -p $(SKETCH_DIR)
	@ $(PYTHON) $< > $@

clean:
	rm -rf $(BUILD_DIR) 

clean_sketches:
	rm -rf $(SKETCH_DIR)

.PHONY: default clean
