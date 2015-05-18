# PyTex2png 


PyTex2png is a Latex to png convertor. It uses a c++ module written by Bruno Bachelet and published under GPL-Licensed. The code runs as an online tool and the source code is avilable [Here](http://www.nawouak.net/?cat=informatics.tex2png+lang=en). The Python extentions uses command line calls to communicate with `tex2png`. 

## Usage

+ Before you can run the code, you will to run a `make` command. The `tex2png` binary provided was compilied using *gcc version 4.2.1 (Apple Inc. build 5666) (dot 3)*. I would recommand recomiling using the `Makefile` to fit your arcitcture.

+ To run the code issue the command: 

```python
    python pytex2png pytex.py <latex_source_file_path> <png_output_path> [BOOLEAN]
```

### Running the example code


In the `examples` folder you will find multiple text files contating LaTeX code. The file `examples.py` will convert every file in the `examples` folder and covert the LaTeX code to a png file. The output png file will have transperant background and white text. You can see the examples code output in the `output` folder. To run the example issue this command:

```python
    python example.py
```

## Disclaimers


1. This code was devloped and tested on a Linux based system. I have no idea if it will work on another system. If you have tested it on another system, please let me know. 
2. I have tested the script on a select few LaTeX snippets. It might not work for every Math LaTeX command. From the sample I selected it worked on all. 

## License

This code is distrubted under the [GNU General Public License](http://www.gnu.org/copyleft/gpl.html)

## ToDo 

- Make the background color customiziable
- Make the output text code customiziable
- Create a setup file
- Port the code to non-Linux machines

## Contact 

If you have any private comments you can email me: cpt@thelivingpearl.com

Another [LivingPearl Project](http://www.thelivingpearl.com)

