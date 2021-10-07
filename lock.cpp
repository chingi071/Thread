#include <iostream>
#include <thread>
#include <mutex>
using namespace std;
// 定義 lock
mutex mu;
void first_thread_job()
{
 mu.lock();
 cout << "This is the first thread "<< endl;
 mu.unlock();
}
int main()
{
 thread first_thread(first_thread_job);
 first_thread.join();
 return 0;
}