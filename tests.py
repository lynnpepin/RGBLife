import unittest
from PIL import Image
from cells import *
from Board import Board
import tools


class CellsTest(unittest.TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
    
    def test_to_rgb(self):
        self.assertEqual((255,255,255),to_rgb(E))
        self.assertEqual((255,0,0),to_rgb(R))
        self.assertEqual((0,255,0),to_rgb(G))
        self.assertEqual((0,0,255),to_rgb(B))
    
    def test_from_rgb(self):
        self.assertEqual(E,from_rgb(255,255,255))
        self.assertEqual(R,from_rgb(255,0,0))
        self.assertEqual(G,from_rgb(0,255,0))
        self.assertEqual(B,from_rgb(0,0,255))
    
    def test_to_string(self):
        self.assertEqual(to_string(E)," ")
        self.assertEqual(to_string(R),"R")
        self.assertEqual(to_string(G),"G")
        self.assertEqual(to_string(B),"B")
        
    def test_is_prey(self):
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

    def test_iterate_cell(self):
        # Overpopulation
        self.assertEqual(iterate_cell(R, [R,R,R,R]), E)
        self.assertEqual(iterate_cell(G, [G,G,G,G]), E)
        self.assertEqual(iterate_cell(B, [B,B,B,B]), E)
        
        # Survival
        self.assertEqual(iterate_cell(R, [R,R,R,E]), R)
        self.assertEqual(iterate_cell(G, [G,E,G,G]), G)
        self.assertEqual(iterate_cell(B, [E,B,B,E]), B)
        
        self.assertEqual(iterate_cell(R, [R,G,G,R]), R)
        self.assertEqual(iterate_cell(G, [B,G,B,G]), G)
        self.assertEqual(iterate_cell(B, [B,B,R,R]), B)

        self.assertEqual(iterate_cell(R, [R,R,R,B]), R)
        self.assertEqual(iterate_cell(G, [G,G,R,G]), G)
        self.assertEqual(iterate_cell(B, [G,B,B,B]), B)

        self.assertEqual(iterate_cell(R, [R,G,G,B]), R)
        self.assertEqual(iterate_cell(G, [B,G,R,G]), G)
        self.assertEqual(iterate_cell(B, [G,B,R,B]), B)

        # Conversion
        self.assertEqual(iterate_cell(R, [B,B,R,E]), B)
        self.assertEqual(iterate_cell(G, [R,R,R,G]), R)
        self.assertEqual(iterate_cell(B, [B,G,G,G]), G)

        # Starvation
        self.assertEqual(iterate_cell(R, [E,E,R,E]), E)
        self.assertEqual(iterate_cell(G, [G,E,E,E]), E)
        self.assertEqual(iterate_cell(B, [E,E,E,R]), E)
        self.assertEqual(iterate_cell(R, [E,E,E,E]), E)

        # Dead cells
        self.assertEqual(iterate_cell(E, [R,R,G,E]), R)
        self.assertEqual(iterate_cell(E, [G,E,G,G]), G)
        self.assertEqual(iterate_cell(E, [R,R,G,B]), E)
        
        self.assertEqual(iterate_cell(E, [R,R,B,E]), B)
        self.assertEqual(iterate_cell(E, [R,B,B,E]), B)
        self.assertEqual(iterate_cell(E, [B,B,B,E]), B)

        self.assertEqual(iterate_cell(E, [E,E,R,R]), E)
        self.assertEqual(iterate_cell(E, [R,G,E,E]), E)
        self.assertEqual(iterate_cell(E, [E,E,E,E]), E)
        
        self.assertEqual(iterate_cell(E, [B,B,G,E]), G)


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.initial_data = [ [G,R,E,R],[R,E,E,E],[B,R,E,E],[E,B,E,E] ]
        self.next_data    = [ [R,E,E,E],[E,R,E,E],[B,E,E,E],[G,B,E,E] ]
        self.second_data  = [ [E,B,E,E],[B,E,E,E],[E,B,E,E],[E,E,E,E] ]
        self.third_data   = [ [E,E,E,E],[E,B,E,E],[E,E,E,E],[E,E,E,E] ]
        self.empty_data   = [ [E,E,E,E],[E,E,E,E],[E,E,E,E],[E,E,E,E] ]
        self.other_data   = [ [R,R,R,R],[G,G,G,G],[B,B,B,B],[E,E,E,E] ]
        self.board = Board(4,4, self.initial_data)

    def tearDown(self):
        pass

    def test_data(self):
        self.assertEqual(self.board.data()[0][0],G)
        self.assertEqual(self.board.data()[0][1],R)
        self.assertEqual(self.board.data()[1][0],R)
        self.assertEqual(self.board.data()[1][1],E)
        self.assertEqual(self.board.data()[2][0],B)

    def test_get_neighbours(self):
        self.assertEqual(
            self.board._get_neighbours(0,0,self.initial_data),
            [R,R,R,E])
        self.assertEqual(
            self.board._get_neighbours(0,3,self.initial_data),
            [E,E,G,E])
        self.assertEqual(
            self.board._get_neighbours(3,0,self.initial_data),
            [E,G,B,B])
        self.assertEqual(
            self.board._get_neighbours(3,3,self.initial_data),
            [E,R,E,E])
        self.assertEqual(
            self.board._get_neighbours(1,1,self.initial_data),
            [R,R,E,R])
        self.assertEqual(
            self.board._get_neighbours(2,1,self.initial_data),
            [B,B,E,E])
        self.assertEqual(
            self.board._get_neighbours(1,2,self.initial_data),
            [E,E,E,E])
        self.assertEqual(
            self.board._get_neighbours(2,2,self.initial_data),
            [R,E,E,E])

    def test_data(self):
        self.assertEqual(self.initial_data, self.board.data())
        
    def test_generation(self):
        self.assertEqual(0, self.board.generation())

    def testiterate_board(self):
        self.assertEqual(self.initial_data, self.board.data())
        self.assertEqual(0, self.board.generation())

        self.board.iterate_board()
        self.assertEqual(self.next_data, self.board.data())
        self.assertEqual(1, self.board.generation())

        self.board.iterate_board()
        self.assertEqual(self.second_data, self.board.data())
        self.assertEqual(2, self.board.generation())

        self.board.iterate_board()
        self.assertEqual(self.third_data, self.board.data())
        self.assertEqual(3, self.board.generation())

        self.board.iterate_board()
        self.assertEqual(self.empty_data, self.board.data())
        self.assertEqual(4, self.board.generation())

    def test_clear(self):
        self.board.iterate_board()
        self.board.iterate_board()
        self.board.clear()
        self.assertEqual(self.empty_data, self.board.data())
        self.assertEqual(0, self.board.generation())

    def test_set_board(self):
        self.board.iterate_board()
        self.board.set_board(self.other_data)
        self.assertEqual(0, self.board.generation())
        self.assertEqual(self.other_data, self.board.data())
    
    def test_size(self):
        self.assertEqual((4,4),self.board.size())
        self.board.set_board(([R,R,R],[R,R,R]))
        self.assertEqual((2,3),self.board.size())


class ToolsTest(unittest.TestCase):
    def setUp(self):
        self.initial_data = [ [G,R,E,R],[R,E,E,E],[B,R,E,E],[E,B,E,E] ]
        self.board = Board(4,4, self.initial_data)

        self.input_image = "input.png"
        self.initial_data_string = "GR R\nR   \nBR  \n B  "

    def tearDown(self):
        pass

    def test_pic_to_board(self):
        self.newboard = tools.pic_to_board(self.input_image)
        self.assertEqual(self.initial_data, self.newboard.data())

    def test_save_as_pic(self):
        tools.save_as_pic(self.board, "0.png")
        
        saved_image = Image.open("0.png").convert("RGB")
        comparison_image = Image.open(self.input_image).convert("RGB")
        
        self.assertEqual(
            list(saved_image.getdata()), list(comparison_image.getdata()) )
        
        saved_image.close()
        comparison_image.close()

    def test_board_to_string(self):
        self.assertEqual(self.initial_data_string, tools.board_to_string(self.board))


if (__name__ == "__main__"):
    cells_suite = unittest.TestLoader().loadTestsFromTestCase(CellsTest)
    unittest.TextTestRunner(verbosity=2).run(cells_suite)

    board_suite = unittest.TestLoader().loadTestsFromTestCase(BoardTest)
    unittest.TextTestRunner(verbosity=2).run(board_suite)

    tools_suite = unittest.TestLoader().loadTestsFromTestCase(ToolsTest)
    unittest.TextTestRunner(verbosity=2).run(tools_suite)

