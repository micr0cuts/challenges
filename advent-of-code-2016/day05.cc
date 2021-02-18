#include <string>
#include <vector>
#include <iostream>
#include <openssl/md5.h>

std::string part1(const unsigned char d) {
    uint64_t n = 0;
    std::string password;
    while (true) {
        const unsigned char* n_char;
        n_char = (unsigned char*)n;
        const unsigned char* hashable = d + n_char;
        size_t m = sizeof(hashable);
        unsigned char* md;
        unsigned char* hash = MD5(hashable, m, md);
        std::string substring = std::to_string(*hash).substr(0,5);
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
    const unsigned char* doorId;
    doorId = (unsigned char*)"ojvtpuvg";
    std::string solution1 = part1(*doorId);
    std::cout << solution1 << std::endl;
}