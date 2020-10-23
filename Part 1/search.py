# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal directions.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of directions that solves tinyMaze.  For any other maze, the
    sequence of directions will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def graphSearch(problem, fringe, heuristic=nullHeuristic):
    """
        problem: Abstract representation of current problem to be solved.
        fringe: Data structure depending on the type of search that holds the fringe.
        heuristic: Heuristics determined by state and problem. Set default to nullHeuristic if heuristics are not used.
    Search through the successors of a problem to find a goal. Maintain fringe to explore new elements. 
    Return a list of paths/directions to be used to reach the goal.
    """
    startState = problem.getStartState()
    fringe.push((startState, [], 0)) #Fringe holds state, path list and any possible cost and heuristics.
    visited = set() #Maintain a set of visited nodes explored.

    while not fringe.isEmpty():
        newState, newPath, newCost = fringe.pop() #Pop off fringe to explore newState, newPath, and newCost.

        if newState not in visited: #Store visited states.
            visited.add(newState)
            
            if problem.isGoalState(newState): #Check if goal state is met, return a list of paths if met.
                return newPath

            for successor in problem.getSuccessors(newState): #Explored new nodes determined by successor function, push to fringe         
                fringe.push((successor[0], newPath + [successor[1]], newCost + successor[2])) #Push new state, append to path list, and accumulate costs.
                
    return []


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    return graphSearch(problem, util.Stack())

    
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    return graphSearch(problem, util.Queue())


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    #Everytime we push new successor to fringe, we call lambda function on the last element of fringe, i.e cost
    pQueue = util.PriorityQueueWithFunction(lambda x: x[2]) #Priority queue with function chooses the lowest value priority. 
    return graphSearch(problem, pQueue)


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    #Similar to UCS, everytime we push new successor to fringe, we call lambda function on the last element of fringe i.e cost + current heuristics
    pQueue = util.PriorityQueueWithFunction(lambda x: x[2] + heuristic(x[0], problem)) #Add accumulated costs from fringe and heuristics from current state and problem.
    return graphSearch(problem, pQueue)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
