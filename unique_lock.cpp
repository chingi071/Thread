#include <iostream>
#include <thread>
#include <mutex>
using namespace std;
mutex u_mutex;
void first_thread_job()
{
 unique_lock<mutex> lock(u_mutex);
 cout << "This is the first thread " << endl;
}
int main()
{
 thread first_thread( first_thread_job);
 first_thread.join();
 return 0;
}