//Program without synchronization
#include<stdio.h>
#include<pthread.h>
#define NUM_THREADS 4
#define INCREMENTS 1000000
long long counter = 0;

void* increment_counter(void* arg) {
    for (int i = 0; i < INCREMENTS; i++) {
        counter++; // Incrementing the shared counter(UNSAFE)
    }
    return NULL;
}
int main() {
    pthread_t threads[NUM_THREADS];

    // Create multiple threads to increment the counter
    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_create(&threads[i], NULL, increment_counter, NULL);
    }

    // Wait for all threads to finish
    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    // Print the final value of the counter
    printf("Final counter value: %lld\n", counter);
    printf("Expected counter value: %lld\n", (long long)NUM_THREADS * INCREMENTS);
    return 0;
}