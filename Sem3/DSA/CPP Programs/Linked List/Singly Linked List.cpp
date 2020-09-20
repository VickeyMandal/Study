//Pending
#include <iostream>
using namespace std;
void display();
struct node{
	int data;
	struct node *next;
};
struct node *head;
// insertion at first
void insertatB(){
	int d;
	cout<<"Enter value : ";
	cin>>d;
	
	struct node *new_node = new node;
	new_node->data = d;
	new_node->next = NULL;
	
	if(head==NULL){
		head = new_node;
	} else {
		new_node->next = head;
		head=new_node;
	}
	display();
}

void insertafter(){
	int d;
	cout<<"Enter value : ";
	cin>>d;
	
	struct node *new_node = new node;
	new_node->data = d;
	new_node->next = NULL;
//	ptr=head;
//	preptr=ptr;
	
}

void insertatL(){
	int d;
	cout<<"Enter value : ";
	cin>>d;
	
	struct node *new_node = new node;
	new_node->data = d;
	new_node->next = NULL;
	
	if(head==NULL){
		head = new_node;
	} else {
		struct node *new_node = head;
		while(new_node->next!=NULL){
			new_node=new_node->next;
		}
		new_node->next=new_node;
	}
	//display();
}

node* search(int item){
	
	cout<<"Enter element to search : ";
	cin>>item;
	if(head==NULL)
	{
	cout<<"List is empty."<<endl;
	return NULL;
	}
	else{
	     struct node *p=head;
	     
	     while(p!=NULL)
	     {
	     	if(item==p->data){
	     		return p;
			 } else {
			 	p=p->next;
			 }
	     }
	    
	}
	return NULL;
}

void insertAfterNode(int item, int d)
{
node *a= search(item);
struct node *t= new node;
t->data=d;
if(a==NULL)
{
cout<<"node not found cannot insert after it"<<endl; return;
}
else
{
    t->next=a->next;
    a->next= t ;
}
}
// search
node* searchNode(int s)
{
if(head==NULL)
    {
    cout<<"List is empty"<<endl;
	return NULL;
    }
else
{
struct node *p=head;
while(p!=NULL)
    {
        if(s==p->data)
        {
            cout<<"item found"<<endl;
			return p;
        }
        else
        {
        p=p->next;
        }
    }
cout<<" item not found"<<endl;

}
return NULL;
}

void display(){
	if(head==NULL)
	{
	cout<<"List is empty."<<endl;
	}
	else{
	     struct node *p=head;
	     cout<<"List elements are : ";
	     while(p!=NULL)
	     {
		     cout<<p->data<<"  ";
		     p= p->next;
	     }
	    cout<<"\n";
	}
}


int main(){
	insertatB();
	insertatB();
	insertatB();
	insertatL();
	insertAfterNode(12,6);
//	node* res=search(20);
//	if(res==NULL){
//		cout<<"not found";
//	} else {
//		cout<<"found";
//	}
}


