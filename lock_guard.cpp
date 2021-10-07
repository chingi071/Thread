#include <iostream>
#include <thread>
#include <mutex>
using namespace std;
mutex g_mutex;
void first_thread_job()
{
 lock_guard<mutex> lock(g_mutex);
 cout << "This is the first thread " << endl;
}
int main()
{
 thread first_thread( first_thread_job);
 first_thread.join();
 return 0;
}