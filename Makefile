SHELL := /usr/bin/bash
PYTHON := /usr/bin/python3

EXAMPLES_DIR := examples

EXAMPLES := $(wildcard $(EXAMPLES_DIR)/*.py) 
OBJECTS := $(addprefix $(BUILD_DIR)/, $(notdir $(SOURCES:.py=.ly)))

BUILD_DIR := build

default: score.pdf

score.pdf: bassoon_example copy_score
	@ lilypond -o $(BUILD_DIR)/score $(BUILD_DIR)/score.ly

# Copy lilypond score to build_dir 
copy_score: 
	@ mkdir -p $(BUILD_DIR)
	@ cp $(EXAMPLES_DIR)/score.ly $(BUILD_DIR)

venv/bin/activate: requirements.txt 
	python3 -m venv venv
	./venv/bin/pip install -e .
	./venv/bin/pip install -r requirements.txt

bassoon_example: venv/bin/activate
	mkdir -p $(BUILD_DIR)
	./venv/bin/python3 $(EXAMPLES_DIR)/bassoon.py > $(BUILD_DIR)/bassoon.ly

clean:
	rm -rf $(BUILD_DIR) 

.PHONY: default clean
