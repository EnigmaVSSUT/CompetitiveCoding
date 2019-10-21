#include <iostream>
#include <string.h>

using namespace std;

class Word
{
public:
    string s;
    int v, T, F;
    void get()
    {
        cin >> s >> v;
    }
    Word()
    {
        T = 0;
        F = 0;
    }
    friend int check(Word w[], Word x, int *n)
    {
        int i;
        for(i=0; i<(*n) ; i++)
        {
            if(w[i].s == x.s)
            {
                if(x.v == 1)
                {
                    w[i].T += 1;
                }
                else if(x.v == 0)
                {
                    w[i].F += 1;
                }
                return 1;
            }
        }
        w[(*n)-1].s = x.s;
        w[(*n)-1].v = x.v;
        if(x.v == 0)
            w[(*n)-1].F += 1;
        else
            w[(*n)-1].T += 1;
        (*n)++;
        return 0;
    }
};


int main()
{
    int test;
    cin >> test;
    while(test--)
    {
        int N, n = 1, i, j, result = 0;
        cin >> N;
        Word arr[N], arrf[N];
        for(i=0 ; i<N ; i++)
        {
            arr[i].get();
            check(arrf, arr[i], &n);
        }
        for(j=0 ; j<(n-1) ; j++)
        {
            if(arrf[j].T >= arrf[j].F)
                result += arrf[j].T;
            else
                result += arrf[j].F;
        }
        cout << result << "\n";
    }
    return 0;
}
