from transaction import Transaction
from node import Node
from candidate import Candidate

class CompliantNode(Node):
    def __init__(self, p_graph, p_mallicious, p_txDistribution, numRound):
        # IMPLEMENT THIS
        return

    def setFollowees(self, followees):
        # IMPLEMENT THIS
        return

    def setPendingTransaction(self, pendingTransactions):
        # IMPLEMENT THIS
        return

    def sendToFollowers(self) -> set:
        # IMPLEMENT THIS
        return set()

    def receiveFromFollowees(self, candidates: set):
        # IMPLEMENT THIS
        return
