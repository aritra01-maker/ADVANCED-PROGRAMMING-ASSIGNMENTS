//Modified correct program using mutex to protect the shared counter variable
#include<stdio.h>
#include<pthread.h>
#define NUM_THREADS 4
#define INCREMENTS 1000000
long long counter = 0;
// Mutex variable
pthread_mutex_t lock;

/*
Thread function
*/
void* increment_counter(void* arg)
{
    for(int i = 0; i < INCREMENTS; i++)
    {
        // Lock critical section
        pthread_mutex_lock(&lock);

        counter++;

        // Unlock critical section
        pthread_mutex_unlock(&lock);
    }

    return NULL;
}

int main()
{
    pthread_t threads[NUM_THREADS];

    /*
    Initialize mutex
    */
    pthread_mutex_init(&lock, NULL);

    /*
    Create threads
    */
    for(int i = 0; i < NUM_THREADS; i++)
    {
        pthread_create(&threads[i],
                       NULL,
                       increment_counter,
                       NULL);
    }

    /*
    Wait for all threads
    */
    for(int i = 0; i < NUM_THREADS; i++)
    {
        pthread_join(threads[i], NULL);
    }

    /*
    Print final result
    */
    printf("Final Counter Value = %lld\n", counter);
    printf("Expected Counter Value = %lld\n", (long long)NUM_THREADS * INCREMENTS);
    /*
    Destroy mutex
    */
    pthread_mutex_destroy(&lock);

    return 0;
}