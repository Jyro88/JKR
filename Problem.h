#ifndef PROBLEM_H
#define PROBLEM_H

#include "State.h"
#include <vector>

using namespace std;

class Problem {
public:
    State initialState;
    State goalState;

    Problem(State initial, State goal);
    vector<State> getSuccessors(const State& state) const;
};

#endif // PROBLEM_H
