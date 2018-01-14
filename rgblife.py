import argparse
import tools

parser = argparse.ArgumentParser(description='Three-species game of life variant.')
parser.add_argument("loadpic",
                    help="Load an image of the board from a filename",
                    type=str, nargs=1)
parser.add_argument("--savepic","-s",
                    help="save an image to the directory, appended _xxx.png",
                    type=str, nargs=1)
parser.add_argument("--iterate","-i",
                    help="iterate n times. Default 1.",
                    type=int, nargs=1)
parser.add_argument("--print","-p",
                    help="Print the board to console during each iteration.",
                    action="store_true")
parser.add_argument("--printonce",
                    help="Print the board to console after the final iteration.",
                    action="store_true")

args = parser.parse_args()


def _print_border(width):
    border = "="*width
    print(border)

def _save_iteration(save_board, iteration, max_iterations):
    if (args.savepic):
        filename = args.savepic[0]
        num_digits = len(str(max_iterations))
        filename += "_" + str(iteration).zfill(num_digits) + ".png"
        tools.save_as_pic(save_board, filename)


board = tools.pic_to_board(args.loadpic[0])

if (args.iterate):
    num_iterations = args.iterate[0]
else:
    num_iterations = 1


if(args.print or args.printonce):
    _print_border(board.size()[0])

for ii in range(0,num_iterations):
    _save_iteration(board,ii,num_iterations)
    if(args.print):
        print(tools.board_to_string(board))
        _print_border(board.size()[0])
    board.iterate_board()
# TODO: Check if board goes stale; if so, stop

_save_iteration(board,num_iterations,num_iterations)

if (args.print or args.printonce):
    print(tools.board_to_string(board))
    print_border(board.size()[0])
    print("Finished after",board.generation(),"generations.")


