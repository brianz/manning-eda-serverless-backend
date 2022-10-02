TARGET_DIR = $(ARTIFACTS_DIR)/python


build-CommonServicesLayer: requirements foodie2ue
.PHONY: build-TicTacToeLayer

requirements:
	mkdir -p $(TARGET_DIR)
	python -m pip install -r requirements.txt -t $(TARGET_DIR)
	find $(TARGET_DIR) -name __pycache__ | xargs rm -rf
	find $(TARGET_DIR) -name 's3transfer*' | xargs rm -rf
.PHONY: requirements

foodie2ue:
	cp -r foodie2ue $(TARGET_DIR)
.PHONY: foodie2ue
