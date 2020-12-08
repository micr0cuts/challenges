#include <vector>
#include <string>
#include <iostream>
#include <fstream>

using std::vector;


int main() {
    vector<int> entries;
    std::ifstream myfile;
    std::string line;

    myfile.open("input01.txt");

    while (getline(myfile,line))
        {
          entries.push_back(std::stoi(line));
        }
    myfile.close();

    bool found = false;
    for(size_t i = 0; i != entries.size(); i++) {
        if (found) { 
            break;
        }
        for(size_t j = 0; j != entries.size(); j++) {
            if (entries[i] == entries[j]) {
                continue;
            }
            else if (found) {
                break;
            }

            for(size_t k = 0; k != entries.size(); k++) {
                if (entries[i] == entries[k]) {
                    continue;
                }

                if (entries[i] + entries[j] + entries[k] == 2020) {
                    std::cout << entries[i] << " " << entries[j] << " " << 
                    entries[k] << " " << entries[i]*entries[j]*entries[k] << std::endl;
                    found = true;
                }
            }
        }
    }
}