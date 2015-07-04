all: ascii_image.py textedit.py

ascii_image.py: ascii_image.ui
	pyuic ascii_image.ui -o ascii_image.py -x

textedit.py: textedit.ui
	pyuic textedit.ui    -o textedit.py -x

clean:
	rm -f ascii_image.py
