SHELL := /usr/bin/bash
PYTHON := ../../venv/bin/python3

INSTRUMENTS_DIR := instruments
SCORE_DIR := score
PARTS_DIR := parts

SRC_DIR := src
BUILD_DIR := build
SEGMENTS_DIR := $(BUILD_DIR)/segments

SOURCES         := $(wildcard $(SRC_DIR)/*.py)
LY_ASSETS       := $(wildcard $(SCORE_DIR)/*.ly)
MUSIC_TEMPLATES := $(wildcard $(SCORE_DIR)/*.ily)
PARTS           := $(wildcard $(PARTS_DIR)/*.ly)
SEGMENTS        := $(addprefix $(SEGMENTS_DIR)/, $(notdir $(SOURCES:.py=.ily)))
PARTS_PDF       := $(addprefix $(BUILD_DIR)/$(PARTS_DIR)/, $(notdir $(PARTS:.ly=)))

.PHONY: parts segments clean

all: stringcanon wwindchorale iygh parts

default: all

# Generate segments ############################################################
#
segments: setup $(SEGMENTS) 
# compile segments
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


iygh: $(BUILD_DIR)/iygh-score segments
$(BUILD_DIR)/iygh-score: $(BUILD_DIR)/iygh-score.ly
	@ printf "%8s %-40s %s\n" lilypond $<
	@ lilypond -o $@ $<


stringcanon: $(BUILD_DIR)/stringcanon segments
$(BUILD_DIR)/stringcanon: $(BUILD_DIR)/stringcanon.ly
	@ printf "%8s %-40s %s\n" lilypond $<
	@ lilypond -o $@ $<


wwindchorale: $(BUILD_DIR)/wwindchorale segments
$(BUILD_DIR)/wwindchorale: $(BUILD_DIR)/wwindchorale.ly
	@ printf "%8s %-40s %s\n" lilypond $<
	@ lilypond -o $@ $<


parts: $(PARTS_PDF) score

$(BUILD_DIR)/parts/%: $(PARTS_DIR)/%.ly
	@ lilypond -o $@ $<  

# Setup scripts ##############################################################
# Copy lilypond score to build_dir 
setup: cp_assets 
	@ $(foreach asset,$(LY_ASSETS),$(shell cp $(asset) $(BUILD_DIR)))

cp_assets: build_dir
	@ $(foreach ily,$(MUSIC_TEMPLATES),$(shell cp $(ily) $(BUILD_DIR)))
	@ $(foreach p,$(PARTS),$(shell cp $(p) $(BUILD_DIR)/parts))
	@ cp scripts/lilypond.sh $(BUILD_DIR)

build_dir:
	@ mkdir -p build/segments build/parts

clean: 
	rm -rf $(BUILD_DIR) 
