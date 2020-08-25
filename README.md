# kivy-builder-test
Test of kivy packaging with builder.load_file

Original Error:

	Traceback (most recent call last):
		File "main.py", line 5, in <module>
		File "kivy\lang\builder.py", line 288, in load_file
		FileNotFoundError: [Errno 2] No such file or directory: 'sub.kv'
		[4680] Failed to execute script main

Fixed with a change as noted to main.py and buildertest.spec
