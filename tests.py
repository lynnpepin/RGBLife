import unittest
from PIL import Image
from cells import *
import Board
import tools


class CellsTest(unittest.TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
        
    def test_prey(self):
        self.assertEqual(prey(R),G)
        self.assertEqual(prey(G),B)
        self.assertEqual(prey(B),R)
        
    def test_predator(self):
        self.assertEqual(predator(R),B)
        self.assertEqual(predator(G),R)
        self.assertEqual(predator(B),G)
        
    def is_like(cell,neighbour):
        self.assertTrue(is_like(R,R))
        self.assertTrue(is_like(G,G))
        self.assertTrue(is_like(B,B))
        
        self.assertFalse(is_like(R,B))
        self.assertFalse(is_like(R,G))
        self.assertFalse(is_like(B,R))
        self.assertFalse(is_like(B,G))
        self.assertFalse(is_like(G,R))
        self.assertFalse(is_like(G,B))


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.initial_data = [ [G,R,B,E],[R,E,R,B],[E,E,E,E],[R,E,E,E] ]
        self.next_data    = [ [R,E,B,E],[E,E,E,E],[E,E,E,E],[E,E,E,E] ]
        self.empty_data   = [ [E,E,E,E],[E,E,E,E],[E,E,E,E],[E,E,E,E] ]
        self.other_data   = [ [R,R,R,R],[G,G,G,G],[B,B,B,B],[E,E,E,E] ]
        self.board = Board(4,4, self.initial_data)

    def tearDown(self):
        pass

    def test_data(self):
        self.assertEqual(self.initial_data, self.board.data)
        
    def test_generation(self):
        self.assertEqual(0, self.board.generation)

    def test_iterate(self):
        self.assertEqual(0, self.board.generation)

        self.board.iterate()
        self.assertEqual(self.next_data, self.board.data)
        self.assertEqual(1, self.board.generation)

        self.board.iterate()
        self.assertEqual(self.empty_data, self.board.data)
        self.assertEqual(2, self.board.generation)

        board.iterate()
        self.assertEqual(self.empty_data, self.board.data)
        self.assertEqual(3, self.board.generation())

    def test_clear(self):
        self.board.iterate()
        self.board.iterate()
        self.board.clear()
        self.assertEqual(self.empty_data, self.board.data)
        self.assertEqual(0, self.board.generation())

    def test_set_board(self):
        self.board.iterate()
        self.board.set_board(self.other_data)
        self.assertEqual(0, self.board.generation())
        self.assertEqual(self.other_data, self.board.data)


class ToolsTest(unittest.TestCase):
    def setUp(self):
        self.initial_data = [ [G,R,B,E],[R,E,R,B],[E,E,E,E],[R,E,E,E] ]
        self.next_data    = [ [R,E,B,E],[E,E,E,E],[E,E,E,E],[E,E,E,E] ]
        self.empty_data   = [ [E,E,E,E],[E,E,E,E],[E,E,E,E],[E,E,E,E] ]
        self.other_data   = [ [R,R,R,R],[G,G,G,G],[B,B,B,B],[E,E,E,E] ]
        self.board = Board(4,4, self.initial_data)

        self.input_image = "input.png"
        self.output_image = "output.png"
        self.initial_data_string = "GRBE\nRERB\nEEEE\nREEE"

    def tearDown(self):
        pass

    def test_pic_to_board(self):
        self.newboard = Tools.pic_to_board(self.input_image)
        self.assertEqual(self.initial_data, self.newboard.data)

    def test_save_as_pic(self):
        Tools.save_as_pic(self.newboard, "0.png")
        
        saved_image = Image.open("0.png").convert("RGB")
        comparison_image = Image.open(self.output_image).convert("RGB")
        
        assertEqual(saved_image.getdata(), comparison_image.getdata())
        
        saved_image.close()
        comparison_image.close()

    def test_board_to_string(self):
        self.assertEqual(self.initial_data_string, Tools.board_to_string(self.board.data))


if (__name__ == "__main__"):
    cells_suite = unittest.TestLoader().loadTestsFromTestCase(CellsTest)
    unittest.TextTestRunner(verbosity=2).run(cells_suite)

    board_suite = unittest.TestLoader().loadTestsFromTestCase(BoardTest)
    unittest.TextTestRunner(verbosity=2).run(board_suite)

    tools_suite = unittest.TestLoader().loadTestsFromTestCase(ToolsTest)
    unittest.TextTestRunner(verbosity=2).run(tools_suite)

