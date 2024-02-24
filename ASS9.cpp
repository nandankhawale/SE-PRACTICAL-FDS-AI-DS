#include<iostream>
#include <cctype>
#include<string.h>
#define max 50
using namespace std;
class STACK
{
	private:
		char a[max];
		int top;
	
	public:
		STACK()
		{
			top=-1;	
		}	
		
		void push(char);
		void reverse();	
		void convert(char[]);
		void palindrome();
};
void STACK::push(char c)
{
	top++;
	a[top] = c;
	a[top+1]='\0';
	
	cout<<endl<<c<<" is pushed on stack ...";
}
void STACK::reverse()
{
	char str[max];
	
	cout<<"\n\nReverse string is : ";
		
	for(int i=top,j=0; i>=0; i--,j++)
	{
		cout<<a[i];
		str[j]=a[i];
	}
	
	cout<<endl;
}
void STACK::convert(char str[]) {
    int len = strlen(str);

    for (int j = 0; j < len; j++) {
        // Check if the character is an alphabet
        if (isalpha(str[j])) {
            // Convert the character to lowercase using tolower
            str[j] = tolower(str[j]);
        }
    }

    cout << "Converted String: " << str << "\n";
}
void STACK::palindrome() {
    char str[max];
    int i, j;

    // Assuming 'a' is a member variable of the STACK class
    for (i = top, j = 0; i >= 0; i--, j++) {
        str[j] = a[i];
    }

    // Null-terminate the reversed string
    str[j] = '\0';

    // Compare the original string 'a' and the reversed string 'str'
    if (strcmp(a, str) == 0) {
        cout << "\n\nString is palindrome...";
    } else {
        cout << "\n\nString is not palindrome...";
    }
}
int main()
{
	STACK stack;



	char str[max];
	int i = 0;

	cout << "\nEnter string to be reversed and check is it palindrome or not : \n\n";

	cin.getline(str, 50);

	stack.convert(str);

	while (str[i] != '\0')
	{
		stack.push(str[i]);
		i++;
	}

	stack.palindrome();
	stack.reverse();
}