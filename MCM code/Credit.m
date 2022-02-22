clear
[NUM,TXT,RAW]=xlsread('credit.CSV');
ind = NUM(:,1);
value_bit = NUM(:,3);
value_gold = NUM(:,7);
score_gold = NUM(:,12);
score_bit= NUM(:,13);
stock_gold = NUM(:,14);
stock_bit = NUM(:,15);
stock_money = NUM(:,16);
asset_gold = NUM(:,17);
asset_bit = NUM(:,18);
asset_total = NUM(:,19);
buy_gold = NUM(:,20);
buy_bit = NUM(:,21);

%% Plot of Asset
figure
hold on
set(gca, 'Fontname', 'Times New Roman','FontSize',20);
grid on
title("Assets")
plot(ind, asset_total, "linewidth", 3, "Color", '#EDB120')
plot(ind, asset_bit, "-.", "linewidth", 2,"Color",'#4DBEEE')
xlabel('#day')
ylabel('Dollar($)')

yyaxis right
plot(ind, asset_gold, "linewidth", 2, 'Color','#D95319')
ylabel('Dollar ($) of gold')
legend("BitCoin + Gold + Cash", "BitCoin asset", "Gold asset")
hold off

%% Plot of Stock v.s. Price
figure 
tiledlayout(2,1)
% Top plot
nexttile
hold on
set(gca, 'Fontname', 'Times New Roman','FontSize',20);
grid on
title('Stock v.s. Price of BitCoin')

plot(ind, stock_bit, '-.', "linewidth", 3, "Color", '#EDB120')
xlabel('#day')
ylabel('Unit of Stack')

yyaxis right
plot(ind, value_bit, "linewidth", 3, 'Color','#D95319')
ylabel('Value($)')
legend("Stock of BitCoin", "BitCoin value")
hold off

% Bottom plot
nexttile
hold on
set(gca, 'Fontname', 'Times New Roman','FontSize',20);
grid on
title('Stock v.s. Price of Gold')

plot(ind, stock_gold, '-.',"linewidth", 3, "Color", '#EDB120')
xlabel('#day')
ylabel('Unit of Stack')

yyaxis right
plot(ind, value_gold, "linewidth", 3, 'Color','#D95319')
ylabel('Value($)')
legend("Stock of Gold", "Gold value")
hold off


%% Plot of Purchase & Sell Position
figure 
tiledlayout(2,1)
% Top plot
nexttile
hold on
set(gca, 'Fontname', 'Times New Roman','FontSize',20);
grid on
title('Purchase & Sell of BitCoin')

plot(ind, value_bit, "linewidth", 3, "Color", '#EDB120')
scatter(ind(buy_bit > 0), value_bit(buy_bit > 0), 'r',"linewidth", 2)
scatter(ind(buy_bit < 0), value_bit(buy_bit < 0), 'b',"linewidth", 2)
xlabel('#day')
ylabel('Value($)')

yyaxis right
bar(ind(buy_bit > 0), buy_bit(buy_bit > 0), 5,...
    'FaceColor', '#D95319', 'EdgeColor', 'none');

bar(ind(buy_bit < 0), buy_bit(buy_bit < 0), 0.5,...
    'FaceColor', '#4DBEEE', 'EdgeColor', 'none');
ylabel('Unit of operation')


legend("Value of BitCoin", "Purchase Point", "Sell Point", "Unit of Purchase", "Unit of Sell")
hold off

% Bottom plot
nexttile
hold on
set(gca, 'Fontname', 'Times New Roman','FontSize',20);
grid on
title('Purchase & Sell of Gold')

plot(ind, value_bit, "linewidth", 3, "Color", '#EDB120')
scatter(ind(buy_gold > 0), value_bit(buy_gold > 0), 'r',"linewidth", 2)
scatter(ind(buy_gold < 0), value_bit(buy_gold < 0), 'b',"linewidth", 2)
xlabel('#day')
ylabel('Value($)')

yyaxis right
bar(ind(buy_gold > 0), buy_gold(buy_gold > 0), 5,...
    'FaceColor', '#D95319', 'EdgeColor', 'none');

bar(ind(buy_gold < 0), buy_gold(buy_gold < 0), 5,...
    'FaceColor', '#4DBEEE', 'EdgeColor', 'none');
ylabel('Unit of operation')


legend("Value of Gold", "Purchase Point", "Sell Point", "Unit of Purchase", "Unit of Sell")
hold off
