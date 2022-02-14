A=[1 2 5 
    1/2 1 2
    1/5 1/2 1]
%% 一致性检验和权向量计算
n = length(A);
[v,d]=eig(A);%计算特征根和特征向量
[temp,loc] = max(max(d));%返回loc为特征向量所在列
r=max(max(d));
CI=(r-n)/(n-1);
RI=[0 0 0.58 0.90 1.12 1.24 1.32 1.41 1.45 1.49 1.52 1.54 1.56 1.58 1.59];
CR=CI/RI(n);
if  CR<0.10 || n==2
    CR_Result='通过';
   else
    CR_Result='不通过';   
end
 
%% 权向量计算
w=v(:,loc)/sum(v(:,loc));
w=w';
 
%% 结果输出
disp('该判断矩阵权向量计算报告：');
disp(['CI:' num2str(CI)]);
disp(['CR:' num2str(CR)]);
disp(['一致性检验结果:' CR_Result]);
disp(['特征值:' num2str(r)]);
disp(['权向量:' num2str(w)]);
