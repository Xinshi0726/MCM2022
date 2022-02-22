clear
[NUM,TXT,RAW]=xlsread('gold_lstm.csv');

ind = NUM(:,1);
output_gold = NUM(:,2);
value_gold = NUM(:,3);
error_gold = NUM(:,5);

output_bit = NUM(:,6);
value_bit = NUM(:,7);
error_bit = NUM(:,9);

%% Plot of Stock v.s. Price
figure 
tiledlayout(2,1)
% Top plot
nexttile
hold on
set(gca, 'Fontname', 'Times New Roman','FontSize',20);
grid on
title('LSTM result of Gold')
plot(ind, error_gold, "linewidth", 1.5, 'Color','#D95319')
xlabel('#day')
ylabel('Error')

yyaxis right

plot(ind, output_gold, "linewidth", 3, "Color", '#EDB120')
plot(ind, value_gold, '-.', "linewidth", 3, "Color", '#4DBEEE')
ylabel('Value($)')
legend("Error", "Predicted value", "Ground truth")
hold off

% Bottom plot
nexttile
hold on
set(gca, 'Fontname', 'Times New Roman','FontSize',20);
grid on
title('LSTM result of BitCoin')
plot(ind, error_bit, "linewidth", 1.5, 'Color','#D95319')

ylim([-1 1])
xlabel('#day')
ylabel('Error')

yyaxis right

plot(ind, output_bit, "linewidth", 3, "Color", '#EDB120')
plot(ind, value_bit, '-.', "linewidth", 3, "Color", '#4DBEEE')
ylabel('Value($)')

legend("Error", "Predicted value", "Ground truth")
hold off