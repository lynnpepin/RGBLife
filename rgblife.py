import argparse
import tools


def _print_border(width):
    border = "="*width
    print(border)

def _save_iteration(savename, save_board, iteration, max_iterations):
    if (savename):
        filename = savename[0]
        num_digits = len(str(max_iterations))
        filename += "_" + str(iteration).zfill(num_digits) + ".png"
        tools.save_as_pic(save_board, filename)


def run(loadname, iterations, printeach, printonce, savename):
    #main(args.loadpic, args.iterate, args.print, args.printonce, ags.savepic)
    board = tools.pic_to_board(loadname[0])

    if (iterations):
        num_iterations = iterations[0]
    else:
        num_iterations = 1

    if (printeach or printonce):
        _print_border(board.size()[0])

    for ii in range(0,num_iterations):
        _save_iteration(savename, board, ii, num_iterations)
        if(printeach):
            print(tools.board_to_string(board))
            _print_border(board.size()[0])
        board.iterate_board()

    # TODO: Add board-stale-checking feature

    _save_iteration(savename, board,num_iterations,num_iterations)

    if (printeach or printonce):
        print(tools.board_to_string(board))
        _print_border(board.size()[0])
        print("Finished after",board.generation(),"generations.")

def main():
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
    run(args.loadpic, args.iterate, args.print, args.printonce, args.savepic)


if __name__ == '__main__':
    main()
