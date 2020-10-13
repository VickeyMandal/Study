#include<iostream>
using namespace std;


class stack{
	private:
		
	public:
		int top,size,arr[];
		//int size=5;
		stack(){
			cout<<"Enter size of stack: ";
			cin>>size;
			int arr[size];
			top=-1;
			for(int i=0;i<size;i++){
				arr[i]=0;
			}
		}
		
		//Operations Declaration: 
		bool isEmpty();
		bool isFull();
		void push(int data);
		int pop();	
		int count();
		int peek(int pos);
		void change(int pos,int data);
		void display();
			
};

//Operation implementation: 

bool stack :: isEmpty(){
	if(top == -1){
		return true;
	}
	else{
		return false;
	}
}

bool stack :: isFull(){
	if(top == size-1){
		return true;
	}
	else{
		return false;
	}
}

void stack :: push(int data){
	if(isFull()){
		cout<<"Stack Overflow";
	}else{
		top++;  
		arr[top]=data;
	}	
}

int stack :: pop(){
	if(isEmpty()){
		cout<<"Stack Underflow";
		return 0;
	}
	else{
		int pop_value = arr[top];
		arr[top]=0;
		top--;
		return pop_value;
	}	
}
int stack :: count(){
	return(top+1);
}

int stack :: peek(int pos){
	if(isEmpty()){
		cout<<"Stack Underflow";
		return 0;
	}
	else{
		return arr[pos];
	}
}

void stack :: change(int pos, int data){
	arr[pos]=data;
	cout<<"Values changed: "<<pos<<endl;
} 

void stack :: display(){
	cout<<"Stack items: ";
	for(int i=size-1;i>=0;i--){
		cout<<arr[i]<<" ";
	}
}

int main(){
	//Stack menu: 
	stack s;
	int option,position,data;
	do{
		cout<<endl<<"Operations Available( 0 to exit ): "<<endl;
		cout<<"1. Push()"<<endl;
		cout<<"2. Pop()"<<endl;
		cout<<"3. isEmpty()"<<endl;
		cout<<"4. isFull()"<<endl;
		cout<<"5. Peek()"<<endl;
		cout<<"6. Count()"<<endl;
		cout<<"7. Change()"<<endl;
		cout<<"8. Display()"<<endl;
		cout<<"9. Clear Screen"<<endl;
		cin>>option;
		switch(option){
			case 1:
				cout<<"Enter an item to push in the Stack: ";
				cin>>data;
				s.push(data);
				break;
				
			case 2:
				cout<<"Popped: "<<s.pop()<<endl;
				break;
				
			case 3:
				if(s.isEmpty()){
					cout<<"Stack is Empty.";
				}
				else{
					cout<<"Stack is not Empty.";
				}
				break;
			
			case 4:
				if(s.isFull()){
					cout<<"Stack is Full.";
				}
				else{
					cout<<"Stack is not Full.";
				}
				break;
			
			case 5:
				cout<<"Enter Position: ";
				cin>>position;
				cout<<"Item at "<<position<<" is: "<<s.peek(position)<<endl;
				break;
			
			case 6:
				cout<<"Total items in stack is: "<<s.count()<<endl;
				break;
				
			case 7:
				cout<<"Change function called"<<endl;
				cout<<"Enter position: ";
				cin>>position;
				cout<<"Enter Item: ";
				cin>>data;
				s.change(position,data);
				break;
				
			case 8:
				s.display();
				break;
				
			case 9:
				system("cls");
				break;
				
			default: 
				cout<<"Enter a valid option!";
				break;
			
		}
	}while(option!=0);
	
	
	return 0;
	
}


