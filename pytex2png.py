# imports
import shlex, subprocess, sys

# runs a command line command and waits for it to complete
# by default it will not display any output
def exe_command(cmd, display=False):
	args = shlex.split(cmd)
	if(display):
		p = subprocess.Popen(args)
	else:
		p = subprocess.Popen(args,stdout=subprocess.PIPE)
	p.wait() 
	
# read file content as a single variable
def get_file(filename):
	file = open(filename, "r")
	lines = file.read()
	file.close()
	return lines

# create png from latex
def make_png(data,image,display):
	if(display): print "Making image..."
	command_line = "./tex2png -r* -lq \""+data+"\" " + image
	exe_command(command_line,display)

# remove white background
def make_transparent_bg(image,display):
	if(display): print "Removing white background..."
	command_line = "convert "+image+" -channel rgba -fill \"rgba(255,255,255,0)\" -opaque \"rgb(255,255,255)\" " + image
	exe_command(command_line)

# convert output text to white
def make_white_text(image,display):
	if(display): print "Converting output image text to white..."
	command_line = "convert "+image+" -channel rgb -fill \"rgba(255,255,255)\" -opaque \"rgb(0,0,0)\" " + image
	exe_command(command_line)

# function to make call if not using module as driver
def convert(source,output,display=False):
	if(display): print "Coverting LaTeX from " + source + " to " + output
	data = get_file(source).replace("\\","\\\\")
	make_png(data,output,display)
	make_transparent_bg(output,display)
	make_white_text(output,display)

# main function
def main(args): 
	
	# handle command line args usage
	if(len(args) < 2) or (len(args) > 3):
		print "usage: pytex.py <latex_source_file_path> <png_output_path> [BOOLEAN]"
	else:
	
		# check if display flag is set
		if (len(args) == 3):
			try:
				display = eval(args[-1])
				if(display not in (True,False)): raise Exception()
			except:
				print "ERROR! -display option must take a True or False value only"
				quit()
			
			# make the conversation call if display is True
			convert(args[0],args[1],display)
		
		else:
		
			# make the conversation call if display is False
			convert(args[0],args[1])
		
if __name__ == "__main__":
    main(sys.argv[1:])
