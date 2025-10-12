load hospital.mat

%hospital.BloodPressure
%hospital.Smoker
%hospital.BloodPressure(:,1);

%a=cov(hospital.Weight,hospital.BloodPressure);

b=cov(hospital.Weight); %Variance

%created a maxtrix of individual columns and then COV
matty=[hospital.Weight hospital.BloodPressure(:,1) hospital.BloodPressure(:,2)];
disp(matty)
a=cov(matty);
disp(a);

%

corrcoef([hospital.Age hospital.BloodPressure])

