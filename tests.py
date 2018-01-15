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
        self.assertEqual(E,from_rgb((255,255,255))  )
        self.assertEqual(R,from_rgb((255,0,0)))
        self.assertEqual(G,from_rgb((0,255,0)))
        self.assertEqual(B,from_rgb((0,0,255)))
    
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

    def test_classcount_test(self):
        self.assertEqual(classcount([R,E,G,B,B,R,E,R]),[3,1,2])
        self.assertEqual(classcount([R,R,R,R,G,G,B,E]),[4,2,1])
        self.assertEqual(classcount([E,E,E,E,E,E,E,E]),[0,0,0])
        self.assertEqual(classcount([R,R,R,R,R,R,R,E]),[7,0,0])
        self.assertEqual(classcount([G,E,G,E,G,E,G,E]),[0,4,0])
        self.assertEqual(classcount([E,E,E,B,E,B,E,B]),[0,0,3])
        
    def test_iterate_cell(self):
        # Old unit tests, adapted from iterate_cell(cell, neighbours)
        # to iterate_cell(cell, counts), where counts
        # Overpopulation    Like >= 4
        self.assertEqual(iterate_cell(R, classcount([R,R,R,R,E,E,E,E])), E)
        self.assertEqual(iterate_cell(R, classcount([R,R,R,R,G,G,G,G])), E)
        self.assertEqual(iterate_cell(G, classcount([G,G,G,G,E,E,E,E])), E)
        self.assertEqual(iterate_cell(G, classcount([G,G,G,G,R,R,R,R])), E)
        self.assertEqual(iterate_cell(B, classcount([B,B,B,B,E,E,E,E])), E)
        self.assertEqual(iterate_cell(B, classcount([B,B,B,B,B,B,B,B])), E)

        ##Encroachment      Pred >= Prey + Like + 1
        # Conversion        Pred >= Prey + Like + 2 
        self.assertEqual(iterate_cell(G, classcount([R,R,R,E,E,E,E,E])), R)
        self.assertEqual(iterate_cell(B, classcount([G,G,G,G,G,B,B,R])), G)
        self.assertEqual(iterate_cell(R, classcount([B,B,B,B,B,B,B,B])), B)
        # Stifling          Encroachmnt, but not conversion
        self.assertEqual(iterate_cell(R, classcount([B,B,B,R,G,E,E,E])), E)
        self.assertEqual(iterate_cell(G, classcount([R,R,R,R,G,G,G,E])), E)
        self.assertEqual(iterate_cell(B, classcount([B,B,R,G,E,G,G,G])), E)
        
        # Survival
        self.assertEqual(iterate_cell(R, classcount([R,R,R,E,E,E,E,E])), R)
        self.assertEqual(iterate_cell(G, classcount([G,E,E,G,E,E,E,E])), G)
        self.assertEqual(iterate_cell(B, classcount([E,B,B,E,E,E,E,E])), B)
        
        self.assertEqual(iterate_cell(R, classcount([R,G,G,R,E,E,E,E])), R)
        self.assertEqual(iterate_cell(G, classcount([B,G,B,G,E,E,E,E])), G)
        self.assertEqual(iterate_cell(B, classcount([B,B,R,R,E,E,E,E])), B)

        self.assertEqual(iterate_cell(R, classcount([R,G,G,G,G,G,G,G])), R)
        self.assertEqual(iterate_cell(G, classcount([B,G,B,G,B,B,B,B])), G)
        self.assertEqual(iterate_cell(B, classcount([B,B,B,G,R,R,R,R])), B)


        self.assertEqual(iterate_cell(R, classcount([R,R,R,B,E,E,E,E])), R)
        self.assertEqual(iterate_cell(G, classcount([G,G,R,G,E,E,E,E])), G)
        self.assertEqual(iterate_cell(B, classcount([G,B,B,B,E,E,E,E])), B)

        self.assertEqual(iterate_cell(R, classcount([R,G,G,B,E,E,E,E])), R)
        self.assertEqual(iterate_cell(G, classcount([B,G,R,G,E,E,E,E])), G)
        self.assertEqual(iterate_cell(B, classcount([G,B,R,B,E,E,E,E])), B)
        
        ##Dead cells
        # Reproduction      Three neighbours of one kind
        self.assertEqual(iterate_cell(E, classcount([G,E,G,G,E,E,E,E])), G)
        self.assertEqual(iterate_cell(E, classcount([B,B,B,E,E,E,E,E])), B)
        self.assertEqual(iterate_cell(E, classcount([R,R,R,E,E,E,E,E])), R)
        
        # Expansion         pred+prey>=3, 1<=pred<=3
        self.assertEqual(iterate_cell(E, classcount([R,R,G,E,E,E,E,E])), R)
        self.assertEqual(iterate_cell(E, classcount([R,R,B,E,E,E,E,E])), B)
        self.assertEqual(iterate_cell(E, classcount([R,B,B,E,E,E,E,E])), B)
        self.assertEqual(iterate_cell(E, classcount([G,G,G,G,G,R,E,E])), R)
        
        # Remaining dead;
        self.assertEqual(iterate_cell(E, classcount([E,E,R,R,E,E,E,E])), E)
        self.assertEqual(iterate_cell(E, classcount([R,G,E,E,E,E,E,E])), E)
        self.assertEqual(iterate_cell(E, classcount([G,G,G,G,R,R,R,R])), E)
        self.assertEqual(iterate_cell(E, classcount([R,R,G,B,E,E,E,E])), E)
        self.assertEqual(iterate_cell(E, classcount([E,E,E,E,E,E,E,E])), E)
    

