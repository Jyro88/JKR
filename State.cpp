#include "State.h"

using namespace std;

State::State(vector<vector<int>> b) : board(b) {}

bool State::operator==(const State& other) const {
    return board == other.board;
}

bool State::isGoalState(const State& goalState) const {
    return board == goalState.board;
}
