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
    from game import Directions
    
    fringe=util.Stack()
    state=problem.getStartState()
    
    plans={}
    closed=set()
    successors=problem.getSuccessors(state)
    #plans dict gets some keys (state tuples) and values (directions)
    for i in successors:
        fringe.push(i)
        plans[i]=i[1]
    closed.add(state)
    
    
    while not problem.isGoalState(state):
        if not fringe:
            print "FAILURE"
            return none
        stateFull=fringe.pop()
        state=stateFull[0]
        #if this is the goal state, then return the value of the current state in the dict (winning plan)
        if problem.isGoalState(state):
            movedir=stateFull[1]
            plan=plans[stateFull]
            return list(plan)
        if state not in closed:
            closed.add(state)
            successors=problem.getSuccessors(state)
            #add successors to the fringe, and also create dict entries for them
            #that depend on the plan of their parent node (the current state)
            #and their own direction from the current state
            for i in successors:
                if type(plans[stateFull])==tuple:
                    plans[i]=plans[stateFull]+(i[1],)
                else: #single case, plans[state] is a string
                    plans[i]=plans[stateFull],i[1]
                fringe.push(i)
                                    
    util.raiseNotDefined()
    

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """

    "*** YOUR CODE HERE ***"
    
    from game import Directions
    
    fringe=util.Queue()
    state=problem.getStartState()
    
    plans={}
    closed=set()
    successors=problem.getSuccessors(state)
    print successors
    #plans dict gets some keys (state tuples) and values (directions)
    for i in successors:
        fringe.push(i)
        plans[i]=i[1]
    closed.add(state)
    
    
    while not problem.isGoalState(state):
        if not fringe:
            print "FAILURE"
            return none
        stateFull=fringe.pop()
        state=stateFull[0]
        #if this is the goal state, then return the value of the current state in the dict (winning plan)
        if problem.isGoalState(state):
            movedir=stateFull[1]
            plan=plans[stateFull]
            return list(plan)
        if state not in closed:
            closed.add(state)
            successors=problem.getSuccessors(state)
            #add successors to the fringe, and also create dict entries for them
            #that depend on the plan of their parent node (the current state)
            #and their own direction from the current state
            for i in successors:
                if type(plans[stateFull])==tuple:
                    plans[i]=plans[stateFull]+(i[1],)
                else: #single case, plans[state] is a string
                    plans[i]=plans[stateFull],i[1]
                fringe.push(i)

    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    
    from game import Directions
    
    fringe=util.PriorityQueue()
    state=problem.getStartState()
    
    plans={}
    closed=set()
    successors=problem.getSuccessors(state)
    #plans dict gets some keys (state tuples) and values (directions)
    for i in successors:
        fringe.push(i,problem.getCostOfActions([i[1]]))
        plans[i]=i[1]
    closed.add(state)
    
    
    while not problem.isGoalState(state):
        if not fringe:
            print "FAILURE"
            return none
        stateFull=fringe.pop()
        state=stateFull[0]
        #if this is the goal state, then return the value of the current state in the dict (winning plan)
        if problem.isGoalState(state):
            movedir=stateFull[1]
            plan=plans[stateFull]
            return list(plan)
        if state not in closed:
            closed.add(state)
            successors=problem.getSuccessors(state)
            #add successors to the fringe, and also create dict entries for them
            #that depend on the plan of their parent node (the current state)
            #and their own direction from the current state
            for i in successors:
                if type(plans[stateFull])==tuple:
                    plans[i]=plans[stateFull]+(i[1],)
                else: #single case, plans[state] is a string
                    plans[i]=plans[stateFull],i[1]
                fringe.push(i,problem.getCostOfActions(list(plans[i])))

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
    from game import Directions
    
    fringe=util.PriorityQueue()
    state=problem.getStartState()
    
    plans={}
    closed=set()
    successors=problem.getSuccessors(state)
    #plans dict gets some keys (state tuples) and values (directions)
    for i in successors:
        fringe.push(i,problem.getCostOfActions([i[1]])+(heuristic(i[0],problem)))
        plans[i]=i[1]
    closed.add(state)
    
    
    while not problem.isGoalState(state):
        if not fringe:
            print "FAILURE"
            return none
        stateFull=fringe.pop()
        state=stateFull[0]
        #if this is the goal state, then return the value of the current state in the dict (winning plan)
        if problem.isGoalState(state):
            movedir=stateFull[1]
            plan=plans[stateFull]
            return list(plan)
        if state not in closed:
            closed.add(state)
            successors=problem.getSuccessors(state)
            #add successors to the fringe, and also create dict entries for them
            #that depend on the plan of their parent node (the current state)
            #and their own direction from the current state
            for i in successors:
                if type(plans[stateFull])==tuple:
                    plans[i]=plans[stateFull]+(i[1],)
                else: #single case, plans[state] is a string
                    plans[i]=plans[stateFull],i[1]
                fringe.push(i,problem.getCostOfActions(list(plans[i]))+(heuristic(i[0],problem)))

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
