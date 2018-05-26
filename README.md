RGB Game of Life

A cellular automota with 3 kinds of life, based on Conway's Game of Life.

![Animated GIF of a game of RGB Life](https://i.imgur.com/Gqz7mZW.gif)

---

Simulates the RGB Game of Life on a torus (wrapping 2D array.)

CLI usage:

    -s --savepic f  Save a pic of each iteration to f, appended _xxx.png.
    -i --iterate n  Iterate n times, print the board at each iteration
    -p --print      Print the image to console during each iteration.

e.g.:

    python3 rgblife.py input.png -s output -i 300
    # Iterates 300 steps of RGB Game of Life, outputs output_000.png, output_001.png, etc.

---

There are three classes of life; R, G, and B.

The food chain is cyclic: R preys on G, G preys on B, and B preys on R.

Terminology is as follows:

   * A **cell** is the smallest element in the game of life.
   * A cell can be **live** (R, G, or B) or **dead** (AKA empty).
   * A **neighbour** is a live cell adjacent to a cell in question.
   * A**predatory** neighbour of a cell a neighbour that preys on it. (E.g. B is a predator of R.)
   * A **prey** neighbour of a cell is a neighbour that cell preys on. (E.g. R preys on G.)
   * A **like** neighbour is a cell of the same kind. (E.g. R is like R.)
   * A **friendly** neighbour is a cell that is like or prey. (E.g. R and G are friendly to R.)
   * A **non-prey** neighbour is a cell that is like or predator. (E.g. R and B are non-prey neighbours of R.)

Live cells continue to live so long as they have ample friendly neighbours. Predatory cells can convert a live cell or kill it. The rules for live cells are as follows, and are checked in this order:

   * **Overpopulation**: Any live cell with 4 or more like neighbours dies
   * **Encroachment**: Any live cell in which predatory neighbours outnumber friendly neighbours is subject to encroachment (see below).
   * **Conversion**: Any live cell subject to encroachment in which predatory neighbours outnumber friendly neighbours by at least two is converted to the predatory cell.
   * **Stifling**: Any live cell subject to encroachment but not conversion dies.
   * **Starvation**: Any live cell with fewer than two friendly neighbours dies.
   * **Survival**: Any cell that does not die from the previous rules survives another generation.

Dead cells can become living cells subject to the following rules:

   * **Reproduction**: A dead cell with three neighbours of the same class and one empty neighbour becomes a living cell of the same class.
   * **Expansion**: A dead cell with neighbours of only two different classes (one predatory and one prey) is converted to the predatory class so long as there is between one to three predator neighbours, and at least three neighbours total.
 
---

Version 1.0.1

History:
1.0.1       Performance enhancements
1.0.0       Initial release

To be fixed/done:
   
   * (x,y) order is internally inconsistent
   * There is minimal error checking
   * The CLI has no unit tests; rewrite under TDD
   * Add documentation to the Wiki
   * It is slow; rewrite to make faster
    
