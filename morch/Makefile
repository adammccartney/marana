SHELL := /usr/bin/bash
PYTHON := ../../venv/bin/python3

INSTRUMENTS_DIR := instruments
SCORE_DIR := score

INSTRUMENTS := $(wildcard $(INSTRUMENTS_DIR)/*.py) 
OBJECTS := $(addprefix $(BUILD_DIR)/, $(notdir $(SOURCES:.py=.ly)))

BUILD_DIR := build

default: $(BUILD_DIR)/score.pdf

$(BUILD_DIR)/score.pdf: bassoon_example copy_score
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

clean:
	rm -rf $(BUILD_DIR) 

.PHONY: default clean
