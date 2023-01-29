// find the nth prime

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

void printArray(int arr[], int size, string name) {
    cout << name;
    for (int i=0; i<size; i++) { 
        int ai = arr[i];
        if (ai==0) {break;}
        cout << arr[i] << ", ";}
    cout << endl;
}

int primesTo(int n) {
        int sieve[n] = {};
        string sieveName = "Sieve : ";
        for (int i=2; i<=n; i++) { sieve[i] = 1; }
        int primes[(n+1)/2] = {};
        string primeString = "Primes : ";

    	int pi = 0;
    	for (int m=2; m<=n; m++) {
    		if (sieve[m]) {
    			primes[pi++] = m;
    			for (int j=m*m; j<=n; j+=m) {
    				sieve[j] = 0;
    			}
    		}
    	}
        // printArray(sieve,n,sieveName);
        printArray(primes,(n+1)/2, primeString);
    	return 0;
    /*
def primes_to(n):
    sieve=[1]*(n+1)
    primes = []
    for m in range(2,n+1):
        if sieve[m]:
            primes += [m]
            for j in range(m*m,n+1,m): sieve[j]=0
    return primes
*/
    }

int main(){

    int t = 1;
    // cin >> t;
    for(int i = 0; i < t; i++){
        int n = 50000;
        // cin >> n;
        primesTo(n);
    }
    return 0;
}


