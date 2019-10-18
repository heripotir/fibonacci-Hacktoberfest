function y = fibo(x)
global f=zeros(1,x);
f = [ f 
if((x+1==1)||(x+1==0))
    y=1;
else
    y= fibo(x-2)+fibo(x-1);
    fiboarray(x+1,1)=y;
end
end


fiboarray(n,1);
fiboarray(1,1)=0;
fiboarray(2,1)=1;
fiboarray(x+1,1)=y;