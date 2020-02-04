# coding=utf-8
int main()
{
    int n;
    int a,b,c;
    while(cin>>n)
    {
        a=n%10;
        b=(n/10)%10;
        c=n/100;
        if(a*a*a+b*b*b+c*c*c==n)
            cout<<"Yes"<<endl;
        else
            cout<<"No"<<endl;
    }
    return 0;
}