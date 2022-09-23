#include<iostream>
#include<vector>

using namespace std;

int main()
{
    int a[5],b[5];
    cout<<"enter numbers";
    for(int i=0;i<5;i++)
    {
        cin>>a[i];
    }
    cout<<"for b enter number"<<endl;
    for(int i=0;i<5;i++)
    {
        cin>>b[i];
    }
    vector<int> v;
    for(int i=0,j=0;i<5,j<5;i++,j++)
    {
        int temp = a[i] + b[j];
        int n = temp % 10;
        v.push_back(n);

    }
    for(int i=0;i<v.size();i++)
    {
        cout<<v[i]<<"   ";
    }
    return 0;


}