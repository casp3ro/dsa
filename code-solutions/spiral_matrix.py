matrix = [[1,2,3],[4,5,6],[7,8,9]]

def spiralMatrix(matrix:list[list[int]]):

  output = []
  while matrix:

    output.extend(matrix.pop(0))
    #col
    if matrix and matrix[0]:
      for row in matrix:
        output.append(row.pop())

    #row
    if matrix: 
      last = matrix.pop()
      output.extend(reversed(last))

    #col
    if matrix and matrix[0]:
      for row in reversed(matrix):
        output.append(row.pop(0))

  
  return output

    

print(spiralMatrix(matrix))