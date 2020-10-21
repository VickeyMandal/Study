
#include<iostream>
using namespace std;
struct node{
	int data;
	struct node*left,*right;
};
struct node*root,*parent;

struct node* search(int item)
{
	node*p,* save;;
    if(root==NULL)
    {
     parent=NULL;
     return NULL;
    }
    
    else if(item==root->data)
    {
        parent=NULL;
        return root;
    }
    else if(item<root->data)
    {
        p=root->left;
        save=root;
    }
    else
    {
        p=root->right;
        save=root;
    }
    
    while(p!=NULL)
    {
        if(item==p->data)
        {
            parent=save;
            return p;
        }
      if(item<p->data)
      {
          save=p;
          p=p->left;
      }
      
      else 
      {
          save=p;
          p=p->right;
      }
    }
    parent=save;
    cout<<"search was unsuccesuull"<<"\n";
    return NULL;
   	
}
void insert(int item)
{
	node* loc=search(item);
	if(loc!=NULL)
     {
       return;
     }
	struct node*t=new node;
     //t=t->left;
	t->data=item;
	t->left=NULL;
	t->right=NULL;
	
	if (parent==NULL)
	{
		root=t;
	}
	
	else if(item<parent->data)
	parent->left=t;
	
	else
	parent->right=t;
	
	return ;
}

void preorder(node *r)
{
	struct node*p=r;
	if(r!=NULL)
	{
		cout<<p->data<<"\n";
		preorder(p->left);
		preorder(p->right);
	}
}
void inorder(node *r)
{
	struct node*p=r;
	if(r!=NULL)
	{
		preorder(p->left);
		cout<<p->data<<"\n";
		preorder(p->right);
	}
}
void postorder(node *r)
{
	struct node*p=r;
	if(r!=NULL)
	{
		preorder(p->left);
		preorder(p->right);
		cout<<p->data<<"\n";
	}
}

void delcaseA(node *loc, node *par){
	node *child;
	if (loc->left==NULL && loc->right==NULL){
		child=NULL;
	}
	else if(loc->left!=NULL){
		child=loc->left;
	}
	else{
		child=loc->right;
	}
	if(par==NULL){
		root=child;
	}
	else if(loc==par->left){
		
	}
}

void delnode(int item){
	node*loc = search(item);
	if(loc==NULL){
		return;
	}
	
	if(loc->right!=NULL && loc->left=NULL){
		delcaseB(loc,par);
	}
	else{
		delcaseA(loc,par)
	}
}

int main()
{
	insert(20);insert(30);insert(10);insert(50);
	
	cout<<"Preorder traversal of tree is:"<<endl;
	preorder(root);
	cout<<"inorder traversal of tree is:"<<endl;
	inorder(root);
	cout<<"Postorder traversal of tree is:"<<endl;
	postorder(root);
}



