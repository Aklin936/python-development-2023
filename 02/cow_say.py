import cowsay
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("message", help="massage that cow says", type=str)
parser.add_argument("-l", help="list of creatures can be used", action = "store_true" )
args = parser.parse_args()
if args.l:
    cowsay.list_cows(args.message)
else:
    cowsay.cow(args.message)
