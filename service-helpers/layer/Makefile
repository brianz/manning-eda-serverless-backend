TARGET_DIR = $(ARTIFACTS_DIR)/python

# cp *.py $(TARGET_DIR)

build-TicTacToeLayer:
	mkdir -p $(TARGET_DIR)
	python -m pip install -r requirements.txt -t $(TARGET_DIR)
	find $(TARGET_DIR) -name __pycache__ | xargs rm -rf
	find $(TARGET_DIR) -name 's3transfer*' | xargs rm -rf
.PHONY: build-TicTacToeLayer