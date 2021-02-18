//
//  main.cpp
//  aoc2016day05
//
//  Created by Simon Vandieken on 2021-02-17.
//  Copyright © 2021 Simon Vandieken. All rights reserved.
//

#include <string>
#include <vector>
#include <iostream>
#include "md5.h"

std::string part1(std::string d) {
    uint64_t n = 0;
    std::string password;
    while (true) {
        std::string hashable = d + std::to_string(n);
        std::string hash = MD5(hashable).hexdigest();
        std::string substring = hash.substr(0,5);
        if (substring.compare("00000") == 0) {
            password.push_back(hash[5]);
            if (password.size() == 8) {
                return password;
            }
        }
        n++;
    }
    
}
int main() {
    std::string doorId = "ojvtpuvg";
    std::string solution1 = part1(doorId);
    std::cout << solution1 << std::endl;
}
