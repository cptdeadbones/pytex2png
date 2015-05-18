import pytex2png, os

# runs examples
def main():
	
	# grab all the files in examples folder
	files = os.listdir("examples")
	
	# go through and run convert method on each file
	for file in files:
		pytex2png.convert("examples/"+file,"output/"+file+".png")

if __name__ == "__main__":
    main()
