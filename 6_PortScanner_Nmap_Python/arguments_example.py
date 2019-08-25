import argparse

#Adding Description for -h argument
parser = argparse.ArgumentParser(description='This is a sample example File')

parser.add_argument('--a', action = "store", dest = "aaa", required=True)

args = parser.parse_args()

myDefinedVar = args.aaa

print "Hello "+myDefinedVar+"....."
