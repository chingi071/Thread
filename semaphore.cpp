#include <iostream>
#include <thread>
#include <semaphore.h>
using namespace std;
sem_t binSem;
int a;
void first_thread_job()
{
 sem_wait(&binSem);
 for (int i = 0; i < 3; i++)
 {
 a += 1;
 cout << "This is the first thread " << a << endl;
 }
}
void second_thread_job()
{
 for (int i = 0; i < 3; i++)
 {
 a -= 1;
 cout << "This is the second thread " << a << endl;
 }
 sem_post(&binSem);
}
int main()
{
 int res;
 // Semaphore 初始化
 res = sem_init(&binSem, 0, 0);
 // 建立執行緒
 thread first_thread(first_thread_job);
 thread second_thread(second_thread_job);
 // 將主執行緒暫停，等待指定的執行緒結束
 first_thread.join();
 second_thread.join();
return 0;
}