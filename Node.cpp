#include "Node.h"

Node::Node(State s, Node* p, int a, int d, float c) : state(s), parent(p), action(a), depth(d), pathCost(c) {}
