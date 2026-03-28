#include <iostream>
#include <unistd.h>

int main() {
    int sumEven = 0, sumOdd = 0;
    pid_t pid = fork();

    if (pid == 0) {
        for (int i = 1; i <= 10; i++) {
            if (i % 2 != 0) {
                sumOdd += i;
            }
        }
        std::cout << "Child Process: Sum of odd numbers = " << sumOdd << "\n";
    } else if (pid > 0) {
        for (int i = 1; i <= 10; i++) {
            if (i % 2 == 0) {
                sumEven += i;
            }
        }
        std::cout << "Parent Process: Sum of even numbers = " << sumEven << "\n";
    } else {
        std::cerr << "Fork failed!\n";
    }

    return 0;
}