#!/usr/bin/env python3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""Sample code for Comp24011 Constraints lab solution

NB: The default code in non-functional; it simply avoids type errors
"""

__author__ = "USERNAME"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import constraint
import sys

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def Travellers(axiomList, extraPairs):
  """Solves Task 1 of the lab manual

  :param axiomList: list of puzzle axioms
  :type axiomList:  list[int]
  :param extraPairs: list of (traveller,destination) pairs
  :type extraPairs:  list[tuple[str,str]]

  :return: list of solutions
  :rtype:  list[dict[str,str]]
  """

  problem = constraint.Problem()
  people = ['claude', 'olga', 'pablo', 'scott']
  times = ['2:30', '3:30', '4:30', '5:30']
  destinations = ['peru', 'romania', 'taiwan', 'yemen']
  t_variables= list(map(( lambda x: 't_'+x ), people))
  d_variables= list(map(( lambda x: 'd_'+x ), people))
  problem.addVariables(t_variables, times)
  problem.addVariables(d_variables, destinations)

  # no two travellers depart at the same time
  problem.addConstraint(constraint.AllDifferentConstraint(), t_variables)
  # no two travellers return from the same destination
  problem.addConstraint(constraint.AllDifferentConstraint(), d_variables)

  
  if 1 in axiomList: 
    # Olga is leaving 2 hours before the traveller from Yemen
    for person in people:
      problem.addConstraint((
        lambda x,y,z:
        (y != 'yemen')
        or ((x == '4:30') and (z == '2:30'))
        or ((x == '5:30') and (z == '3:30'))
        ), ['t_'+person, 'd_'+person, 't_olga'])
    

  # Claude is either the person leaving at 2:30 pm or the traveller leaving at 3:30 pm.

  if 2 in axiomList: 
    for person in people:
      problem.addConstraint(
        (lambda x: 
        (x == '2:30') or (x == '3:30')
        ), ['t_claude']
      )


  # The person leaving at 2:30 pm is flying from Peru

  if 3 in axiomList: 
    for person in people:
      problem.addConstraint((
        lambda x,y:
        (y != 'peru') or ((x == '2:30'))
        ), ['t_'+person, 'd_'+person]
        )

  # The person flying from Yemen is leaving earlier than the person flying from Taiwan.

  #if a == yemen and b == taiwan then not(yemen later than taiwan)
  
  if 4 in axiomList: 
    for person1 in people:
        for person2 in people:
          if person1 == person2: continue
          problem.addConstraint(
          lambda a, b, x, y:
          ((a != "yemen") or (b != "taiwan")) or (x < y),  
          ['d_' + person1, 'd_' + person2, 't_' + person1, 't_' + person2]
      )
          
  #

  # The four travellers are Pablo, the traveller flying from Yemen, the person leaving at 2:30 pm
  # and the person leaving at 3:30 pm

  
  if 5 in axiomList: 
    #Pablo is not flying from yemen, leaving at 2:30 or 3:30
  
    problem.addConstraint(
      (lambda x: 
      ((x != '2:30') and (x != '3:30')) 
      ), ["t_pablo"]
    )
    problem.addConstraint(
          (lambda x: 
          ((x != 'yemen')) 
          ), ["d_pablo"]
        )


    #The traveller from yemen is not pablo, nor are they leaving at 2:30 or 3:30
    for person in people:
      problem.addConstraint(
            lambda a, b:
              ((a != "yemen") or ((b != "2:30") and (b != "3:30"))),   
              ['d_' + person, 't_' + person]  
        )
    #The person leaving at 2:30 is not pablo nor are they travelling from yemen [already covered by previous axioms]
    #The person leaving at 3:30 is not pablo nor are they travelling from yemen [already covered by previous axioms]

  #Establish additional axioms
  for pair in extraPairs:
    if ":" in pair[1]: #must be a time
      problem.addConstraint(lambda x: (x == str(pair[1])), ['t_'+pair[0]])
    else:
      problem.addConstraint(lambda x: (x == str(pair[1])), ['d_'+pair[0]])

  return problem.getSolutions()


def CommonSum(n):
  """Solves Task 2 of the lab manual

  :param n: size of square
  :type n:  int

  :return: common sum
  :rtype:  int
  """
  return n*(n**2 + 1) / 2


def BrokenDiags(n):
  """Solves Task 3 of the lab manual

  :param n: size of square
  :type n:  int

  :return: list of broken diagonals
  :rtype:  list[list[int]]
  """

  #So, thinking out loud
  #our return array is of size (n), and is comprised of an array of ints
  #There are 2n broken diagonals for any given size n magic square
  #We would compute them by considering going in the forward direction (x++, y--)
  #And then the backwards direction (x--, y--)
  bd = []
  for i in range(n):
    x = i
    y = 0
    currbd = []
    for j in range(n):
      currbd.append((n*y)+x%n)
      x += 1
      y += 1
    bd.append(currbd)

  for i in range(n):
    x = i
    y = 0
    currbd = []
    for j in range(n):
      currbd.append((n*y)+x%n)
      x -= 1
      y += 1
    bd.append(currbd)

  return bd


def MSquares(n, axiomList, extraPairs):
  """Solves Task 4 of the lab manual

  :param n: size of square
  :type n:  int
  :param axiomList: list of magic square axioms
  :type axiomList:  list[int]
  :param extraPairs: list of (position,value) pairs
  :type extraPairs:  list[tuple[int,int]]

  :return: list of solutions
  :rtype:  list[dict[int,int]]
  """

  """
  problem = constraint.Problem()
  problem.addVariables(range(0, 16), range(1, 16 + 1))
  problem.addConstraint(constraint.AllDifferentConstraint(), range(0, 16))
  problem.addConstraint(constraint.ExactSumConstraint(34), [0, 5, 10, 15])
  problem.addConstraint(constraint.ExactSumConstraint(34), [3, 6, 9, 12])
  for row in range(4):
    problem.addConstraint(constraint.ExactSumConstraint(34),
    [row * 4 + i for i in range(4)])
  for col in range(4):
    problem.addConstraint(constraint.ExactSumConstraint(34),
    [col + 4 * i for i in range(4)])
  solutions = problem.getSolutions()
  print(solutions)
  """

  #The above is the n = 4 solution, we must generalise it

  #Step 1, fix variable range
  problem = constraint.Problem()
  problem.addVariables(range(0, n**2), range(1, n**2 + 1))

  #Step 2, add constraints

  #2.1  Different numbers
  problem.addConstraint(constraint.AllDifferentConstraint(), range(0, n**2))

  #2.2 Broken diagonals add up to EXACTLY the Const CommonSum
  #Define Commonsum
  CS = CommonSum(n)
  bds = BrokenDiags(n)


  #Such also applies vertically, and horizontally, trivial
  if 1 in axiomList:
    for row in range(n):
      problem.addConstraint(constraint.ExactSumConstraint(CS),
      [row * n + i for i in range(n)])

  if 2 in axiomList:
    for col in range(n):
      problem.addConstraint(constraint.ExactSumConstraint(CS),
      [col + n * i for i in range(n)])

  if 3 in axiomList:
    problem.addConstraint(constraint.ExactSumConstraint(CS),bds[0])
    problem.addConstraint(constraint.ExactSumConstraint(CS),bds[-1])

  #For all broken diagonals, they add up to the commonsum
  if 4 in axiomList:
    for bd in bds: problem.addConstraint(constraint.ExactSumConstraint(CS),bd)
  
  # Each extra pair (𝑣, 𝑘) asserts that the position 𝑣 of the square is filled with the integer k


  #print(extraPairs)
  for pair in extraPairs:
    problem.addConstraint(lambda x, value = pair[1]: (x == value), [pair[0]] )
  

  #python3 ./constraintsLab.py MSquares 4 '[1,2,3]' '[(0,13),(1,12),(2,7)]'


  return problem.getSolutions()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# debug run
if __name__ == '__main__':
  if len(sys.argv) > 2:
    cmd = "{}({})".format(sys.argv[1], ",".join(sys.argv[2:]))
    print("debug run:", cmd)
    ret = eval(cmd)
    print("ret value:", ret)
    try:
      cnt = len(ret)
      print("ret count:", cnt)
    except TypeError:
      pass
  else:
    sys.stderr.write("Usage: {} <FUNCTION> <ARG>...\n".format(sys.argv[0]))
    sys.exit(1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vim:set et ts=2 sw=2:
