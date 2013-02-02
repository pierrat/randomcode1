# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and Pieter 
# Abbeel in Spring 2013.
# For more info, see http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    
    from game import Directions
    from pacman import GameState

    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    '''
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    '''

    
    fringe=util.Stack()
    state=problem.getStartState()
    successors=problem.getSuccessors(state)
    # debug later if getSuccessors returns an error (if there are no succ. to start)
    for i in successors:
        fringe.push(i)
    closed=set()
    closed.add(state)
    plan=[]
    
    while not problem.isGoalState(state):
        if not fringe:
            print "FAILURE"
            return none
        statePrev=state #store previous state
        stateFull=fringe.pop()
        state=stateFull[0] #this is state now
        if problem.isGoalState(state):
            movedir=stateFull[1]
            plan.append(movedir)
            return plan
        if state not in closed:
            closed.add(state)
            print problem.getSuccessors(state)
            #check if there are no successors: if so, go to prev state (current state will already be off fringe)
            if problem.getSuccessors(state)=='false':
                state=statePrev
                badmove=plan.pop()
            else:
                successors=problem.getSuccessors(state)
                movedir=stateFull[1]
                plan.append(movedir)
                for i in successors:
                    fringe.push(i)
    

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    """
    from game import directions
    from searchAgents import SearchAgent

    fringe=util.Queue()
    state=problem.getStartState()
    fringe.push(startState)
    closed=[startState]
    
    while problem.isGoalState(state)=='false':
        if not fringe:
            print "FAILURE"
        state=fringe.pop()
        if problem.isGoalState(state)=='true':
            movedir=state[1]
            plan=plan.append(movedir)
            return plan
        if state not in closed:
            closed.append(state)
            movedir=state[1]
            plan=plan.append(movedir)
            successors=problem.getSuccessors(state)
            fringe.push(successors)
    
    """
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    """
    from game import directions
    from searchAgents import SearchAgent

    fringe=util.PriorityQueue()
    state=problem.getStartState()
    fringe.push(startState)
    closed=[startState]
    
    while problem.isGoalState(state)=='false':
        if not fringe:
            print "FAILURE"
        state=fringe.pop()
        if problem.isGoalState(state)=='true':
            movedir=state[1]
            plan=plan.append(movedir)
            return plan
        if state not in closed:
            closed.append(state)
            movedir=state[1]
            plan=plan.append(movedir)
            successors=problem.getSuccessors(state)
            costs=[costs[1] for costs in successors]
            '''
            how to acct for costs from beginnning??? ie cumulative costs
            '''
            fringe.push(successors)
    """
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
