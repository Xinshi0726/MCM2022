[ml_NUM,ml_TXT,mlRAW] = xlsread('log_ml.csv');
[log_NUM,log_TXT,logRAW] = xlsread('log_SLTMA.csv');
[NUM,TXT,RAW]=xlsread('Analyzed_Data.CSV');

ind = NUM(:,1);
value = NUM(:, 3);
ma5 = NUM(:, 4);
ma30 = NUM(:, 7);


money_sltma = log_NUM(2:end,6);
money_ml = ml_NUM(2:end,6);

figure
hold on
set(gca, 'Fontname', 'Times New Roman','FontSize',20);

plot(log_NUM(2:end, 1), money_sltma, "linewidth", 2);
plot(ml_NUM(2:end, 1), money_ml, "linewidth", 2);

legend("Model I", "Model II")
title("Asset when using Model I and Model II for Bit coin")
xlabel("#day")
ylabel("Total asset")

grid on
hold off