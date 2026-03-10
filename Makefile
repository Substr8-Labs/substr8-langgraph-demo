.PHONY: demo install verify clean

demo: install
	@python demo_agent.py
	@substr8 proof verify runproof.json

install:
	@pip install -r requirements.txt -q
	@pip install substr8 -q

verify:
	@substr8 proof verify runproof.json

clean:
	@rm -f runproof.json
