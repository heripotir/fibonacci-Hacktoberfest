function y = matrixfibo(x)
%matrix based implementated fibonacci function
%useful information: https://medium.com/future-vision/fibonacci-sequence-algorithm-5eebae4e85be
k=([ 0 1 ; 1 1 ]^x)*[0 ; 1 ];
y=k(1,1);
end
