#ifndef STATE_H
#define STATE_H

#include <vector>

using namespace std;

class State {
public:
    vector<vector<int>> board; // 2D vector to represent the puzzle board

    State(vector<vector<int>> b); // Constructor
    bool operator==(const State& other) const; // Equal operator override
    bool isGoalState(const State& goalState) const; 
};

#endif // STATE_H
