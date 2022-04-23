SHELL := /usr/bin/bash
PYTHON := ../../venv/bin/python3

INSTRUMENTS_DIR := instruments
SCORE_DIR := score
SRC_DIR := src
SKETCH_DIR := sketch
BUILD_DIR := build
SEGMENTS_DIR := $(BUILD_DIR)/segments

SOURCES         := $(wildcard $(SRC_DIR)/*.py)
SCORE_TEMPLATES := $(wildcard $(SCORE_DIR)/*.ly)
SKETCHES        := $(addprefix $(SKETCH_DIR)/, $(notdir $(SOURCES:.py=.ly)))

default: scores
setup: sketches copy_score_templates copy_segments 

# Compile components ##########################################################
#
sketches: $(SKETCHES)
# compile sketches
$(SKETCH_DIR)/%.ly: $(SRC_DIR)/%.py
	@ printf "%8s %-40s %s\n" $(PYTHON) $<
	@ mkdir -p $(SKETCH_DIR)
	@ $(PYTHON) $< > $@

# Link step ###################################################################
# 
#
SCORES          := $(addprefix $(BUILD_DIR)/, $(notdir $(SCORE_TEMPLATES:.ly=)))
scores: setup $(SCORES)
# link the sketches (segments) to the scores
$(BUILD_DIR)/%: $(BUILD_DIR)/%.ly
	@ printf "%8s %-40s %s\n" lilypond $<
	@ lilypond -o $@ $<

# Setup scripts ##############################################################
# Copy lilypond score to build_dir 
copy_score_templates: build_dirs
	@ $(foreach score,$(SCORE_TEMPLATES),$(shell cp $(score) ./build/))

copy_segments: build_dirs
	@ $(foreach sketch,$(SKETCHES),$(shell cp $(sketch) ./build/segments/))

build_dirs:
	@ mkdir -p build build/segments

clean: clean_sketches
	rm -rf $(BUILD_DIR) 

clean_sketches:
	rm -rf $(SKETCH_DIR)

.PHONY: clean setup scores sketches
