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
PARTS_INCLUDE   := $(PARTS_DIR)/segments.ily

.PHONY: parts segments clean

all: dist 

default: all

dist: score parts score-dist
	rm $(BUILD_DIR)/parts/*.ly
	rm $(BUILD_DIR)/*.ly
	rm $(BUILD_DIR)/*.ily
	rm -rf $(BUILD_DIR)/segments
	rm $(BUILD_DIR)/lilypond.sh
	rm $(BUILD_DIR)/parts/*.ily
	rm $(BUILD_DIR)/score.pdf

score-dist: dist.org
	@ emacs $< --batch -f org-latex-export-to-pdf 
	@ mv dist.pdf $(BUILD_DIR)/marana-score.pdf
	@ rm dist.tex*
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
	@ cp $(PARTS_INCLUDE) $(BUILD_DIR)/parts
	@ cp scripts/lilypond.sh $(BUILD_DIR)

build_dir:
	@ mkdir -p build/segments build/parts

clean: 
	rm -rf $(BUILD_DIR) 
	rm dist.tex dist.pdf
