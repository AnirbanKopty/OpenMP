#include <stdio.h>
#include <omp.h>

int main()
{
    printf("Number of processors available = %d\n", omp_get_num_procs());
    printf("Number of threads = %d\n", omp_get_max_threads());

    int id = omp_get_thread_num();  // To get the number 

}