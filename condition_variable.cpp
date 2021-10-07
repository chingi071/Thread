#include <iostream>
#include <thread>
#include <mutex>
#include<condition_variable>
using namespace std;
condition_variable cond_var;
mutex u_mutex;
bool ready = false;
void first_thread_job()
{
 unique_lock<mutex> lock(u_mutex);
// 使用 wait() 進行等待
 cout << "thread wait" << endl;
 cond_var.wait(lock);
 cout << "This is the first thread " << endl;
}
void second_thread_job()
{
 unique_lock<mutex> lock(u_mutex);
// 使用 wait() 進行等待 傳入第二個參數
 cout << "thread wait" << endl;
 cond_var.wait(lock, [](){ return ready; });
 cout << "This is the second thread " << endl;
}
int main()
{
 thread first_thread(first_thread_job);
 thread second_thread(second_thread_job);
 cout << "wait 5 millisecond…" << endl;
 this_thread::sleep_for(std::chrono::milliseconds(5));
// 使用 notify_one() 喚醒執行緒
 cout << "thread notify_one" << endl;
 cond_var.notify_one();
 // 回傳 ready 判斷是否要停止等待
 ready = true;
// 使用 notify_one() 喚醒執行緒
 cout << "thread notify_one" << endl;
 cond_var.notify_one();
 first_thread.join();
 second_thread.join();
 return 0;
}