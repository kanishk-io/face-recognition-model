#include <stdio.h>
#include <math.h>

double f(double x) {
    return x*x*x - x - 1;
}

double f_prime(double x) {
    return 3*x*x - 1;
}

void newtonRaphson(double x0, double tolerance) {
    double x1;
    do {
        x1 = x0 - f(x0) / f_prime(x0);
        if (fabs(x1 - x0) < tolerance)
            break;
        x0 = x1;
    } while (1);
    printf("Root: %.6lf\n", x1);
}

int main() {
    double x0 = 2, tolerance = 0.0001;
    newtonRaphson(x0, tolerance);
    return 0;
}
