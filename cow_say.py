import cowsay
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("message", help="massage that cow says", type=str)
args = parser.parse_args()
cowsay.cow(args.message)
