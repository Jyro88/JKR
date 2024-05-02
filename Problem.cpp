#include "Problem.h"
#include <algorithm>

using namespace std;

// Constructor for Problem class
Problem::Problem(State initial, State goal) : initialState(initial), goalState(goal) {}

// Method to generate successor states
vector<State> Problem::getSuccessors(const State& state) const {
    vector<State> successors;

    // Find the position of the empty tile (0)
    int emptyRow = -1, emptyCol = -1;
    for (int i = 0; i < state.board.size(); ++i) {
        for (int j = 0; j < state.board[i].size(); ++j) {
            if (state.board[i][j] == 0) {
                emptyRow = i;
                emptyCol = j;
                break;
            }
        }
        if (emptyRow != -1) break;
    }

    // Define possible moves (up, down, left, right)
    int dr[] = {-1, 1, 0, 0};
    int dc[] = {0, 0, -1, 1};

    // Generate successor states by swapping the empty tile with its neighbors
    for (int k = 0; k < 4; ++k) {
        int newRow = emptyRow + dr[k];
        int newCol = emptyCol + dc[k];

        // Check if the new position is within the bounds of the puzzle
        if (newRow >= 0 && newRow < static_cast<int>(state.board.size()) && 
            newCol >= 0 && newCol < static_cast<int>(state.board[0].size())) {
            // Create a new state by swapping the empty tile with its neighbor
            vector<vector<int>> newBoard = state.board;
            swap(newBoard[emptyRow][emptyCol], newBoard[newRow][newCol]);
            successors.push_back(State(newBoard));
        }
    }

    return successors;
}
