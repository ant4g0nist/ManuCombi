import os
import sys
import argparse
import ManuCombi


def fuzz_(ext, folder, count):
	f=open(folder+'/'+str(count)+'.'+ext,'w')
	f.write(fbruter._permute())
	f.close()

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--sample", help="sample file to fuzz", action="store", required=True)
	parser.add_argument("-r", "--round", help="combination round", action="store", required=False)
	parser.add_argument("-e", "--ext", help="extension of sample file", action="store", required=True)
	parser.add_argument("-o", "--output", help="output folder to save samples", action="store", required=True)
	parser.add_argument("-v", "--version", action="version", version="You are running {0}".format(ManuCombi.__version__))

	args = parser.parse_args()
	sample = args.sample
	output_folder = args.output
	ext = args.ext

	try:
		os.mkdir(output_folder)
	except Exception as e:
		raise e

	count = 0

	if args.round:
		fbruter = ManuCombi.ManuCombi(sample,int(args.round))
	else:
		fbruter = ManuCombi.ManuCombi(sample)

	done = False
	while not done:
		fuzz_(ext,output_folder,count)
		count+=1

