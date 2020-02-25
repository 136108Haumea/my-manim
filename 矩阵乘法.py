from manimlib.imports import *

class test(Scene):
  def matrix_multiplication(self,matrix1,matrix2):
    matrix1_row = len(matrix1)
    matrix1_ele = len(matrix1[0])
    matrix2_row = len(matrix2)
    matrix2_ele = len(matrix2[0])
    if matrix1_row != matrix2_ele or matrix1_ele != matrix2_row:
      return []
    return [[sum([matrix1[i][j]*matrix2[j][k] for j in range(matrix2_ele)]) for k in range(matrix1_row)] for i in range(matrix1_row)]
      

  def construct(self):
    
    self.add(Matrix(matrix=self.matrix_multiplication([[1,2],[3,4]],[[1,2],[3,4]])))
    #|1 2|* |1 2| = | 7 10|
    #|3 4|  |3 4|   |15 22|
    self.wait()
