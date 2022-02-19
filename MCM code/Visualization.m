LOG = csvread('log.csv');
[NUM,TXT,RAW]=xlsread('Analyzed_Data.CSV');

ind = NUM(:,1) + 1;
value = NUM(:, 3);
ma5 = NUM(:, 4);
ma30 = NUM(:, 7);

figure
hold on
plot(ind, value, "--", "linewidth", 1.5)
plot(ind, ma5, ":", "linewidth", 1.5)
plot(ind, ma30, "linewidth", 1.5)

sall_or_buy = LOG(2:end, 2);
sall_or_buy_index = LOG(2:end, 1);
sall_index = sall_or_buy_index(sall_or_buy == -1);
buy_index = sall_or_buy_index(sall_or_buy == 1);

scatter(sall_index, ma5(sall_index), 'r', "linewidth", 2)
scatter(buy_index, ma5(buy_index), 'black',"linewidth", 2)

legend("value", "ma5", "ma30","sall","buy")
hold off
