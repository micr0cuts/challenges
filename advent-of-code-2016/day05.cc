#include <string>
#include <vector>
#include <iostream>
#include <openssl/md5.h>

std::string part1(std::string d) {
    uint64_t n = 0;
    std::string password;
    while (true) {
        std::string hashable = d + std::to_string(n);
        // size_t m = hashable.size();
        unsigned char* hash;
        MD5(reinterpret_cast<const unsigned char*>(hashable.data()), hashable.size(), hash);
        std::string hash_string = reinterpret_cast<char*>(hash);
        std::string substring = hash_string.substr(0,5);
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