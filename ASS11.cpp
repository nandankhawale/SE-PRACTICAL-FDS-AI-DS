/*Queues are frequently used in computer programming, and a typical example is the creation of a job queue by an operating system.
If the operating system does not use priorities, then the jobs are processed in the order they enter the system.
Write C++ program for simulating job queue. Write functions to add job and delete job from queue.*/

#include <iostream>
#define MAX 10
using namespace std;

class queue
{
private:
    int data[MAX];
    int rear, front;

public:
    queue()
    {
        rear = front = -1;
    }
    int isempty();
    int isfull();
    void enqueue(int);
    int delqueue();
    void display();
};
int queue::isempty()
{
    return (rear == front) ? 1 : 0;
}
int queue::isfull()
{
    return (rear == MAX - 1) ? 1 : 0;
}
void queue::enqueue(int x)
{
    data[++rear]=x;
}
int queue::delqueue()
{
    return data[++front];
}
void queue::display()
{
    int i;
    cout << "n";
    for (i = front + 1; i < rear; i++)
    {
        cout << data[i];
    }
}
int main()
{
    queue obj;
    int ch, x;
    do
    {
        cout << "\n 1.Insert Job\n 2.Delete Job\n 3.Display\n 4.Exit\n Enter your choice : ";
        cin >> ch;
        switch (ch)
        {
        case 1:
            if (!obj.isfull())
            {
                cout << "enter the data";
                cin >> x;
                obj.enqueue(x);
            }
            else
            {
                cout << "queue is full";
            }
            break;
        case 2:
            if (!obj.isempty())
            {
                cout << "Deleted element"<< endl;
                obj.delqueue() ;
            }
            else{
             cout << "queue is empty";
            }
            cout << "remaining jobs are" << endl;
            obj.display();
            break;
        case 3:
            obj.display();
            break;
        case 4:
        
            cout << "\n Exiting Program.....";
            break;
        
        default:
            cout << "\nInvalid choice";
            break;
        }
    } while (ch != 4);;
}