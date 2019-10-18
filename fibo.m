function y = fibo(x)
%classical implementation of fibonacci on MATLAB
if((x==0))
    y=0;
else if (x==1)
        y=1;
    else
    y= fibo(x-2)+fibo(x-1);
    end  
end
end
