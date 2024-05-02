#ifndef NODE_H
#define NODE_H

#include "State.h"

class Node {
public:
    State state;        // State represented by the node
    Node* parent;       // Parent node
    int action;         // Action that led to this state
    int depth;          // Depth of the node in the search tree
    float pathCost;     // Cost to reach this node from the root

    Node(State s, Node* p, int a, int d, float c);
};

#endif // NODE_H
