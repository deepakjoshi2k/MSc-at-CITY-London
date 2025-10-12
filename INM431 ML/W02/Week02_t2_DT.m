load fisheriris.mat
c_tree=fitctree(meas,species)
view(c_tree)

%Decision tree for classification Algorithm
%1  if x3<2.45 then node 2 elseif x3>=2.45 then node 3 else setosa
%2  class = setosa
%3  if x4<1.75 then node 4 elseif x4>=1.75 then node 5 else versicolor
%4  if x3<4.95 then node 6 elseif x3>=4.95 then node 7 else versicolor
%5  class = virginica
%6  if x4<1.65 then node 8 elseif x4>=1.65 then node 9 else versicolor
%7  class = virginica
%8  class = versicolor
%9  class = virginica

%to plot DT Graph
%view(c_tree,'mode','graph')

n=size(meas,1);
rng(1) %like seed in python

idxTrn = false(n,1) %training data mask
idxTrn(randsample(n,round(0.7*n)))= true
idxTest= idxTrn==false %testing data

model=fitctree(meas(idxTrn,:), species(idxTrn)) %Model training
label = predict(model,meas(idxTest,:))
label(randsample(numel(label),5))
numMisclass = sum(~strcmp(label,species(idxTest)))

