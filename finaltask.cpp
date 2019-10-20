#include <iostream>
using namespace std;

int gcd(int a, int b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);

}

int main()
{
    int N, i, max=1, res=0;
    cin >> N;
    int a[N];
    for(i=0 ; i<N ; i++)
    {
        cin >> a[i];
        res = gcd(a[i], res);
        if(res == 1)
        {
            break;
        }
    }
    cout << (res*N) << "\n";
    return 0;
}
