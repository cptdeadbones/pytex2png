# Make file for latex cpp l2p.cpp coverer

TARGET = tex2png

all:  
	g++ -o $(TARGET) -w ./source/l2p.cpp

clean:
	$(RM) $(TARGET)