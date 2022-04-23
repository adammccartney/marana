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
MUSIC_TEMPLATES := $(wildcard $(SCORE_DIR)/*.ily)
SEGMENTS        := $(addprefix $(SEGMENTS_DIR)/, $(notdir $(SOURCES:.py=.ily)))


PARTS := flute1 flute2 oboe1 oboe2 clarinet1 clarinet2 bassoon

PARTS_PDF := $(foreach p, $(PARTS), parts-$(p).pdf)

default: score

# Generate segments ############################################################
#
segments: setup $(SEGMENTS) 
# compile sketches
$(SEGMENTS_DIR)/%.ily: $(SRC_DIR)/%.py
	@ printf "%8s %-40s %s\n" $(PYTHON) $<
	@ mkdir -p $(SEGMENTS_DIR)
	@ $(PYTHON) $< > $@

# Link step ###################################################################
#
score: setup segments $(BUILD_DIR)/score
# link the sketches (segments) to the scores
$(BUILD_DIR)/score: $(BUILD_DIR)/score.ly
	@ printf "%8s %-40s %s\n" lilypond $<
	@ lilypond -o $@ $<



# Setup scripts ##############################################################
# Copy lilypond score to build_dir 
setup: cp_mutemplates 
	@ cp score/score.ly $(BUILD_DIR)

cp_mutemplates: build_dir
	@ $(foreach ily,$(MUSIC_TEMPLATES),$(shell cp $(ily) $(BUILD_DIR)))

build_dir:
	@ mkdir -p build/segments

clean: clean_sketches
	rm -rf $(BUILD_DIR) 

clean_sketches:
	rm -rf $(SKETCH_DIR)

.PHONY: clean setup scores sketches
