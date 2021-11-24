from transaction import Transaction
from node import Node
from candidate import Candidate

class CompliantNode(Node):

    def __init__(self, p_graph, p_mallicious, p_txDistribution, numRound):
        # IMPLEMENT THIS
        self._p_graph = p_graph
        self._p_mallicious = p_mallicious
        self._p_txDistribution = p_txDistribution
        self._numRound = numRound
        self._currentRound = 0
        self._oldRound = 0
        # self._followees = set()
        self._candidates = set()
        self._pendingTransactions = set()
        self._consensusTransactions = set()

    def setFollowees(self, followees):
        # if isinstance(followees, set):
        self._followees = followees
        # else:
        #     raise Exception("Not array")

    def setPendingTransaction(self, pendingTransactions):
        self._pendingTransactions = pendingTransactions
        self._consensusTransactions = pendingTransactions

    def sendToFollowers(self) -> set:
        txs = set()
        if self._currentRound == self._numRound:
            txs = self._consensusTransactions
        else:
            txs = self._pendingTransactions
            self._oldRound = self._currentRound
        return txs

    def receiveFromFollowees(self, candidates: set):
        self._currentRound = self._currentRound + 1
        if 0 < self._oldRound < self._currentRound:
            self._pendingTransactions.clear()
        for candidate in candidates:
            if self._followees[candidate.sender]:
                self._pendingTransactions.add(candidate.tx)