class BoardTest(unittest.TestCase):
    def setUp(self):
        self.initial_data = [ [G,R,E,R],[R,E,E,E],[B,R,E,E],[E,B,E,E] ]
        self.iter_01_data = [ [R,R,B,R],[R,E,R,E],[B,E,E,E],[E,B,B,E] ]
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

    def test_get_neighbour_count(self):
        self.assertEqual(
            self.board._get_neighbour_count(0,0,self.initial_data),
            [3,0,1])
        self.assertEqual(
            self.board._get_neighbour_count(0,3,self.initial_data),
            [1,1,0])
        self.assertEqual(
            self.board._get_neighbour_count(3,0,self.initial_data),
            [3,1,2])
        self.assertEqual(
            self.board._get_neighbour_count(3,3,self.initial_data),
            [1,1,1])
        self.assertEqual(
            self.board._get_neighbour_count(1,1,self.initial_data),
            [3,1,1])
        self.assertEqual(
            self.board._get_neighbour_count(2,1,self.initial_data),
            [1,0,2])
        self.assertEqual(
            self.board._get_neighbour_count(1,2,self.initial_data),
            [3,0,0])
        self.assertEqual(
            self.board._get_neighbour_count(2,2,self.initial_data),
            [1,0,1])

    def test_data(self):
        self.assertEqual(self.initial_data, self.board.data())
        
    def test_generation(self):
        self.assertEqual(0, self.board.generation())

    def test_iterate_board(self):
        self.assertEqual(self.initial_data, self.board.data())
        self.assertEqual(0, self.board.generation())

        self.board.iterate_board()
        self.assertEqual(self.iter_01_data, self.board.data())
        self.assertEqual(1, self.board.generation())

        self.board.iterate_board()
        self.assertEqual(2, self.board.generation())

        self.board.iterate_board()
        self.assertEqual(3, self.board.generation())

        self.board.iterate_board()
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
        self.iter_01_data = [ [R,R,B,R],[R,E,R,E],[B,E,E,E],[E,B,B,E] ]
        self.board = Board(4,4, self.initial_data)
        self.input_image = "tests/input.png"
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
        self.assertEqual(
            self.initial_data_string, tools.board_to_string(self.board))


class MoreBoardTest(unittest.TestCase):
    # Board tests that rely on the validity of the tools
    def setUp(self):
        self.img_A_0 = Image.open("tests/test_case_A_0.png").convert("RGB")
        self.img_A_1 = Image.open("tests/test_case_A_1.png").convert("RGB")
        self.img_A_2 = Image.open("tests/test_case_A_2.png").convert("RGB")
        self.img_A_3 = Image.open("tests/test_case_A_3.png").convert("RGB")
        self.board_A  = tools.pic_to_board("tests/test_case_A_0.png")
        self.data_A_0 = tools.pic_to_board("tests/test_case_A_0.png").data()
        self.data_A_1 = tools.pic_to_board("tests/test_case_A_1.png").data()
        self.data_A_2 = tools.pic_to_board("tests/test_case_A_2.png").data()
        self.data_A_3 = tools.pic_to_board("tests/test_case_A_3.png").data()
        
        self.img_B_0 = Image.open("tests/test_case_B_0.png").convert("RGB")
        self.img_B_1 = Image.open("tests/test_case_B_1.png").convert("RGB")
        self.board_B  = tools.pic_to_board("tests/test_case_B_0.png")
        self.data_B_0 = tools.pic_to_board("tests/test_case_B_0.png").data()
        self.data_B_1 = tools.pic_to_board("tests/test_case_B_1.png").data()
    def tearDown(self):
        self.img_A_0.close()
        self.img_A_1.close()
        self.img_A_2.close()
        self.img_A_3.close()

    def test_board_A(self):
        self.assertEqual(self.board_A.data(),self.data_A_0)
        self.assertEqual(self.board_A.generation(),0)
        
        self.board_A.iterate_board()
        self.assertEqual(self.board_A.data(),self.data_A_1)
        self.assertEqual(self.board_A.generation(),1)
        
        self.board_A.iterate_board()
        self.assertEqual(self.board_A.data(),self.data_A_2)
        self.assertEqual(self.board_A.generation(),2)
        
        self.board_A.iterate_board()
        self.assertEqual(self.board_A.data(),self.data_A_3)
        self.assertEqual(self.board_A.generation(),3)

    def test_board_B(self):
        self.assertEqual(self.board_B.data(),self.data_B_0)
        self.assertEqual(self.board_B.generation(),0)
        
        self.board_B.iterate_board()
        self.assertEqual(self.board_B.data(),self.data_B_1)
        self.assertEqual(self.board_B.generation(),1)
        
        self.board_B.iterate_board()
        self.assertEqual(self.board_B.data(),self.data_B_0)
        self.assertEqual(self.board_B.generation(),2)
        
        self.board_B.iterate_board()
        self.assertEqual(self.board_B.data(),self.data_B_1)
        self.assertEqual(self.board_B.generation(),3)
    

if (__name__ == "__main__"):
    cells_suite = unittest.TestLoader().loadTestsFromTestCase(CellsTest)
    unittest.TextTestRunner(verbosity=2).run(cells_suite)

    board_suite = unittest.TestLoader().loadTestsFromTestCase(BoardTest)
    unittest.TextTestRunner(verbosity=2).run(board_suite)

    tools_suite = unittest.TestLoader().loadTestsFromTestCase(ToolsTest)
    unittest.TextTestRunner(verbosity=2).run(tools_suite)
    
    more_board_suite = unittest.TestLoader().loadTestsFromTestCase(MoreBoardTest)
    unittest.TextTestRunner(verbosity=2).run(more_board_suite)

