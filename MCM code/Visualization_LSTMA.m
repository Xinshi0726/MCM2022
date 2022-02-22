[log_NUM,log_TXT,logRAW] = xlsread('log_SLTMA.csv');
[NUM,TXT,RAW]=xlsread('Analyzed_Data.CSV');

ind = NUM(:,1);
value = NUM(:, 3);
ma5 = NUM(:, 4);
ma30 = NUM(:, 7);

figure
hold on
p = plot(ind, value, "linewidth", 1.2);
plot(ind, ma5, "--", "linewidth", 1.6)
plot(ind, ma30, ":", "linewidth", 1.6)
set(gca, 'Fontname', 'Times New Roman','FontSize',20);


sall_or_buy = log_NUM(2:end, 3);
sall_or_buy_index = log_NUM(2:end, 1); 
sall_index = sall_or_buy_index(sall_or_buy < 0);
buy_index = sall_or_buy_index(sall_or_buy > 0);

profit = log_NUM(2:end, 7);

bar(sall_or_buy_index(profit > 0), profit(profit > 0), 5,...
    'FaceColor', '#D95319', 'EdgeColor', 'none');
bar(sall_or_buy_index(profit < 0), profit(profit < 0), 1,...
    'FaceColor', '#4DBEEE', 'EdgeColor', 'none');

scatter(sall_index, value(sall_index + 1), 'r', "linewidth", 2)
scatter(buy_index, value(buy_index + 1), 'black',"linewidth", 2)

legend("value", "ma5", "ma30","earn", 'lost', "sell","buy")
title("sell&buy position with only SLTMA model")
xlabel("#day")
ylabel("stock price")

grid on
hold off
