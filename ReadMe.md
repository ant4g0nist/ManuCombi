ManuCombi
	- Mutates and generates files with all possible combinations of fuzzed bytes in the file.

Usage:
	
	~/ManuCombi ❯❯❯ python combin.py -h

	usage: combin.py [-h] -s SAMPLE [-r ROUND] -e EXT -o OUTPUT [-v]

	optional arguments:
	  -h, --help            show this help message and exit
	  -s SAMPLE, --sample SAMPLE
	                        sample file to fuzz
	  -r ROUND, --round ROUND
	                        combination round
	  -e EXT, --ext EXT     extension of sample file
	  -o OUTPUT, --output OUTPUT
	                        output folder to save samples
	  -v, --version         show program's version number and exit

	~/ManuCombi ❯❯❯ python combin.py -s Sample.xls -o op -e xls
	[+]	Going through round 1

	~/ManuCombi ❯❯❯ python combin.py -s Sample.xls -o op -e xls -r 3
	[+]	Going through round 3

- thanks for bearing the with my dumb ass code