#include <iostream>
#include "Problem.h"

using namespace std;

// Function to take input for a board from the user
vector<vector<int>> getInputBoard() {
    vector<vector<int>> board;
    int size;
    cout << "Enter the size of the board (Ex: for a 3x3 board, enter 3): ";
    cin >> size;
    cout << "Enter the board:\n (separate numbers by spaces and hit enter after each row)";
    for (int i = 0; i < size; ++i) {
        vector<int> row;
        for (int j = 0; j < size; ++j) {
            int cell;
            cin >> cell;
            row.push_back(cell);
        }
        board.push_back(row);
    }
    return board;
}

int main() {
    // Get input for initial board
    cout << "Enter the initial board:\n";
    vector<vector<int>> initialBoard = getInputBoard();

    // Define the predetermined goal board
    vector<vector<int>> goalBoard = {{1, 2, 3}, {4, 5, 6}, {7, 8, 0}};

    State initialState(initialBoard);
    State goalState(goalBoard);

    Problem problem(initialState, goalState);

    return 0;
}

