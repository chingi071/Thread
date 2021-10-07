#include <iostream>
#include <thread>
using namespace std;
void first_thread_job()
{
 cout << "This is the first thread "<< endl;
}
// 傳入string x
void second_thread_job(string x)
{
 cout << "This is the second thread " << x << endl;
}
int main()
{
 // 建立執行緒
 thread first_thread(first_thread_job);
 thread second_thread(second_thread_job, "abc"); 
 // 將主執行緒暫停，等待指定的執行緒結束
 first_thread.join();
 second_thread.join();
return 0;
}