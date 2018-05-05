import sys
# from outter import load_outter_method

print("module inner loaded")

if __name__ == "__main__":
	print("module __main__ method excuted")
	print("package name:",__package__)
	print("package name:",__name__)
	print("path:",sys.path)

	# load_outter_method()