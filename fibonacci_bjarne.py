import os

sl = "#include<iostream>\nusing namespace std;int fibonacci(int n){if(n==0){cout<<\"ULAN xd\"<<endl;return 0;}else if(n==1||n==2){return 1;}else{return fibonacci(n-1)+fibonacci(n-2);}}int main(){std::ios::sync_with_stdio(false);int fn;cout<<\"Enter which Fibonacci number you'd like to have: \"<<endl;cin>>fn;cout<<fibonacci(fn)<<endl;cout<<\"DIE POTATO DIE\"<<endl;return 0;}"
f = open("koluacik.cpp","w+")
f.write(sl)
f.close()
os.system("g++ koluacik.cpp -o koluacik")
os.system("./koluacik")
os.system("rm temp.cpp koluacik")
