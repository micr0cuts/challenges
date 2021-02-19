#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<std::vector<std::string> > keypad = {{'1', '2', '3'}, {'4', '5', '6'}, {'7', '8', '9'}};

    std::vector<std::string> entries;
    std::ifstream myfile;
    std::string line;
    myfile.open("input02.txt");

    while (getline(myfile,line))
        {
          entries.push_back(line);
        }
    myfile.close();
}