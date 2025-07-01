import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')

add_parser = subparsers.add_parser('add', help='Add two numbers')
add_parser.add_argument('--a', type=int, required=True)
add_parser.add_argument('--b', type=int, required=True)

subtract_parser = subparsers.add_parser('subtract', help='Subtract two numbers')
subtract_parser.add_argument('--a', type=int, required=True)
subtract_parser.add_argument('--b', type=int, required=True)

args = parser.parse_args()

if args.command == 'add':
    print(args.a + args.b)
elif args.command == 'subtract':
    print(args.a - args.b)


